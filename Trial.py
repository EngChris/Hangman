'''
Test
'''
import random
import time
guessed_no =[1,2,3,4,5,6,7,8,9,10,2,4]
n=1

#user_input= input("Please input a value ")



while True:
    select= random.choice(guessed_no)
    print("\033c",end="")
    print("The random number is", select)
    time.sleep(0.01)
    if input()== "":
        break

print("The lucky number is", select)
