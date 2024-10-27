# write a python program to count the frequecy of words in a sentence
def freq_words():
    str = input("Enter a string: ")

    li = str.split()
    dict = {}

    for i in  li:
        if i not in dict.keys():
            dict[i]=0
        dict[i]=dict[i]+1
    print(dict)    

freq_words()    

  