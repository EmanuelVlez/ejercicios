# Tecnicas In-memory:
# 1.Almacenamiento en Memoria Principal (Main Memory Storage)
import redis

# Conectarse a Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Almacenar un valor
r.set('clave', 'valor')

# Obtener el valor almacenado
valor = r.get('clave')
print(valor.decode('utf-8'))  # Decodificar bytes a string


#2.Almacenamiento Columnar en Memoria (In-Memory Columnar Storage)

import pandas as pd

# Crear un DataFrame como ejemplo de almacenamiento columnar
data = {'id': [1, 2, 3],
        'nombre': ['Juan', 'Ana', 'Luis'],
        'edad': [23, 34, 45]}

df = pd.DataFrame(data)

# Acceder a una columna (almacenada contiguamente)
print(df['nombre'])


#3.Indices en Memoria (In-Memory Indexing)

# Agregar elementos con una puntuación para ordenar
r.zadd('mi_indice', {'item1': 1, 'item2': 2, 'item3': 3})

# Obtener elementos del conjunto ordenado
items = r.zrange('mi_indice', 0, -1)
print(items)


#4.Compresión en Memoria (In-Memory Compression)

import zlib

# Comprimir datos
data = "Este es un texto que quiero comprimir"
compressed_data = zlib.compress(data.encode('utf-8'))

# Almacenar datos comprimidos en Redis
r.set('compressed_data', compressed_data)

# Recuperar y descomprimir datos
retrieved_data = r.get('compressed_data')
original_data = zlib.decompress(retrieved_data).decode('utf-8')
print(original_data)


#5.Caching en Memoria (In-Memory Caching)

# Almacenar un valor en caché con expiración
r.set('clave_cache', 'valor_cache', ex=60)  # Expira en 60 segundos

# Recuperar el valor antes de que expire
valor_cache = r.get('clave_cache')
print(valor_cache.decode('utf-8') if valor_cache else "No encontrado")


#6.Procesamiento en Memoria (In-Memory Processing)


# Agregar elementos a una lista
r.rpush('mi_lista', 'a', 'b', 'c')

# Procesar datos en memoria, contar elementos
longitud_lista = r.llen('mi_lista')
print(f"La lista tiene {longitud_lista} elementos")


#7.Particionado de Datos en Memoria (In-Memory Data Partitioning)

# Particionamiento simple usando múltiples claves
r.set('part1', 'datos_para_part1')
r.set('part2', 'datos_para_part2')

# Acceder a los datos de diferentes particiones
part1_data = r.get('part1')
part2_data = r.get('part2')

print(part1_data.decode('utf-8'))
print(part2_data.decode('utf-8'))


