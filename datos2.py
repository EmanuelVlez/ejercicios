import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('archivo.csv')

# Eliminar filas con valores nulos
df = df.dropna()

# Aplicar una función a una columna (por ejemplo, multiplicar por 2)
df['columna'] = df['columna'].apply(lambda x: x * 2)

# Guardar el DataFrame en un nuevo archivo CSV
df.to_csv('archivo_procesado.csv', index=False)

import pandas as pd

# Extraer: Leer el archivo CSV
df = pd.read_csv('archivo.csv')

# Transformar:
# 1. Eliminar filas con valores nulos
df = df.dropna()

# 2. Renombrar columnas para mayor claridad
df.rename(columns={'columna_original': 'columna_renombrada'}, inplace=True)

# 3. Convertir la columna 'fecha' de texto a datetime
df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d')

# 4. Agregar una nueva columna calculada
df['nueva_columna'] = df['columna_renombrada'] * 2

# 5. Filtrar filas que cumplan una condición (e.g., valores mayores a 100 en 'columna_renombrada')
df = df[df['columna_renombrada'] > 100]

# Cargar: Guardar el DataFrame transformado en un nuevo archivo CSV
df.to_csv('archivo_procesado.csv', index=False)



from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr
from pyspark.sql.types import DateType

# Crear una sesión de Spark
spark = SparkSession.builder \
    .appName("ETL Example") \
    .getOrCreate()


# Leer el archivo CSV
df = spark.read.csv('archivo.csv', header=True, inferSchema=True)

df = df.dropna()

df = df.withColumnRenamed('columna_original', 'columna_renombrada')

df = df.withColumn('fecha', col('fecha').cast(DateType()))

df = df.withColumn('nueva_columna', col('columna_renombrada') * 2)

df = df.filter(col('columna_renombrada') > 100)

df.write.csv('archivo_procesado.csv', header=True, mode='overwrite')


from pyspark.sql.functions import col

# Multiplicar los valores de la columna 'columna_renombrada' por 2
df = df.withColumn('nueva_columna', col('columna_renombrada') * 2)




