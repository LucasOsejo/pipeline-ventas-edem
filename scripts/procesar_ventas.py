import json
import sys

archivo = sys.argv[1]
entorno = sys.argv[2]

with open(archivo, encoding="utf-8") as f:
    datos = json.load(f)

ventas = datos["ventas"]

# En staging se procesa solo una muestra (la mitad de las ventas)
if entorno == "staging":
    ventas = ventas[: len(ventas) // 2]

total = sum(v["cantidad"] * v["precio_unitario"] for v in ventas)

with open(f"reporte_{entorno}.txt", "w", encoding="utf-8") as f:
    f.write(f"Reporte de ventas - entorno: {entorno}\n")
    f.write(f"Periodo: {datos['periodo']}\n")
    f.write(f"Numero de ventas: {len(ventas)}\n")
    f.write(f"Facturacion total: {total:.2f} euros\n")

print(f"Reporte generado: reporte_{entorno}.txt")
