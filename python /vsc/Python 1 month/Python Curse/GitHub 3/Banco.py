"""*4. Banco “PythonBank” – Evaluador de crédito*  
Como asesor financiero, quiero una función evaluar_credito(ingresos, edad) que:  
- Apruebe el crédito si los ingresos son mayores de 2 millones y la edad está entre 25 y 60.  
- Si no cumple, mostrar “Crédito rechazado”.  
Usar condicionales dentro de la función."""

Ingresos = float(input("Coloque sus ingresos : "))
Edad = int(input("Ingrese su edad: "))
def evaluar_credito(Ingresos,Edad):
    
    if Ingresos >= 2000000 and 25 <= Edad <=60:
            print("Credito aprobado")    
    else :
        print("Credito rechazado")

evaluar_credito(Ingresos,Edad)