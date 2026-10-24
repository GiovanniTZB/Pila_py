CAPACIDAD = 8

pila = [None] * CAPACIDAD
tope = 0


def insertar(valor):
    global tope
    if tope == CAPACIDAD:
        print(f"Insertar({valor}) -> ERROR: desbordamiento (pila llena)")
        return False
    pila[tope] = valor
    tope += 1
    return True


def eliminar(nombre_var):
    global tope
    if tope == 0:
        print(f"Eliminar({nombre_var}) -> ERROR: subdesbordamiento (pila vacia)")
        return None
    tope -= 1
    valor = pila[tope]
    pila[tope] = None
    print(f"Eliminar({nombre_var}) -> {nombre_var} = {valor}")
    return valor


def dibujar():
    for i in range(CAPACIDAD - 1, -1, -1):
        celda = pila[i] if pila[i] is not None else " "
        flecha = "  <-- TOPE" if tope > 0 and i == tope - 1 else ""
        print(f"  {i + 1} | {celda} |{flecha}")
    print(f"  TOPE = {tope}")


operaciones = [
    ("a", "ins", "X"),
    ("b", "ins", "Y"),
    ("c", "del", "Z"),
    ("d", "del", "T"),
    ("e", "del", "U"),
    ("f", "ins", "V"),
    ("g", "ins", "W"),
    ("h", "del", "p"),
    ("i", "ins", "R"),
]

errores = []

for inciso, tipo, dato in operaciones:
    if tipo == "ins":
        print(f"\n{inciso}) Insertar(PILA, {dato})")
        ok = insertar(dato)
    else:
        print(f"\n{inciso}) Eliminar(PILA, {dato})")
        ok = eliminar(dato) is not None
    if not ok:
        errores.append(inciso)
    dibujar()

print("\n--- RESULTADO ---")
print(f"Elementos finales en la pila: {tope}")
print(f"Incisos con error: {', '.join(errores) if errores else 'ninguno'}")
