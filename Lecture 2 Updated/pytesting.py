# Test update with comment

def return_multiple():
    """ Returnerar 3 unika variabler av olika typer """
    a = "anka"
    b = 3
    c = []

    return a, b, c


a, _, _ = return_multiple()


def bike(year, model="mc"):
    print(model, year)


def perform_addition(a=5, b=6):
    return a+b


def check_type_varible(variable):
    print(type(variable))


def check_dir(variable):
    print(dir(variable))


def main():
    my_dict = {"key1": 1, "key2": 5}

    for i in range(1, 10):
        # print(i)
        pass

    for key, value in my_dict.items():
        # print(key)
        # print(value)
        pass

    my_list = ["Anton", "Adrian", "Anna"]

    for _, e in enumerate(my_list):
        pass


main()
if __name__ == "__main__":
    main()
