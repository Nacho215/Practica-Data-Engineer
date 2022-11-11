def get_char_counts(string_list):
    # Get a string list and returns a list
    # containing the character count for each string
    char_counts = []
    for string in string_list:
        char_counts.append(len(string))
    return char_counts


def main():
    # Get and show character counts for animals
    animals = ['perro', 'elefante', 'dragón']
    char_counts = get_char_counts(animals)
    print(char_counts)


if __name__ == '__main__':
    main()
