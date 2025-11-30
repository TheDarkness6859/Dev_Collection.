"""*7. Panadería “Don Pancho” – Control de producción diaria*  
Como panadero, quiero una función hornear_pan(lotes) que use un for para indicar qué lote se está horneando.  
Si el lote es divisible por 3, mostrar “Verificación de calidad”.  
Al final, mostrar “Producción terminada”."""

def hornear_pan(lotes):
    for lote in range (1, lotes + 1):
        if lote % 3 == 0:
            print("Verificación de calidad")
        else:
            print(f"El lote {lote} se esta horneando")

hornear_pan(9)