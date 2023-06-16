from cosas import *

def main():

    per1 = Persona ("Luis", 18)
    print(per1)
    print(Persona.descripcion)

    print("---------- Herencia Alumno -------------")
    al1 = Alumno("Luis", 18, 320118121, 'ICO')
    print(al1)
    print(Alumno.descripcion)

    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Mario"
    print(al2)
    al2.dormir()

    print("-------------Herencia Profesor ----------")
    prof1 = Profesor("Jesus", 30 + 16, 3832783, "Ingenieria de software")
    print(prof1)
    prof1.dormir()

    print("---- Herencia Multiple --------")

    ay = AyudanteProfesor("Adrian", 20, 343, "ICO", 323, 'Ingenieria', 5)
    print(ay)
    a






main()
