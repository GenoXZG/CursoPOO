from cosas import Alumno , Perro

def main():
    al1 = Alumno("Luis", 19, "ICO")
    print(vars(al1))

    al1.set_nombre("Ivan")
    print(vars(al1))
    print("-------- To String ----------")
    print(al1)
    al1.set_edad(999)
    print(al1)
    print("-------- Metodo ------------")
    print(al1.estudiar(8))
    print(" ---------- Clase Perro -----------")

    perro1 = Perro ("Poddle" , 2 , 0.35)
    print(vars(perro1))
    perro1.raza = "Solovino" #Set en notacion de Python
    perro1.edad = 4
    print(perro1)
    cachoro = Perro.es_cachorro(perro1.edad)
    print(cachoro)
    Perro.dormir()
    danes = Perro.perro_grande(0.8)
    print(danes)


main()