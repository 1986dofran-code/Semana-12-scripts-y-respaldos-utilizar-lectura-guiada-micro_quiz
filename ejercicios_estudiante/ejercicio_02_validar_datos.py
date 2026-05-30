"""
Ejercicio 2 - Validar datos de produccion

Objetivo:
Crear una funcion que revise si una cantidad es valida.

Reglas:
1. No puede estar vacia.
2. Debe ser numerica.
3. No puede ser negativa.
"""


def validar_cantidad(valor: str) -> bool:
    if not valor or valor.strip() == "":
        return False
    try:
        cantidad = float(valor)
        return cantidad >= 0
    except ValueError:
        return False


if __name__ == "__main__":
    pruebas = ["20", "0", "-5", "", "abc", "13.5"]
    for prueba in pruebas:
        print(prueba, "=>", validar_cantidad(prueba))
