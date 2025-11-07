"""
Actividad: Retos con funciones lambda
-------------------------------------
Completa los huecos marcados con # completa aquí usando funciones lambda.
Puedes usar map(), filter(), sorted() u otras funciones integradas.
"""

# # 🧩 Reto 1: El precio con IVA
# precios = [10, 25, 100, 4.5]
# precios_finales = list(map( # completa aquí, precios))
# print("Reto 1:", precios_finales)
# # Salida esperada: [12.1, 30.25, 121.0, 5.45]


# # 🧩 Reto 2: Temperaturas positivas
# temperaturas = [-3, 5, 0, -1, 12, 8]
# positivas = list(filter(# completa aquí, temperaturas))
# print("Reto 2:", positivas)
# # Salida esperada: [5, 12, 8]


# # 🧩 Reto 3: Convertir a mayúsculas
# palabras = ["python", "lambda", "funcion", "anonima"]
# mayus = list(map(# completa aquí, palabras))
# print("Reto 3:", mayus)
# # Salida esperada: ['PYTHON', 'LAMBDA', 'FUNCION', 'ANONIMA']


# # 🧩 Reto 4: Ordenar jugadores por puntuación
# jugadores = [("Ana", 85), ("Luis", 92), ("Marta", 75), ("Pablo", 90)]
# ordenados = sorted(jugadores, key=# completa aquí, reverse=True)
# print("Reto 4:", ordenados)
# # Salida esperada: [('Luis', 92), ('Pablo', 90), ('Ana', 85), ('Marta', 75)]


# # 🧩 Reto 5: Nombres que comienzan por “A”
# nombres = ["Ana", "Luis", "Andrés", "María", "Antonio", "Lucía"]
# con_a = list(filter(# completa aquí, nombres))
# print("Reto 5:", con_a)
# # Salida esperada: ['Ana', 'Andrés', 'Antonio']


# # 🧩 Reto 6: Cuadrados de números pares
# numeros = [1, 2, 3, 4, 5, 6]
# pares_cuadrado = list(map(# completa aquí, filter(# completa aquí, numeros)))
# print("Reto 6:", pares_cuadrado)
# # Salida esperada: [4, 16, 36]


# # 🧩 Reto 7: Clasificar notas
# evaluar = # completa aquí
# print("Reto 7:", evaluar(8.5))
# # Salida esperada: Notable


# # 🧩 Reto 8: Ordenar productos por precio (de menor a mayor)
# productos = [("cuaderno", 5), ("mochila", 45), ("boli", 2), ("calculadora", 55), ("agenda", 25)]
# ordenados = sorted(productos, key=# completa aquí)
# print("Reto 8:", ordenados)
# # Salida esperada: [('boli', 2), ('cuaderno', 5), ('agenda', 25), ('mochila', 45), ('calculadora', 55)]


# # 🧩 Reto 9: Filtrar y transformar datos de una lista de diccionarios
# alumnos = [
#     {"nombre": "Ana", "nota": 8},
#     {"nombre": "Luis", "nota": 5},
#     {"nombre": "Marta", "nota": 9},
#     {"nombre": "Pablo", "nota": 6},
# ]
# buenos = list(map(# completa aquí, filter(# completa aquí, alumnos)))
# print("Reto 9:", buenos)
# # Salida esperada: ['Ana', 'Marta']


# # 🧩 Reto 10: Ordenar frases por longitud de palabra más larga
# frases = [
#     "El sol brilla",
#     "Programar en Python es divertido",
#     "Hola mundo",
#     "Lambda es poderosa"
# ]
# ordenadas = sorted(frases, key=# completa aquí)
# print("Reto 10:", ordenadas)
# # Salida esperada:
# # ['El sol brilla', 'Hola mundo', 'Lambda es poderosa', 'Programar en Python es divertido']
