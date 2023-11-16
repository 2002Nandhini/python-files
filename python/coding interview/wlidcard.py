#to check whether a character is a vowel or consonant
#get user input
'''
Char =  input() 
#Check if the Char belong to set of Vowels
if (Char == 'a' or Char == 'e' or Char == 'i' or Char == 'o' or Char == 'u'): 
    #if true 
    print("Character is Vowel") 
else: 
    #if false
    print("Character is Consonant")'''
#Area of circle
'''
def findArea(r):
    PI = 3.142
    return PI * (r*r);

# Driver method
print('Area is %.6f' % findArea(5));'''


#print even string
'''
def even(string):

    string=string.split(' ')

    for word in string:
        if len(word)%2 == 0:
            print(word)
string=input("enter")
even(string)
'''
#quick sort
'''
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr = quick_sort(arr)
print(sorted_arr)
'''

#bubble sort
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Last i elements are already sorted, no need to compare them again
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap the elements

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)

        
    
