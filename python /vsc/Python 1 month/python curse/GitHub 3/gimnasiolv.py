"""*2. Gimnasio “Level Up” – Control de repeticiones*  
Como entrenador, quiero una función repeticiones(n) que use un bucle for para mostrar las repeticiones del 1 al número indicado.
Si el número actual es par, mostrar “Excelente forma”, si no, “Mantén el ritmo”."""

print("gimnasio level up")

def gimnasio () :
    i=int(input("ingrasa numero  de repeticiones:"))
    for i in range(1,i +1) :
        if i %2 == 0:
            print(i,"exelente forma")
        if i %2 != 0 :
            print(i,"manten el ritmo")

gimnasio()