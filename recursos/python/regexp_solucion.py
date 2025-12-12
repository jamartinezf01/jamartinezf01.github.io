import re

# ===============================================================
# CUADERNO DE EJERCICIOS – EXPRESIONES REGULARES 
# ===============================================================

# -----------------------------
# TEXTO BASE
# -----------------------------
texto = """
Nombre: Ana López, Edad: 29, Email: ana.lopez@example.com
Teléfono: 612334455
Dirección: Calle Sol 18, 3ºB
Compra reciente: 45.90€ el 12/01/2025
Código cliente: AA-12B-4456
"""

# ===============================================================
# BLOQUE 1 — BÚSQUEDA BÁSICA
# ===============================================================
print()
# Ejercicio 1:
# Encuentra todos los números del texto.
# (Pista: usa \d+)
# Escribe tu solución debajo:

numeros = re.findall(r"\d+", texto)
print("1) Números encontrados:", numeros)


# Ejercicio 2:
# Encuentra todas las palabras que empiecen por mayúscula.
# (Pista: \b[A-Z]\w+ )

palabras_mayus = re.findall(r"\b[A-ZÁÉÍÓÚÑ][a-zA-ZáéíóúñÑ]+", texto)
print("2) Palabras que empiezan por mayúscula:", palabras_mayus)

# Ejercicio 3:
# Extrae solo el nombre completo de la persona.
# (Pista: empieza por "Nombre:")

nombre = re.search(r"Nombre:\s*([^,]+)", texto).group(1)
print("3) Nombre completo:", nombre)


# ===============================================================
# BLOQUE 2 — GRUPOS DE CAPTURA
# ===============================================================

# Ejercicio 4:
# Extrae el nombre y la edad en forma de pareja.
# Formato esperado: ("Ana López", "29")
# (Pista: usa paréntesis en la regex)
# nombre_edad = ...
nombre_edad = re.findall(r"Nombre:\s*([^,]+),\s*Edad:\s*(\d+)", texto)
print("4) Nombre y edad:", nombre_edad[0])

# Ejercicio 5:
# Extrae la cantidad de dinero (45.90€)
# (Pista: [\d\.]+€ )
cantidad = re.search(r"[\d\.]+€", texto).group()
print("5) Cantidad encontrada:", cantidad)


# ===============================================================
# BLOQUE 3 — VALIDACIÓN
# ===============================================================

# Ejercicio 6:
# Comprueba si la fecha 12/01/2025 es válida con dd/mm/aaaa.
# (Pista: usar fullmatch con \d{2}/\d{2}/\d{4})

patron_fecha = r"\d{2}/\d{2}/\d{4}"
fecha=re.search(patron_fecha,texto).group()
fecha_valida = bool(re.fullmatch(patron_fecha, fecha))
print("6) Fecha válida:", fecha_valida)


# Ejercicio 7:
# Valida el código cliente AA-12B-4456 con la estructura:
# AAA–00A–0000
# (Pista: ^[A-Z0-9]{2,3}-\d{2}[A-Z]-\d{4}$)
codigo = "AA-12B-4456"
patron_codigo = r"^[A-Z0-9]{2,3}-\d{2}[A-Z]-\d{4}$"
codigo_valido = bool(re.fullmatch(patron_codigo, codigo))
print("7) Código cliente válido:", codigo_valido)


# ===============================================================
# BLOQUE 4 — SUSTITUCIÓN
# ===============================================================

# Ejercicio 8:
# Sustituye el email por "EMAIL-OCULTO".

texto_email_oculto = re.sub(r"[\w\.-]+@[\w\.-]+\.\w+", "EMAIL-OCULTO", texto)
print("8) Email oculto:\n", texto_email_oculto)


# Ejercicio 9:
# Sustituye el teléfono por "TEL-OCULTO".
texto_tel_oculto = re.sub(r"\d{9}", "TEL-OCULTO", texto)
print("9) Teléfono oculto:\n", texto_tel_oculto)



print()