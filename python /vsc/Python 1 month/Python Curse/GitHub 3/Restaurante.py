
def calcular_propina():
    total_cuenta = float(input("Propina: "))
    if total_cuenta <= 100000:
        propina = total_cuenta * 0.10
        print(f"Tu propina es del 10%, tienes {propina} de propina")
    elif total_cuenta > 100000:
        propina1 = total_cuenta * 0.15
        print(f"Tu propina es del 15%, tienes {propina1} de propina")

calcular_propina()
calcular_propina()