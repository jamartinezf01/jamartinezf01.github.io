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



# Ejercicio 2:
# Encuentra todas las palabras que empiecen por mayúscula.
# (Pista: \b[A-Z]\w+ )


# Ejercicio 3:
# Extrae solo el nombre completo de la persona.
# (Pista: empieza por "Nombre:")



# ===============================================================
# BLOQUE 2 — GRUPOS DE CAPTURA
# ===============================================================

# Ejercicio 4:
# Extrae el nombre y la edad en forma de pareja.
# Formato esperado: ("Ana López", "29")
# (Pista: usa paréntesis en la regex)
# nombre_edad = ...


# Ejercicio 5:
# Extrae la cantidad de dinero (45.90€)
# (Pista: [\d\.]+€ )



# ===============================================================
# BLOQUE 3 — VALIDACIÓN
# ===============================================================

# Ejercicio 6:
# Comprueba si la fecha 12/01/2025 es válida con dd/mm/aaaa.
# (Pista: usar fullmatch con \d{2}/\d{2}/\d{4})




# Ejercicio 7:
# Valida el código cliente AA-12B-4456 con la estructura:
# AAA–00A–0000
# (Pista: ^[A-Z0-9]{2,3}-\d{2}[A-Z]-\d{4}$)



# ===============================================================
# BLOQUE 4 — SUSTITUCIÓN
# ===============================================================

# Ejercicio 8:
# Sustituye el email por "EMAIL-OCULTO".



# Ejercicio 9:
# Sustituye el teléfono por "TEL-OCULTO".



print()