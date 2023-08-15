def fizz_buzz(number :int)-> str:
    """
    Returns a string (fizz, buzz, fizzbuzz) or a number provided in parameter in string format.
    :param int number:
    :return string:
    """

    if number % 3 == 0:
        return "fizz"

    elif number % 5 == 0:
        return "buzz"

    elif number % 3 == 0 and number % 5 == 0:
        return "fizz buzz"

    else:
        return str(number)





