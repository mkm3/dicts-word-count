
def find_word_count(path):

    '''Finding the numbers of occurences for each word in file'''
    

    the_file = open(path)
    # assigning variable to our open function, passing through produce report (path)

    word_count = {}

    for line in the_file:
    # iterating through each line of the produce report

        line = line.rstrip()
        #removes the whitespace to the right of the string

        line = line.split(' ')

        # line = line.lower()
        #item is created by split string when "|" is located in line

    # for idx, key in enumerate(the_file):
    #     the_file[key] = occurence

        for word in line:

            word = word.lower() 

            word_count[word] = word_count.get(word, 0) + 1





    return word_count



    the_file.close()


print(find_word_count("test.txt"))
