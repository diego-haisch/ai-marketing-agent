# Replenish Engine

Motor de reaprovisionamiento de inventario multi-SKU / multi-tienda con dashboard ejecutivo de salud operativa.

## Stack

| Capa | Tecnología |
| --- | --- |
| Frontend | React 18 + Vite + TypeScript |
| Estilos | Tailwind CSS + design tokens ApplyChain |
| Backend | FastAPI (Python) |
| Motor | Python 3.12+ (stdlib, sin dependencias externas) |

## Estructura

```
├── src/              # Motor Python de reaprovisionamiento
├── frontend/         # Dashboard React
├── config/           # Parámetros configurables (settings.yaml)
├── data/raw/         # CSVs de entrada
├── data/output/      # Resultados generados
├── docs/adr/         # Decisiones de arquitectura
└── tests/            # Tests del motor
```

## Inicio rápido

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el motor
python main.py
```

Los resultados se escriben en `data/output/replenishment_results.csv`.

## Configuración

Edita `config/settings.yaml` para ajustar:

- `execution_date` — Fecha de ejecución
- `period_length_days` — Longitud del período en días
- `service_level` — Nivel de servicio objetivo (default: 0.95)
- `auto_service_level` — Habilitar service level automático por SKU

## Licencia

Privado — ApplyChain
