"""*13. Tienda Online “ShopMaster” – Carrito de compras con validaciones*  
Como comprador, quiero una función carrito() que permita ingresar precios de productos y valide:  
- Si el precio es negativo, mostrar error y pedir otro valor.  
- Si el precio es mayor a 100.000, aplicar un 20% de descuento.  
Usar while y if dentro de la función hasta ingresar 0 para finalizar."""

def carrito():
    
    while True:
        try:
            precio = float(input("Ingresa el precio de los productos en pesos"))
            if precio <= 0:
                print("ingrese un número valido")
        except ValueError:
            print("Solo puedes ingresar números")
            if precio == 0:
                print("Tarea finalizada.")
                break
            elif precio > 100000:
                descuento = precio * 0.20
                print("tienes un 20% de descuento")
                
    