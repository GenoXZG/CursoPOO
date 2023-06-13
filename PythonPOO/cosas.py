class Alumno:
    facultad = "FES Aragón edomex"

    def __init__(self, nom, ed, car):
        self.__nombre = nom
        self.__edad = ed
        self.__carrera = car

    def __str__(self):
        return f"Alumno: {self.__nombre}, Edad: {self.__edad}, Carrera: {self.__carrera}"