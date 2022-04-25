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
        output_file.write(str(sorted_lst))
