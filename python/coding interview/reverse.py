#Reverse a number
'''def reverse(num):
    reverse_str=str(num)
    re_str=reverse_str[::-1]
    reverse_num=(re_str)
    return(reverse_num)

reverse_num=reverse(12)
print(reverse_num)'''

#Fibinnaci series

'''def fib(num1,num2):
    for i in range(1,num2):
        num3=num1+num2
        num1=num2
        num2=num3
        print(num3)
fib(1,9)'''

#gcd
'''
values = [int(x) for x in input("Enter two integer values separated by a space: ").split()]
value1, value2 = values[0], values[1]
if value1 > value2:
    small=value2
else:
    small=value1
for i in range(1,small+1):
    if(value1 % i == 0) and (value2 % i == 0):
        gcd=format(i)
print(gcd)'''

#perfect Number
'''def perfect_num(num):
    sum=0
    for i in range(1,num):
        if(num % i == 0):
            sum=sum+i
            print(sum)
    return sum
num = 28
Total=perfect_num(num)
if Total == num:
    print("It is a perfect number")
else:
    print("It is not a perfect number")'''

#Anagram Program
'''word=input("Enter")
word1=[input("Enter")
if len(word) != len(word1):
    print("It is not anagram ")
else:
    word_s=sorted(word)
    word_o=sorted(word1)
if(word_s == word_o):
    print("It is anagram")
else:
    print("It is not an anagram")'''

#palindrome
'''
a='ken'
b='ngK'
reverse_str=''

if len(a) != len(b):
    print("not palindrome")
else:
    for i in range(len(a)-1,-1,-1):
        reverse_str += a[i]
    if reverse_str.lower() == b.lower():
        print("palindrome")
    else:
        print("not palindrome")'''
#frequecy of characters

'''string_char = input("Enter the word:")
char= input("Enter the character:")
freq=0
for i in string_char:
    if char == i:
        freq+=1

print(freq)'''

#Non repeating characters
'''
word="Nandhini"
w=word.lower()
for i in w:
    count=0
    for j in w:
        if i == j:
            count+=1
        if count > 1:
            break
    if count == 1:
        print(i)'''
'''
def custom_replace(original_string, old_substring, new_substring):
    # Find the index of the old_substring in the original_string
    index = original_string.find(old_substring)

 # If the old_substring is not found, return the original string as it is
    if index == -1:
        return original_string

    # Replace the old_substring with the new_substring using slicing and concatenation
    replaced_string = original_string[:index] + new_substring + original_string[index + len(old_substring):]

    return replaced_string

# Example usage:
text = "Hello, World! Hello, Universe!"
new_text = custom_replace(text, "Hello", "Hi")
print(new_text)'''

#replace each element in an array by its rank in the array
'''
def changearr(input1):
    new_arr = input1.copy()
    new_arr=sorted(new_arr)

    for i in range(len(input1)):
        for j in range(len(new_arr)):
            if input1[i] == new_arr[j]:
                input1[i]= j+1;
                print(input1[i])
                break

    
Array = [5, 3, 4, 2, 1]
changearr(Array)
print(Array)'''
'''
num = int(input("Enter the Number:"))
temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    print(remainder)
    reverse = (reverse * 10) + remainder
    print(reverse)
    num = num // 10
    print(num)

print("The Given number is {} and Reverse is {}".format(temp, reverse))'''

#wildcard

'''
def solve(a,b):
    n,m=len(a),len(b)
    if n==0 and m==0:
        return True
    if n > 1 and a[0] == '*' and m == 0:
        return False
    if (n > 1 and a[0] == '?') or (n != 0 and m !=0 and a[0] == b[0]):
        return solve(a[1:],b[1:]);
    if n !=0 and a[0] == '*':
        return solve(a[1:],b) or solve(a,b[1:])
    return False

str1="Prepins*a"
str2="Prepinsta"
print("First string with wild characters :" , str1)
print("Second string without wild characters ::" , str2)
print(solve(str1,str2))'''
'''
def rotate_array(arr, K):
    n = len(arr)
    K = K % n  # Effective rotation amount
    rotated_arr = [0] * n
    
    for i in range(n):
        new_position = (i + K) % n
        rotated_arr[new_position] = arr[i]
    
    return rotated_arr

# Example usage
original_array = [1, 2, 3, 4, 5]
rotation_amount = 2
rotated_array = rotate_array(original_array, rotation_amount)
print(rotated_array)  # Output: [4, 5, 1, 2, 3]'''


#factorial
'''n=5
out=1
for i in range(1,n+1):
    out *= i
print(out)'''

# code to Reverse the element of the array
'''def reverseList(A, start, end):
  while start < end:
    A[start], A[end] = A[end], A[start]
    start += 1
    end -= 1
# Driver function to test above function
A = [10, 20, 30, 40, 50]
reverseList(A, 0, 4)
print(A)'''


#Print the smallest element of the array
'''
arr = [10, 89, 9, 56, 4, 80, 8]
mini = arr[0]

for i in range(len(arr)):
  if arr[i] < mini:
     mini = arr[i]

print (mini)'''

#Write a code to Remove all characters from string except alphabets
#take user input
'''
String1 = input('Enter the String :')
#initialize empty String
String2 = ''
for i in String1:
    #check for alphabets
    if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
        #concatenate to empty string
        String2+=i
print('Alphabets in string are :' + String2)'''

#Ascii value
#user input
'''
Char = input('Enter the character :')
#convert Char to Ascii value
Asciival = ord(Char)
#print Value
print(Asciival)'''

#to check whether a character is a vowel or consonant
#get user input
Char =  input() 
#Check if the Char belong to set of Vowels
if (Char == 'a' or Char == 'e' or Char == 'i' or Char == 'o' or Char == 'u'): 
    #if true 
    print("Character is Vowel") 
else: 
    #if false
    print("Character is Consonant")




















                

























































































        












































































                                

                            




                                
                                





























