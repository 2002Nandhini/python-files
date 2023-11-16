import random
word=["aditya","ajay","nandhini"]
choosen_word=random.choice(word)
print(choosen_word)
'''user_input=input("Enter the word:")
#true or false 
for i in a:
    if i == user_input:
        print("True")
    else:
        print("False")'''
display=[]
for letter in choosen_word:
    display +="_"
print(display)
user_input=input("Enter the word:")
for i in choosen_word:
    if i == user_input:
        display[i]=user_input
    
        
    
    


