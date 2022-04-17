def q1(input_file_name):
    """
    Read values from input file
    :param input_file_name: An input file name
    :return: The result of the division of the first number by the others
    """
    with open(input_file_name, 'r') as user_file:
        lst_text = user_file.read().split()  # List of al the numbers in the file
        try:  # A "try" block for dealing with exceptions like "FileNotFoundError", "ZeroDivisionError", "ValueError", and
            # "TypeError.
            div_num = float(lst_text[0])  # A variable of the first number in th string
            for i in range(1, len(lst_text)):  # That "for" loop divides al the numbers in the file
                div_num = div_num / float(lst_text[i])
            return div_num

        except FileNotFoundError:
            return -1

        except ZeroDivisionError:
            return -2

        except ValueError or TypeError:
            return -3


def q2(input_file_name):
    """
      a. Read words from input file
      b. Classify the words by length
      c. Write each word and its length to output file.
    """

    with open(input_file_name, "r") as input_file:
    word_lst = input_file.read().split()  # List of the words in the file
    sorted_lst = []
    while len(word_lst) != 0:
        shortest_word = min(word_lst, key=len)
        word_added = (shortest_word, len(shortest_word))
        sorted_lst.append(word_added)
        word_lst.remove(shortest_word)

    with open("output_" + input_file_name, "w") as output_file:
        for item in sorted_lst:
            output_file.write(str(item) + ", ")

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
