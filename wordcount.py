# put your code here.

def count_words(path):
   
    text_file = open(path)
    word_count_dict = {}
    words = []

    for line in text_file:
        line = line.rstrip()
        words.extend(line.split(" "))

    for word in words:
        word_count_dict[word] = word_count_dict.get(word, 0) + 1

    # for word, word_count in word_count_dict.iteritems():
    #     print "%s %d" % (word, word_count)
    
    text_file.close()

    return word_count_dict





 #create empty dictionary
 #split line into separate words 
 #loop through each word, check to see if word is in dictionary
# if no, add as a key and add , if yes add 1
count_words("twain.txt")

