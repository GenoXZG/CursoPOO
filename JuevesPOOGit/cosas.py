class Autor:
    def __init__(self, nombre, pseudonimo):
        self.__nombre = nombre
        self.__pseudonimo = pseudonimo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):

        self.__nombre = nombre

    @property
    def pseudo(self):
        return self.__pseudonimo

    @pseudo.setter
    def pseudo(self, pseudonimo):
        self.__pseudonimo = pseudonimo

    def __str__(self):
        return  f"Nombre: {self.__nombre} Pseudonimo: {self.__pseudonimo}"

    def escribir(self):
        print(f"{self.__nombre} esta escribiendo su siguiente libro")

class Libro:

    def __init__(self, Titulo, Autor, Anio, Editorial):

        self.__titulo = Titulo
        self.__autor = Autor
        self.__anio = Anio
        self.__editorial = Editorial

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def anio(self, anio):
        self.__anio = anio

    @property
    def editorial(self):
        return self.editorial

    @editorial.setter
    def editorial(self, editorial):
        self.__editorial = editorial

    def __str__(self):
        return f"Titulo: {self.__titulo}, Autor: {self.__autor}, Año: {self.__anio}, Editorial: {self.__editorial}"

    @classmethod
    def libro_planeta(cls,titulo,autor,anio):

        return cls(titulo, autor, anio , "Planeta")
    def leer(self, minutos):
        print(f"Leyendo por {minutos} minutos")

class Persona:

    def __init__(self, nombre, edad):
         self.__nombre = nombre
         self.__edad = edad

    @property
    def nombre(self):

      return  self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    def __str__(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}"

class Alumno(Persona):

    def __init__(self, nombre, edad, num_cuenta, carrera, promedio):
        super().__init__(nombre,edad)
        self.__num_cuenta = num_cuenta
        self.__carrera = carrera
        self.__promedio = promedio


    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Num. Cuenta: {self.__num_cuenta}, Carrera: {self.__carrera}, Promedio: {self.__promedio}"













