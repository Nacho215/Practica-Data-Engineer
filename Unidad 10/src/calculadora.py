

def sumar(num1: int, num2: int) -> int:
    """
    Suma 2 numeros y retorna el resultado.

    Args:
        num1 (int): número 1.
        num2 (int): número 2.

    Returns:
        int: Resultado de la suma.
    """
    return num1 + num2


def restar(num1: int, num2: int) -> int:
    """
    Resta 2 numeros y retorna el resultado.

    Args:
        num1 (int): número 1.
        num2 (int): número 2.

    Returns:
        int: Resultado de la resta.
    """
    return num1 - num2


def multiplicar(num1: int, num2: int) -> int:
    """
    Multiplica 2 numeros y retorna el resultado.

    Args:
        num1 (int): número 1.
        num2 (int): número 2.

    Returns:
        int: Resultado de la multiplicación.
    """
    result = num1 * num2
    if type(num1) != int or type(num2) != int:
        result = None
        raise TypeError
    return result


def dividir(num1: int, num2: int) -> int:
    """
    Divide 2 numeros y retorna el resultado.

    Args:
        num1 (int): número 1.
        num2 (int): número 2.

    Returns:
        int: Resultado de la división.

    Raises:
        ZeroDivisionError: Si el número 2 es 0.
    """
    try:
        result = num1 / num2
    except ZeroDivisionError:
        result = None
        raise ZeroDivisionError
    else:
        return result
