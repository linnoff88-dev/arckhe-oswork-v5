#!/usr/bin/env python3
"""Monta curso.html a partir dos fragmentos de aula em aulas/.

A Aula 1 vive dentro do próprio curso.html (é a referência do formato).
As aulas 2..7 são fragmentos gerados separadamente e inseridos aqui, sempre
imediatamente antes do <script src="assets/curso.js">.

Idempotente: remove as views 2..7 já montadas antes de inserir de novo.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURSO = os.path.join(ROOT, "curso.html")
ANCORA = '<script src="assets/curso.js"></script>'
AULAS = range(2, 8)


def main():
    doc = open(CURSO, encoding="utf-8").read()

    # remove montagens anteriores (idempotência)
    for n in AULAS:
        doc = re.sub(
            r'\n<!-- ===== AULA %d ===== -->\n<section class="view" id="v-aula-%d".*?\n</section>\n'
            % (n, n), "\n", doc, flags=re.S)

    partes = []
    for n in AULAS:
        p = os.path.join(ROOT, "aulas", f"aula-{n}.html")
        if not os.path.exists(p):
            print(f"FALTA: aulas/aula-{n}.html")
            return 1
        frag = open(p, encoding="utf-8").read().strip()
        if not frag.startswith(f'<section class="view" id="v-aula-{n}"'):
            print(f"FORMATO: aulas/aula-{n}.html não começa com a view esperada")
            return 1
        if not frag.endswith("</section>"):
            print(f"FORMATO: aulas/aula-{n}.html não termina com </section>")
            return 1
        partes.append(f"\n<!-- ===== AULA {n} ===== -->\n{frag}\n")

    if ANCORA not in doc:
        print("FALHA: âncora do motor não encontrada em curso.html")
        return 1
    doc = doc.replace(ANCORA, "".join(partes) + "\n" + ANCORA)
    open(CURSO, "w", encoding="utf-8").write(doc)

    n = len(re.findall(r'<section class="view" id="v-aula-', doc))
    print(f"curso.html montado: {n} aulas, {len(doc)//1024}KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
