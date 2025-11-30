"""*5. Escuela “Aprende Más” – Promedio de notas*  
Como profesor, quiero una función promedio_notas() que reciba tres notas y calcule el promedio.  
Si el promedio es mayor o igual a 3.0 → mostrar “Aprobado”, de lo contrario “Reprobado”.  
Debe repetirse para varios estudiantes usando un while."""

print("escuela ¡aprende màs!")
def promedio_nota():
 while True:
        
        n1=float(input("ingreasa primera nota:"))
        n2=float(input("ingreasa sengunda nota:"))
        n3=float(input("ingreasa tercera nota:"))

        promedio = ((n1) + (n2)+ (n3)) / 3
        print(promedio)
        
        if promedio <= 3.0 :
                print("reprobado")
        else:
                print("probado")   

promedio_nota()
