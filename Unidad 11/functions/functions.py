def sumar(*nums: float) -> float | None:
    """
    Suma x cantidad de numeros y retorna el resultado redondeado a 2 dígitos,
    o None en caso de recibir algún parámetro no numérico.

    Args:
        nums (float): números a sumar.

    Returns:
        float | None: Resultado de la suma redondeada a 2 dígitos o None.
    """
    # Inicio la operación en 0
    resultado = 0.0
    try:
        # Le sumo todos los números
        for num in nums:
            if type(num) not in [int, float]:
                raise ValueError
            resultado += float(num)
    except ValueError:
        return None
    else:
        return round(resultado, 2)


def restar(*nums: float) -> float | None:
    """
    Resta x cantidad de numeros y retorna el resultado redondeado a 2 dígitos,
    o None en caso de recibir algún parámetro no numérico.

    Args:
        nums (float): números a restar.

    Returns:
        float | None: Resultado de la resta redondeada a 2 dígitos o None.
    """
    try:
        # Inicio la operación con el primer número y su signo original
        if type(nums[0]) not in [int, float]:
            raise ValueError
        resultado = float(nums[0])
        # Le resto los números restantes
        for num in nums[1:]:
            if type(num) not in [int, float]:
                raise ValueError
            resultado -= float(num)
    except ValueError:
        return None
    else:
        return round(resultado, 2)


def multiplicar(*nums: float) -> float | None:
    """
    Multiplica x cantidad de numeros y retorna el resultado redondeado
    a 2 dígitos, o None en caso de recibir algún parámetro no numérico.

    Args:
        nums (float): números a multiplicar.

    Returns:
        float | None: Resultado de la multiplicación
            redondeado a 2 dígitos o None.
    """
    try:
        # Inicio la operación con el primer número
        if type(nums[0]) not in [int, float]:
            raise ValueError
        resultado = float(nums[0])
        # Lo multiplico por los números restantes
        for num in nums[1:]:
            if type(num) not in [int, float]:
                raise ValueError
            resultado *= float(num)
    except ValueError:
        return None
    else:
        return round(resultado, 2)


def dividir(*nums: float) -> float | None:
    """
    Divide x cantidad de numeros y retorna el resultado redondeado a 2 dígitos,
    o None en caso de recibir algún parámetro no numérico
    o intentar dividir por cero.

    Args:
        nums (float): números a dividir.

    Returns:
        float | None: Resultado de la división redondeado a 2 dígitos o None.
    """
    try:
        # Inicio la operación con el primer número
        if type(nums[0]) not in [int, float]:
            raise ValueError
        resultado = float(nums[0])
        # Lo divido por los números restantes
        for num in nums[1:]:
            if type(num) not in [int, float]:
                raise ValueError
            resultado /= float(num)
    except ValueError:
        return None
    except ZeroDivisionError:
        return None
    else:
        return round(resultado, 2)
