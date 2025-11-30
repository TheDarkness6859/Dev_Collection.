"""*9. Tienda “EnergyStore” – Simulador de puntos*  
Como cliente, quiero una función calcular_puntos(compras) que use un for para recorrer la cantidad de compras (ingresada por el usuario).  
Si el número de compra es múltiplo de 3, agregar 10 puntos; en caso contrario, agregar 5.  
Al final, mostrar los puntos totales."""



def calcular_puntos(compras):
    try:
        compra = int(input("Ingresa la cantidad de compras: "))
    except ValueError:
        print("Debes ingresar un número entero")

    totalpuntos = 0

    for puntos in range(1,compra +1):
        if puntos % 3 == 0:
            totalpuntos += 10   
            print("se te han agregado 10 puntos")
        else:
            totalpuntos +=5
            print("se te han agregado 5 puntos")

    print(f"total de puntos aumulados {totalpuntos}")

calcular_puntos(1)