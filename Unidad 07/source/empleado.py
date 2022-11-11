from datetime import date


class Empleado():
    """
    Clase que representa un empleado.
    Tiene las propiedades de una persona cualquiera.

    :ivar nombre: Nombre o nombres de la persona.
    :vartype nombre: str
    :ivar apellido: Apellido o apellidos de la persona.
    :vartype apellido: str
    :ivar fecha_nacimiento: Fecha de nacimiento en formato dd/mm/aaaa.
    :vartype fecha_nacimiento: str
    :ivar nro_dni: Documento Nacional de Identidad (8 digitos).
    :vartype nro_dni: int
    """

    def __init__(self, nombre: str, apellido: str,
                 fecha_nacimiento: str, nro_dni: int):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.nro_dni = nro_dni

    def get_edad(self) -> int:
        """
        Calcula la edad del Empleado.

        :return: Edad del empleado.
        :rtype: int
        """
        anio_actual = date.today().year
        anio_nacimiento = self.fecha_nacimiento[-4:]
        return int(anio_actual) - int(anio_nacimiento)

    def presentarse(self) -> str:
        """
        Construye una breve presentación del empleado,
        informando acerca de sus datos personales.

        :return: Mensaje en formato presentación.
        :rtype: str
        """
        return f"Hola, soy {self.nombre} {self.apellido}. " + \
            "Nací el {self.fecha_nacimiento} y mi DNI es {self.nro_dni}."
