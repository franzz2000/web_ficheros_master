
#!/usr/bin/env python3
"""Genera hojas_ejercicios/indice.json a partir de los .xlsx presentes."""

import json
from collections import Counter
from pathlib import Path

carpeta = Path(__file__).resolve().parent.parent / "hojas_ejercicios"

# Obtener todos los archivos Excel
archivos = sorted(
    p.name
    for p in carpeta.glob("*.xlsx")
    if p.is_file() and not p.name.startswith("~$")
)

# Normalizar identificadores para detectar duplicados
def normalizar(texto):
    return "".join(
        c for c in texto.upper()
        if c not in " .-"
    )

# El identificador es ahora el nombre sin extensión
identificadores = [
    normalizar(Path(nombre).stem)
    for nombre in archivos
]

# Comprobar duplicados
duplicados = [
    ident
    for ident, n in Counter(identificadores).items()
    if n > 1
]

if duplicados:
    raise SystemExit(
        f"Identificadores duplicados: {duplicados}"
    )

# Generar índice
ruta_indice = carpeta / "indice.json"

ruta_indice.write_text(
    json.dumps(archivos, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8"
)

print(f"Índice generado con {len(archivos)} archivo(s).")

