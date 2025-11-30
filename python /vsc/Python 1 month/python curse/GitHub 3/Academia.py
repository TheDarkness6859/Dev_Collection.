"""*10. Academia “CodeStart” – Tabla de multiplicar personalizada*  
Como estudiante, quiero una función tabla_multiplicar(numero) que use un for para mostrar la tabla del número dado hasta el 10.  
Si el resultado es mayor de 50, mostrar también “Resultado alto”."""

numero = int(input("que número quieres multiplicar: "))

def tabla_multiplicar(numero):
    for dato in range (1,10 +1):
        resultado = numero * dato
    if resultado > 50:
        print(f"el resultado de {numero} x {dato} = {resultado}, Resultado alto")
    else:
        print(f"el resultado de {numero} x {dato} = {resultado}")


tabla_multiplicar(numero)
    
