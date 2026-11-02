import re
import sys

archivo = sys.argv[1]

# Patrones tipicos de claves API (AWS, GitHub, Stripe y una generica)
patrones = [
    r"AKIA[0-9A-Z]{16}",
    r"ghp_[A-Za-z0-9]{36}",
    r"sk_live_[A-Za-z0-9]+",
    r"api_key",
]

with open(archivo, encoding="utf-8") as f:
    contenido = f.read()

encontradas = [p for p in patrones if re.search(p, contenido)]

if encontradas:
    print("Se han encontrado posibles claves API expuestas:", encontradas)
    sys.exit(1)

print("Escaneo correcto: no hay claves API expuestas en", archivo)
