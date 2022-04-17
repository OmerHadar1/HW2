def q2(input_file_name):
    """
      a. Read words from input file
      b. Classify the words by length
      c. Write each word and its length to output file.
    """

    input_file = open(input_file_name, "r")
    word_lst = input_file.read().split()  # List of the words in the file
    longest_len = len(max(word_lst, key=len))
    len_word = 1  # A variable of
    sorted_lst = []
    while True:
        for i in range(len(word_lst) + 1):
            if i == len(word_lst):
                len_word = len_word + 1
            elif len(word_lst[i]) == len_word:
                output_word = (word_lst[i], len_word)
                sorted_lst.append(output_word)
            elif len_word > longest_len:
                input_file.close()
                return False
    output_address = "output_" + input_file_name
    output_file = open(output_address, "w")
    output_file.write("".join(sorted_lst))
    output_file.close()


a = "check_1.txt"
q2(a)
f = open("output_check_1.text", "r")
print(f.read())