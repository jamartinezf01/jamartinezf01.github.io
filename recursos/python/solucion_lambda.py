"""
Soluciones: Retos con funciones lambda
--------------------------------------
Cada reto se resuelve con una función lambda. Se incluyen comentarios explicativos.
"""

# 🧩 Reto 1: El precio con IVA
# Se multiplica cada precio por 1.21 para añadir el 21% de IVA
precios = [10, 25, 100, 4.5]
precios_finales = list(map(lambda p: round(p * 1.21, 2), precios))
print("Reto 1:", precios_finales)
# [12.1, 30.25, 121.0, 5.45]


# 🧩 Reto 2: Temperaturas positivas
# Se filtran las temperaturas mayores que 0
temperaturas = [-3, 5, 0, -1, 12, 8]
positivas = list(filter(lambda t: t > 0, temperaturas))
print("Reto 2:", positivas)
# [5, 12, 8]


# 🧩 Reto 3: Convertir a mayúsculas
# Se transforma cada palabra a mayúsculas con .upper()
palabras = ["python", "lambda", "funcion", "anonima"]
mayus = list(map(lambda w: w.upper(), palabras))
print("Reto 3:", mayus)
# ['PYTHON', 'LAMBDA', 'FUNCION', 'ANONIMA']


# 🧩 Reto 4: Ordenar jugadores por puntuación
# Se ordena según el segundo valor de la tupla
jugadores = [("Ana", 85), ("Luis", 92), ("Marta", 75), ("Pablo", 90)]
ordenados = sorted(jugadores, key=lambda j: j[1], reverse=True)
print("Reto 4:", ordenados)
# [('Luis', 92), ('Pablo', 90), ('Ana', 85), ('Marta', 75)]


# 🧩 Reto 5: Nombres que comienzan por “A”
# Se filtran los nombres que empiecen por "A"
nombres = ["Ana", "Luis", "Andrés", "María", "Antonio", "Lucía"]
con_a = list(filter(lambda n: n.startswith("A"), nombres))
print("Reto 5:", con_a)
# ['Ana', 'Andrés', 'Antonio']


# 🧩 Reto 6: Cuadrados de números pares
# Primero se filtran los pares, luego se eleva al cuadrado
numeros = [1, 2, 3, 4, 5, 6]
pares_cuadrado = list(map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, numeros)))
print("Reto 6:", pares_cuadrado)
# [4, 16, 36]


# 🧩 Reto 7: Clasificar notas
# Se devuelve una cadena según el rango de la nota
evaluar = lambda n: (
    "Suspenso" if n < 5 else
    "Aprobado" if n < 7 else
    "Notable" if n < 9 else
    "Sobresaliente"
)
print("Reto 7:", evaluar(8.5))
# Notable


# 🧩 Reto 8: Ordenar productos por precio (de menor a mayor)
# Se ordena por el segundo elemento (precio)
productos = [("cuaderno", 5), ("mochila", 45), ("boli", 2), ("calculadora", 55), ("agenda", 25)]
ordenados = sorted(productos, key=lambda p: p[1])
print("Reto 8:", ordenados)
# [('boli', 2), ('cuaderno', 5), ('agenda', 25), ('mochila', 45), ('calculadora', 55)]


# 🧩 Reto 9: Filtrar y transformar datos de una lista de diccionarios
# Se filtran los alumnos con nota >= 7 y se obtiene solo el nombre
alumnos = [
    {"nombre": "Ana", "nota": 8},
    {"nombre": "Luis", "nota": 5},
    {"nombre": "Marta", "nota": 9},
    {"nombre": "Pablo", "nota": 6},
]
buenos = list(map(lambda a: a["nombre"], filter(lambda a: a["nota"] >= 7, alumnos)))
print("Reto 9:", buenos)
# ['Ana', 'Marta']


# 🧩 Reto 10: Ordenar frases por longitud de palabra más larga
# Se calcula la longitud máxima de cada frase y se usa como clave
frases = [
    "El sol brilla",
    "Programar en Python es divertido",
    "Hola mundo",
    "Lambda es poderosa"
]
ordenadas = sorted(frases, key=lambda f: max(len(palabra) for palabra in f.split(" ")))
print("Reto 10:", ordenadas)
# ['El sol brilla', 'Hola mundo', 'Lambda es poderosa', 'Programar en Python es divertido']
