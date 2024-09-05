'''
Handling files
'''
import random 
#print (f)


def read_file(file_name):
    f = open("words.txt", "rt")
    data = f.read()
    print(data)
    word = data.split("\n")
    print(word)
    for x in word:
           
    #print(x.strip('\n'), end=" ")
    #word = x.split("\n")
        print(x)
        f.close()
    

def read_random(file_name):
    f = open("words.txt", "rt")
    word2= f.readlines()
    print(word2)
    f.close()
    
file = "words.txt"
read_file(file)