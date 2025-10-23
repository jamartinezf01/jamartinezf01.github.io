# ============================================================
# 🧩 EJERCICIOS DE PRÁCTICA — LIST COMPREHENSION EN PYTHON
# ============================================================

# 👉 Rellena cada línea con la expresión correspondiente.
#    Comprueba tus respuestas ejecutando el archivo paso a paso.
# ============================================================


# 🟢 NIVEL 1 — BÁSICOS

# 1. Generar una lista de números del 0 al 10
numeros = [i for i in range(11)]
print("1.",numeros)

# 2. Crear una lista con los cuadrados del 1 al 10
cuadrados = [i**2 for i in range(1, 11)]
print("2.",cuadrados)

# 3. Obtener una lista con los caracteres de la palabra "python"
letras = [c for c in "python"]
print("3.",letras)

# 4. Crear una lista con los números pares del 0 al 20
pares = [i for i in range(21) if i % 2 == 0]
print("4.",pares)

# 5. Generar una lista con el doble de cada número de [1, 3, 5, 7, 9]
doble = [n * 2 for n in [1, 3, 5, 7, 9]]
print("5.",doble)



# 🟡 NIVEL 2 — CON CONDICIONES

# 6. Obtener una lista con los números impares del 0 al 20
impares = [i for i in range(21) if i % 2 != 0]
print("6.",impares)

# 7. Palabras con más de 5 letras
palabras = ["manzana", "pera", "plátano", "uva"]
palabras_largas = [p for p in palabras if len(p) > 5]
print("7.",palabras_largas)

# 8. Múltiplos de 3 entre 1 y 30
multiplos_3 = [i for i in range(1, 31) if i % 3 == 0]
print("8.",multiplos_3)

# 9. Números positivos de la lista [4, -2, 7, -9, 0, 3]
numeros = [4, -2, 7, -9, 0, 3]
positivos = [n for n in numeros if n > 0]
print("9.",positivos)

# 10. Elementos mayores que 25 en [10, 20, 30, 40, 50]
mayores_25 = [n for n in [10, 20, 30, 40, 50] if n > 25]
print("10.",mayores_25)



# 🔵 NIVEL 3 — TRANSFORMACIONES Y COMBINACIONES

# 11. Convertir todos los elementos a mayúsculas
lenguajes = ["python", "java", "c++"]
mayus = [l.upper() for l in lenguajes]
print("11.",mayus)

# 12. Longitud de cada palabra
palabras = ["hola", "mundo", "python"]
longitudes = [len(p) for p in palabras]
print("12.",longitudes)

# 13. Combinar listas ["a","b","c"] y [1,2,3]
letras = ["a", "b", "c"]
numeros = [1, 2, 3]
combinadas = [(l, n) for l, n in zip(letras, numeros)]
print("13.",combinadas)

# 14. Convertir temperaturas de °C a °F
celsius = [0, 10, 20, 30]
fahrenheit = [c * 9/5 + 32 for c in celsius]
print("14.",fahrenheit)

# 15. Convertir "12345" en [1, 2, 3, 4, 5]
cadena = "12345"
numeros = [int(c) for c in cadena]
print("15.",numeros)



# 🧠 NIVEL 4 — LISTAS ANIDADAS

# 16. Todas las combinaciones posibles de (x, y)
x=[1, 2, 3]
y=['a', 'b']
combinaciones = [(i, j) for i in x for j in y]
print("16.",combinaciones)

# 17. Aplanar lista de listas
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
aplanada = [n for sublista in lista for n in sublista]
print("17.",aplanada)

# 18. Matriz 3x3 de ceros
matriz = [[0 for x in range(3)] for x in range(3)]
print("18.",matriz)

# 19. Elementos de la diagonal
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
diagonal = [matriz[i][i] for i in range(len(matriz))]
print("19.",diagonal)

# 20. Números del 1 al 50 que no sean múltiplos de 2 o de 5
no_multiplos = [i for i in range(1, 51) if not (i % 2 == 0 or i % 5 == 0)]
print("20.",no_multiplos)


# ============================================================
# ✅ Fin del ejercicio
# Sugerencia: prueba a cambiar los rangos o condiciones
# para observar cómo cambia el resultado.
# ============================================================
