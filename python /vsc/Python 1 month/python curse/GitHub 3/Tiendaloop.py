"""*3. Tienda “LoopShop” – Descuentos acumulados*  
Como vendedor, quiero una función aplicar_descuentos() que pida varios precios hasta que el usuario escriba 0.  
Si el precio supera 50.000, aplicar 10% de descuento.  
Al final, mostrar la suma total de las compras con descuento."""

compras =[]
def aplicar_descuento():
    while True:
        try:
            print("Si escribes 0 dejas de poner el precio")
            precio = float(input("Ingresa el precio en pesos: "))   
        except ValueError:
            print("Debes ingresar un valor valido, (1000 o 20000)")
            continue

        if precio < 0:
            print("Necesitas ingresar un valor adecuado")
            continue

        elif precio == 0:
            break

        elif precio > 50000:
            descuento = precio * 0.10
            final = precio - descuento
            compras.append(final)
            print("tienes un descuento del 10%")
    
        else:
            compras.append(precio)
            print("Gracias por la compra <3")

suma = sum(compras)
        
aplicar_descuento()       

if compras:
    suma = sum(compras)
    print(f"la suma total de tus compras es: {suma}")
else:
    print("no se registraron compras")