class Alumno:
    facultad = "FES Aragón"

    def __init__(self, nom, ed, carr):
        self.__nombre = nom
        self.__edad = ed
        self.__carrera = carr

    def set_nombre(self, nom):
        self.__nombre = nom

    def get_nombre(self):
        return self.__nombre

    def set_edad(self, ed):
        if ed >= 8 and ed < 120:
            self.__edad = ed
        else:
            print("Esa edad no esta permitida")
            self.__edad = 0
        return self.__edad

    def get_edad(self):
        return self.__edad

    def set_carrera(self, carr):
        self.__carrera = carr

    def get_carrera(self):
        return self.__carrera

    def __str__(self):
        cadena = "------------\n Nombre: " + self.__nombre
        cadena = cadena + "\n Edad: " + str(self.__edad)
        cadena = cadena + "\n Carrera: " + self.__carrera
        cadena = cadena + "\n ---------------------"
        return cadena
    def estudiar(self, horas):
        print(f"El alumno {self.__nombre } esta estudiando por {horas} horas ")

class Perro:
    reino = "Canino"
    def __init__(self, raza, edad , estatura):
        self.__raza = raza
        self.__edad = edad
        self.__estatura = estatura
    #Metodo de acceso get
    @property
    def raza(self):
        return self.__raza

    #Metodo de acceso set

    @raza.setter
    def raza(self, raza):
        self.__raza = raza

    @property
    def edad(self):
        return self.__edad


    @edad.setter
    def edad(self, edad):
        if edad >= 0 and edad < 20:
            self.__edad = edad
        else:
            print("Edad no permitida")
            self.__edad = 0


    @property
    def estatura(self):
        return self.__estatura

    @estatura.setter
    def estatura(self,estatura):
        if estatura >= 0.1 and estatura <1.1:
          self.__estatura = estatura
        else:
           print("Estatura inadecuada")
           self.__estatura = 0.1

    def __str__(self):

        cadena = "------------\n Raza: " + self.__raza
        cadena = cadena + "\n Edad: " + str(self.__edad)
        cadena = cadena + "\n Estatura: " + str(self.__estatura)
        cadena = cadena + "\n ---------------------"
        return cadena
    @staticmethod
    def es_cachorro(edad):
        return edad < 3
    @staticmethod
    def dormir(veces = 5):
        for n in range(veces):
            print(f"Dando vuelta {n + 1}")
        print("zzzzzz")

    @classmethod
    def perro_grande(cls, est):
        if est > 0.79:
            return cls("",0,est)
