# Forecast de Ventas - ML

Sistema de forecasting de ventas basado en Random Forest, disenado para prever la demanda futura a nivel SKC (Stock Keeping Color).

## Descripcion

Modelo de Machine Learning que aprende de tendencias historicas de venta y genera previsiones a 12 meses.

- **Granularidad**: SKC (agrupacion de colores, con tallas dentro)
- **Horizonte**: 12 meses
- **Algoritmo**: Random Forest Regressor
- **Fuente de datos**: Excel (MVP) -> Odoo + Shopify API (produccion)

## Estructura

```
├── data/
│   ├── raw/           # Excel historico, ficheros fuente
│   ├── processed/     # Modelo entrenado, datasets transformados
│   └── historical/    # Registro de ejecuciones de forecast
├── src/
│   ├── config.py      # Configuracion centralizada
│   ├── data_loader.py # Carga de datos (Excel, Odoo, Shopify)
│   ├── features.py    # Feature engineering
│   ├── train.py       # Entrenamiento del modelo
│   ├── predict.py     # Generacion de forecast
│   ├── evaluate.py    # Metricas de evaluacion
│   └── utils/         # Funciones auxiliares
├── tests/             # Tests unitarios
├── requirements.txt
├── dockerfile
└── .env.example
```

## Instalacion

1. Crear entorno virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# o
.venv\Scripts\activate     # Windows
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar variables de entorno:
```bash
cp .env.example .env
# Editar .env con tus valores
```

## Uso

### Colocar datos de entrada

Colocar el fichero Excel con historico de ventas en `data/raw/`. Por defecto se espera `ventas.xlsx`.

### Entrenar modelo

```bash
python src/train.py
```

### Generar forecast

```bash
python src/predict.py
```

### Ejecutar con Docker

```bash
docker build -t forecast-ml .
docker run -v $(pwd)/data:/app/data --env-file .env forecast-ml
```

## Configuracion

Las variables en `.env` permiten ajustar:

| Variable | Descripcion | Default |
|---|---|---|
| `X_LEN` | Meses historicos de input | 6 |
| `Y_LEN` | Meses de forecast | 12 |
| `N_ESTIMATORS` | Arboles en Random Forest | 20 |
| `MAX_DEPTH` | Profundidad maxima | 250 |
| `MIN_SAMPLES_SPLIT` | Min samples para split | 12 |
| `MIN_SAMPLES_LEAF` | Min samples por hoja | 4 |
| `DATA_SOURCE` | Fuente: excel, odoo, shopify | excel |
| `COL_*` | Mapeo de columnas del Excel | - |

## Formato de datos

El Excel de ventas debe contener como minimo:

| Columna | Descripcion | Ejemplo |
|---|---|---|
| Fecha de pedido | Fecha de la venta | 2024-01-15 |
| SKC | Codigo de color | SKC-001 |
| SKU | Codigo con talla | SKU-001-38 |
| Canal | Canal de venta | Online |
| Zona | Region/Zona | BCN |
| Cantidad vendida | Unidades | 10 |

## Contacto

Responsable: [Tu nombre]
Email: [tu@email.com]
