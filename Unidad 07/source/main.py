from empleado import Empleado


def main():
    # Define un Empleado, calcula su edad, y lo presenta
    empleado1 = Empleado("Juan Ignacio", "Hernández", "21/05/1997", "40365768")
    print(empleado1.get_edad())
    print(empleado1.presentarse())


if __name__ == '__main__':
    main()
