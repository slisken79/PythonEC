import random
# from pytest2 import get_random_number, a
import pytest2
import testdir
random.seed(1337)


def sum_variable_plus_one(x=5):
    """ Denna funktion summerar x med sina 3 efterföljande values"""
    increment_by_one_x_times = 4
    sum = 0
    for i in range(increment_by_one_x_times):
        sum = sum + x + i
        print(sum)
    return sum


def teach_if(x, y=7):
    if x == 5:
        print("X is 5")
    elif x == 10:
        print("X is 10")
    elif x == 6 and y == 7:
        print("X is 6 and y is 7")
    else:
        print(f"X is apparently: {x}")

    if x == 15:
        print("X is 15")
    elif x == 5:
        print("X is five AGAIN!!")


def teach_while_and_for_loop() -> int:
    """This function teaches while and forloops"""
    # Our job is to summarize 10 random numbers using both forloop and whileloop
    randomize_x_numbers = 10
    my_numbers = []
    my_numbers2 = []

    for _ in range(randomize_x_numbers):
        my_number = random.randint(a=0, b=20)
        my_numbers.append(my_number)

    print(my_numbers)
    print(sum(my_numbers))

    x = 0
    while x < 10:
        my_number = random.randint(a=0, b=20)
        my_numbers2.append(my_number)
        if x == 5:
            break  # You can also use continue! It works a bit different tho
        x += 1

    print(my_numbers2)
    print(sum(my_numbers2))


def main():
    # sum_variable_plus_one(x=5)
    # teach_if(x=5)
    # teach_while_and_for_loop()
    print(pytest2.get_random_number())
    print(pytest2.a)


if __name__ == "__main__":
    main()
