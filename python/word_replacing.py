
import random
import stages
import words
print (stages.logo)

stages=stages.stages

length=6
choosen_word=random.choice(words.word_list)
print(f'The chosen word is {choosen_word}')


display = []
count=len(choosen_word)
for letter in range(count):
    display += '_'
print(display)


end = False
while end == False:
    guess = input("Enter the word you guess:")
   
    for position in range(count):
        letter = choosen_word[position]
        if guess == letter:
            display[position] = guess
            print(display)

    if '_' not in display:
        print("You Win")
        end = True
        
    if guess not in choosen_word:
        length -= 1
        if length == 0:
            end = True
            print("You lose.")
            
    print(stages[length])

        



        
        
