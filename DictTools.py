
def print_dictionary(dictionary: dict):
    for key, values in dictionary.items():
        if key is values:
            print()
        else:
            print(key, end=", ")
