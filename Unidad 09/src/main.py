
def get_int_input(message: str) -> int:
    """
    Print a given message, get the user input (integer) and returns it.

    Args:
        message (str): Message prompting the user to enter an integer.

    Returns:
        int: User input.

    Raises:
        ValueError: If user input is not an integer.
        KeyboardInterrupt: If user abort input by pressing Ctrl+C.
    """
    print(message)
    return int(input())


def get_value_from_list(str_list: list, index: int) -> str:
    """
    Get the value corresponding to a given index in a given string list,
    and returns it.

    Args:
        str_list (list): A list of strings.
        index (int): The index of the value to find.

    Returns:
        str: The value found.

    Raises:
        AssertionError: If given index is not positive.
        IndexError: If given index is out of list bounds.
    """
    assert index >= 0
    value = str_list[index]
    return value


def main():
    # List of strings used
    example_list = ['auto', 'avión', 'barco', 'bicicleta', 'ómnibus']
    # Ask user for an index to find an element in the list
    # This process will be looping until the user enters a valid index
    # or abort the program with Ctrl+C
    while True:
        try:
            input = get_int_input(
                "Please enter an index to find an element in the list:"
                )
        except ValueError:
            print("That's not a number.")
        except KeyboardInterrupt:
            print("Program aborted by the user.")
            break
        else:
            try:
                value = get_value_from_list(example_list, input)
            except AssertionError:
                print("That's not a positive number.")
            except IndexError:
                print("Index out of bounds.")
            else:
                print(f"The value in the list for that index is: {str(value)}")
                break


if __name__ == '__main__':
    main()
