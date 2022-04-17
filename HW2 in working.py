def q1(input_file_name):
    """
    Read values from input file
    :param input_file_name: An input file name
    :return: The result of the division of the first number by the others
    """
    user_file = open(input_file_name, "r")
    lst_text = user_file.read().split()
    print(lst_text)
    try:
        div_num = float(lst_text[0])
        for i in range(1, len(lst_text)):
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