#!/usr/bin/env python3
"""Genera hojas_ejercicios/indice.json a partir de los .xlsx presentes."""
import json
from collections import Counter
from pathlib import Path

carpeta = Path(__file__).resolve().parent.parent / 'hojas_ejercicios'
archivos = sorted(p.name for p in carpeta.glob('*.xlsx') if p.is_file() and not p.name.startswith('~$'))

invalidos = [nombre for nombre in archivos if '_' not in nombre or not nombre.split('_', 1)[0]]
if invalidos:
    raise SystemExit(f'Nombres de archivo incorrectos: {invalidos}')

normalizar = lambda s: ''.join(c for c in s.upper() if c not in ' .-')
identificadores = [normalizar(nombre.split('_', 1)[0]) for nombre in archivos]
duplicados = [ident for ident, n in Counter(identificadores).items() if n > 1]
if duplicados:
    raise SystemExit(f'Identificadores duplicados: {duplicados}')

(carpeta / 'indice.json').write_text(json.dumps(archivos, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(f'Índice generado con {len(archivos)} archivo(s).')
