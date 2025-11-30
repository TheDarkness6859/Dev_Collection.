"""*6. Estación “LoopBus” – Simulador de pasajeros*  
Como conductor, quiero una función simular_viaje(pasajeros) que recorra con un for cada pasajero y muestre “Pasajero X a bordo”.  
Si llega a 10 pasajeros, mostrar “Bus lleno” y detener el bucle."""

Pasajeros = int(input("Coloque la cantidad de pasajeros: "))

def simular_viajeros():
    for Viajeros in range(1, Pasajeros + 1):
        print(f"Pasajero {Viajeros} a bordo")
        if Viajeros == 10 :
            print("Bus Lleno")
            break
        else:
            print("Ingrese valor correcto")

simular_viajeros()