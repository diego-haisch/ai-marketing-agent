# 🧭 Project Overview — Collection Flow Model

## 1. Descripción general

Este proyecto construye un sistema de **predicción de ventas y generación de propuestas de compra/asignación por tallas** basado en modelos de Machine Learning.

El sistema tiene dos modelos independientes:

- **Modelo de ventas** (`train.py`) — predice el ratio de ventas por producto y tienda
- **Modelo de curva de tallas** (`train_size_curve.py`) — predice la distribución de ventas entre posiciones de talla

Ambos modelos se combinan en el **pipeline de predicción** (`predict.py`) para generar propuestas de compra y distribución a nivel `producto × tienda × talla`.

El enfoque es **vectorizado, sin bucles por producto**, priorizando:
- rendimiento en batch
- trazabilidad
- separación clara entre API y lógica de negocio

---

## 2. Arquitectura del sistema

```
Excel (negocio)
    │  JSON input
    ▼
Backend API (infraestructura)
    │  POST /predict
    ▼
Business Box (este repositorio)
    ├── predict.py          ← lógica de predicción
    ├── train.py            ← entrena modelo de ventas
    ├── train_size_curve.py ← entrena modelo de tallas
    └── functions.py        ← utilidades comunes
```

### 2.1 Frontend (Excel)
- Genera inputs en formato tabla con un producto por fila
- Convierte a JSON y lanza petición `POST /predict`
- Recibe el JSON de respuesta y vuelca en Excel

### 2.2 Backend API (Infraestructura — externo a este repo)
- Desplegado en máquina virtual Ubuntu
- Expone los endpoints HTTP y orquesta los procesos Python
- Endpoint principal: `POST /predict` → llama a `predict_from_json()`

### 2.3 Business Box (este repositorio)
- Toda la lógica de negocio, transformaciones, entrenamiento y predicción
- Conexión directa a PostgreSQL para datos de entrenamiento
- Artefactos `.joblib` generados en `model/` y cargados en inferencia

---

## 3. Flujo de funcionamiento

### 3.1 Entrenamiento de ventas (`train.py`)

Se ejecuta bajo demanda. No recibe inputs externos.

1. Extrae datos de ventas, PVI, tiendas, SKU desde PostgreSQL
2. Construye variables derivadas: `sales_ratio`, `lifecycle`, `price_group`, `release_month`, etc.
3. Aplica one-hot encoding + escalado
4. Entrena un `RandomForestRegressor` con split estratificado
5. Evalúa con MAE, wMAE, RMSE, BIAS
6. Guarda artefactos en `model/`:
   - `rf_model_sales.joblib`
   - `sales_scaler.joblib` (contiene `scalerObj` + `columns`)
   - `price_thresholds.joblib`

---

### 3.2 Entrenamiento de curva de tallas (`train_size_curve.py`)

Trabaja a nivel `modcol` (no segmenta por tienda ni canal).

1. Extrae histórico de ventas por SKU desde PostgreSQL
2. Calcula el `withdrawal_date` por modcol: punto en que se alcanza el 50 % de ventas acumuladas (periodo "saludable", sin roturas de stock)
3. Agrega ventas por posición de talla dentro de cada modcol
4. Construye features: `size_count`, `release_year`, `family`, `category`, `size_type`
5. Target: vector de pesos por posición de talla (normalizado a 1)
6. Entrena un `RandomForestRegressor` multi-output con split estratificado
7. Evalúa con MAE por posición de talla
8. Guarda artefactos en `model/`:
   - `size_curve_model.joblib`
   - `size_curve_columns.joblib` (contiene `columns`, `scaler`, `y_cols`)

---

### 3.3 Pipeline de predicción (`predict.py`)

Recibe un DataFrame (o JSON) con un producto por fila y devuelve propuestas de compra y distribución.

```
df_products (1 fila/producto)
    │
    ├─ 1. Feature engineering vectorizado
    │      family, sku_count, release_year/month, sales_level,
    │      lifecycle_weeks, price_group
    │
    ├─ 2. Curva de tallas (batch ML)
    │      → size_df: {_pid, size_pos, size_weight}
    │
    ├─ 3. Expand × tiendas del cluster
    │
    ├─ 4. Predecir sales_ratio (vectorizado)
    │
    ├─ 5. Coverage + min_talla (vectorizado por producto)
    │      cov decrece linealmente de coverage_upper → coverage_lower por ranking
    │      min_talla: min_talla_top si cum_pct ≤ 90 %, min_talla_rest en el resto
    │
    ├─ 6. Lifecycle attrs + mínimo de allocation por tienda
    │      _alloc_store = max(sales_ratio × sku_count × cov, sku_count × min_talla)
    │
    ├─ 7. Expand × tallas (merge con size_df)
    │
    └─ 8. Propuestas finales
           purchase_qty   = max(⌊sales_ratio×sku_count×size_weight×weeks/sellthrough⌋, min_talla)
           allocation_qty = max(⌊_alloc_store×size_weight⌋, min_talla)

Output:
    purchase_df  — compra total por [product_id, size_pos]
    alloc_df     — distribución por [product_id, store, size_pos]
```

---

## 4. Estructura del proyecto

```
python-functions/
├── src/
│   ├── train.py                ← entrenamiento modelo de ventas
│   ├── train_size_curve.py     ← entrenamiento modelo de tallas
│   ├── predict.py              ← predicción batch + entrada JSON
│   └── functions.py            ← utilidades comunes (DB, transformaciones, config)
├── model/                      ← artefactos .joblib (generados por los trainers)
│   ├── rf_model_sales.joblib
│   ├── sales_scaler.joblib
│   ├── price_thresholds.joblib
│   ├── size_curve_model.joblib
│   └── size_curve_columns.joblib
├── data/
│   ├── store_cluster.csv       ← mapeo cluster → tiendas
│   └── family_classification.csv ← mapeo subfamilia → familia
├── sql/                        ← queries SQL parametrizadas
├── config/
│   ├── database.ini            ← credenciales PostgreSQL
│   └── model.ini               ← hiperparámetros y configuración del modelo
├── flask/
│   └── application.py          ← API Flask (gestionada por infraestructura)
└── requirements.txt            ← dependencias del proyecto (API, inferencia, notebooks y training)
```

---

## 5. Contrato de la API

### `POST /predict`

**Input** — JSON array, un objeto por producto:

```json
[
  {
    "product_id":     "BOOT-001",
    "cluster":        "EMOALL",
    "size_range_ref": "12",
    "category":       "CALZADO",
    "subfamily":      "Botín",
    "sales_level":    1,
    "year_in_store":  2026,
    "month_in_store": 5,
    "retail_price":   59.99,
    "life_cycle":     20
  }
]
```

Campos obligatorios: `product_id`, `cluster`, `size_range_ref`, `category`, `subfamily`, `sales_level`, `year_in_store`, `month_in_store`, `retail_price`, `life_cycle`.

- `sales_level` debe ser entero entre `1` y `4` (1=BS, 2=GS, 3=NS, 4=IM).
- `life_cycle` debe ser entero con número de semanas en tienda (ej: 20, 40, 60).

**Output** — JSON con tres keys:

```json
{
  "purchase":   [{"product_id": "BOOT-001", "size_pos": 1, "purchase_qty": 24}, ...],
  "allocation": [{"product_id": "BOOT-001", "store": "05", "size_pos": 1, "allocation_qty": 3}, ...],
  "errors":     []
}
```

Si hay campos faltantes, `errors` contendrá los mensajes descriptivos y `purchase`/`allocation` estarán vacíos (HTTP 422).

---

## 6. Instalación y uso

```bash
# Clonar y activar entorno
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS / Linux

# Producción (servidor Flask)
pip install -r requirements.txt

# Desarrollo local (training + exploración)
pip install -r requirements.txt
```

### Entrenar modelos

```bash
# Modelo de ventas
python src/train.py

# Modelo de curva de tallas
python src/train_size_curve.py
```

Ambos scripts leen la configuración de `config/model.ini` y las credenciales de `config/database.ini`.

### Probar la predicción en local

```bash
python src/predict.py
```

Ejecuta el bloque `__main__` con dos productos de ejemplo (`BOOT-001`, `JKT-002`) e imprime la propuesta de compra.

---

## 7. Configuración (`config/model.ini`)

Fuente única de verdad para todos los hiperparámetros. Secciones principales:

| Sección | Parámetros clave |
|---|---|
| `[paths]` | `model_dir` |
| `[features]` | `feature_cols`, `dummy_cols` |
| `[prediction]` | `coverage_upper`, `coverage_lower`, `min_talla_top`, `min_talla_rest` |
| `[size_curve]` | `dummy_cols`, `numeric_cols`, `stratify_col`, `min_qty_modcol` |
| `[lifecycle]` | atributos por ciclo de vida (sellthrough, weeks, etc.) |

---

## 8. Principios de desarrollo

- Mismas transformaciones en training y predicción (garantizado por `functions.py`)
- Predicción completamente vectorizada — sin bucles por producto ni por tienda
- Separación estricta entre API (infraestructura) y lógica de negocio (este repo)
- Un único `config/model.ini` como fuente de hiperparámetros
- Artefactos `.joblib` versionables y reproducibles

---

## 9. Pendiente de integración

- [ ] Integración con la nueva aplicación Flask del equipo de infraestructura
  - Punto de entrada: `from predict import predict_from_json`
  - Wiring: `result = predict_from_json(request.get_json())`
- [ ] Carga de modelos al arrancar Flask (una vez, no por request)
- [ ] Autenticación en el endpoint `/predict`


## 5. Bitacora real de instalacion y resolucion de xlwings

### 5.1 Instalacion

No se uso el manual basico. Se hizo con el Python correcto:

    pip install xlwings
    python -m xlwings.cli addin install

Punto clave: el add-in se instalo por CLI, no solo con pip.

### 5.2 Interprete

Se cambio el interprete desde la pestana xlwings en Excel para apuntar al Python deseado.

Este paso fue el detonante de errores posteriores cuando la configuracion no quedo consistente.

### 5.3 Error 62 (critico)

Al aparecer Error 62 tras cambiar interprete, la solucion efectiva fue forzar regeneracion de configuracion:

    xlwings config create --force

Esto reseteo la configuracion interna de xlwings y elimino el Error 62.

### 5.4 Centro de confianza (VBA)

Para desbloquear la ejecucion en Excel fue necesario:

- Activar: Confiar en el acceso al modelo de objetos de VBA.
- Trabajar desde una ubicacion de confianza.

No fue necesario habilitar todas las macros.

### 5.5 Error 1004 (Import Functions)

Al importar UDFs con Import Functions aparecio Error 1004.

Causa: bloqueo de VBA.

Solucion: aplicar configuracion del Centro de confianza (punto anterior). Tras eso, Import Functions funciono y las UDFs quedaron disponibles como formulas.