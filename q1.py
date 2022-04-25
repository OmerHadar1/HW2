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
            print(div_num)

        except FileNotFoundError:
            print(-1)

        except ZeroDivisionError:
            print(-2)

        except ValueError or TypeError:
            print(-3)


a = "check_1.txt"
q1(a)