"""Script simples para ler e exibir o conteúdo de um arquivo CSV."""

import csv
import sys


def ler_csv(caminho):
    """Lê um CSV e retorna uma lista de dicionários (uma linha por item)."""
    with open(caminho, newline="", encoding="utf-8") as arquivo:
        return list(csv.DictReader(arquivo))


def main():
    if len(sys.argv) != 2:
        print("Uso: python ler_csv.py <arquivo.csv>")
        sys.exit(1)

    linhas = ler_csv(sys.argv[1])
    print(f"{len(linhas)} linha(s) lida(s).")
    for linha in linhas:
        print(linha)


if __name__ == "__main__":
    main()
