from cosas import Libro , Autor , Alumno , Persona

def main():

    l1 = Libro.libro_planeta("El perfume",Autor("Patrik", "PS"),1998)
    l1.autor.pseudo = l1.autor.pseudo.lower()
    print(l1)
    print("---- Persona ----------")
    a1 = Alumno("Luis", 18 , 3201171015, "ICO", 9.0)
    print(a1)

main()
