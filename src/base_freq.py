#!/usr/bin/env python3

# Programa: base_freq.py
# Objetivo: calcular frecuencias de bases A, C, G, T de un archivo FASTA

import argparse
import sys
import os

def leer_argumentos():
    parser = argparse.ArgumentParser(description="Calcula frecuencias de A, C, G y T en un archivo FASTA.")
    parser.add_argument("--input", required=True, help="Ruta al archivo FASTA")
    return parser.parse_args()

def leer_fasta(ruta):
    if not os.path.exists(ruta):
        print(f"ERROR: El archivo '{ruta}' no existe.")
        sys.exit(1)

    secuencia = ""

    with open(ruta, "r") as f:
        for linea in f:
            linea = linea.strip()
            if linea.startswith(">"):
                continue
            secuencia += linea.upper()

    return secuencia

def contar_bases(seq):
    conteo = {
        "A": seq.count("A"),
        "C": seq.count("C"),
        "G": seq.count("G"),
        "T": seq.count("T")
    }
    return conteo

def calcular_frecuencias(conteo):
    total = sum(conteo.values())

    if total == 0:
        print("ERROR: La secuencia está vacía.")
        sys.exit(1)

    frecuencias = {}
    for base, cantidad in conteo.items():
        frecuencias[base] = (cantidad / total) * 100

    return frecuencias
