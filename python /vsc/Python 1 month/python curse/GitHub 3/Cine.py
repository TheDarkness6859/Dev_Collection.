"""*8. Cine “MovieLoop” – Calculadora de entradas*  
Como cajero, quiero una función calcular_entradas() que pida edades de los clientes hasta que se ingrese 0.  
Aplicar precio:
- Menores de 12 → $5.000  
- De 12 a 59 → $8.000  
- Mayores de 60 → $4.000  
Usar un while y condiciones."""

def calcular_entradas():
    total = 0
    while True:
        edad = int(input("Ingresa la edad del cliente (0 para terminar): "))
        if edad == 0:
            break
        if edad < 12 :
            precio = 5000
            total += precio
        elif edad <= 59 :
            precio = 8000
            total += precio
        else :
            precio = 4000
            total += precio


    print("Tu valor total a pagar es",total)
calcular_entradas()