'''
Handling files
'''
import random 
#print (f)


def read_file(file_name):
    f = open("words.txt", "rt")
    data = f.read()
    print(data)
    word=[]
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
    
    
def print_random(file_name):
    f= open(file_name)
    data= f.read()
    word = data.split("\n")
    rand= random.choice(word)
    print(rand)
    
file = "words.txt"
read_file(file)
#read_random(file)
#print_random(file)