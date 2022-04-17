def q1(input_file_name):
    """
    Read values from input file
    :param input_file_name: An input file name
    :return: The result of the division of the first number by the others
    """
    user_file = open(input_file_name, "r")
    lst_text = user_file.read().split()  # List of al the numbers in the file
    try:  # A "try" block for dealing with exceptions like "FileNotFoundError", "ZeroDivisionError", "ValueError", and
        # "TypeError.
        div_num = float(lst_text[0])  # A variable of the first number in th string
        for i in range(1, len(lst_text)):  # That "for" loop divides al the numbers in the file
            div_num = div_num / float(lst_text[i])
        print(div_num)

    except FileNotFoundError:
        print(-1)

    except ZeroDivisionError:
        print(-2)

    except ValueError or TypeError:
        print(-3)


def q2(input_file_name):
    """
      a. Read words from input file
      b. Classify the words by length
      c. Write each word and its length to output file.
    """


def q3_a(n: int):
    """
    :param n: An integer number
    :return: All prime numbers up to n
    """


def q3_b(n: int):
    """
    uses the function q3_a
    :param n: An integer number
    :return: A list that contains all the three prime numbers combinations whose product is less than or equal to n.
    """


def q4(n: int):
    """
    :param n: A positive number
    :return: The n-th line in the Pascal triangle
    """


def q5_a(z, a, b, n):
    """
     The function returns the approximation of the root of 𝑧(𝑥) (𝑧(𝑥)=0) according to the bisection method.
    """


def q5_b(f, g, a, b, n):
    """
    The function returns the approximation of a solution 𝑓(𝑥)=𝑔(𝑥) (using the bisection method)
    """


# ########### TESTING FUNCTIONS, DO NOT CHANGE THESE FUNCTIONS ################


def f(x):
    return 3 * x + 9


def g(x):
    return x ** 2 - 5

# ###############################################################################
