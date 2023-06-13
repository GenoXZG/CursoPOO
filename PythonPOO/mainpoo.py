from cosas import Alumno


def main():
    """
    al1 = Alumno()
    print(al1)
    al2 = Alumno()

    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)

    print("--------")

    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)
    print("Un vistazo a los objetos")
    print(vars(al1))
    print(vars(al2))
    print("------Modificar atributos publicos--------")
    al1.edad = 999 
     """
    al1 = Alumno("Diego", 19, "Economia")
    al1.facultad = "Fes aragon EDOMEX"  # Se agrega un atributo
    al2 = Alumno("Monse", 18, "Derecho")
    print(al1,",Facultad: " ,al1.facultad)
    print(al2,",Facultad: " ,al2.facultad)

main()
