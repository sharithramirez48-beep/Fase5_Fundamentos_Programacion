# FASE 5 - EVALUACIÓN FINAL POA
# Estudiante: Sharith Dayana Ramirez Ramirez
# Programa: Ingeniería de Sistemas
# Problema 3: Control de inventario

# Matriz de inventario
inventario = [
    ["A001", "Arroz", 10, 20],
    ["A002", "Aceite", 15, 15],
    ["A003", "Azúcar", 5, 12],
    ["A004", "Leche", 8, 18],
    ["A005", "Café", 25, 20]
]


# Función para calcular la cantidad que se debe pedir
def calcular_reabastecimiento(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


# Mostrar informe de inventario
print("======================================")
print("       INFORME DE INVENTARIO")
print("======================================")

for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_reabastecimiento(
        stock_actual, stock_minimo
    )

    print("\nCódigo:", codigo)
    print("Artículo:", nombre)
    print("Stock actual:", stock_actual)
    print("Stock mínimo:", stock_minimo)
    print("Cantidad a solicitar:", cantidad_pedir)

    if cantidad_pedir > 0:
        print("Estado: Necesita reabastecimiento")
    else:
        print("Estado: Stock suficiente")

print("\n======================================")
print("       FIN DEL INFORME")
print("======================================")