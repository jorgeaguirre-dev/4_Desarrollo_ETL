# 4 - Desarrollo ETL

Este proyecto implementa un data pipeline usando Dagster para dos fines, como orquestador y catálogo de datos. El proceso ETL ingesta datos en bruto en dos archivos de datos que se actualizan con cierta frecuencia:
- Datos de cablemodems (JSON).
- Datos de clientes (CSV).
El proceso de transformación se realiza a través de una capa de staging, donde se limpian y transforman los datos, y luego se produce un reporte final con el análisis del estado de los cablemodems.


## Dagster
Usado no solo como orquestador sinó también como catálogo de datos vivo donde el estado de cada reporte es rastreable.

```bash
export DAGSTER_HOME=$(pwd)/.dagster_home
dagster dev -m my_etl/definitions.py -h 0.0.0.0 -p 3000

# Variante 1
export DAGSTER_HOME=/home/repo/Challenges/4_desarrollo_etl/.dagster_home
dagster dev -f my_etl/definitions.py

# Variante 2
export DAGSTER_HOME=$(pwd)/.dagster_home
PYTHONPATH=. venv/bin/dagster dev -m my_etl.definitions -h 0.0.0.0 -p 3000
```

http://localhost:3000

## Instalación
```bash
pip install -r requirements.txt
```


