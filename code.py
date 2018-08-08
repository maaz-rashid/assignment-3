# Q no 1 : you have some strings in variable text your task is to make a list of capital letters only using list comprehension and print that list
# Hint! explore isUpper() method then do this

text = "THis Is Some TeXT"
caps = [letter for letter in text if letter.isupper()]
print(caps)

# Q no 2: Make a list of numbers from 0 to 20 which is divisible by 2 using list comprehension
even_numbers = [num for num in range(21) if num%2==0]
print(even_numbers)

# Q no 3 : Find all of the numbers from 1-1000 that are divisible by 7 by making a list using list comprehension and print it

divisible_by_seven = [num for num in range(1001) if num%7==0]
print(divisible_by_seven)

#Q no 4 : Count the number of spaces in a string below using list comprehension and print the result

text = "This is some dummy text"
no_of_spaces = len([letter for letter in text if letter==" "])
print(no_of_spaces)

#Q no 5 : Write a script that draws a triangle as below:
for a in range(1,13):
    print("*"*a)

# Q no 6 : Write a script that draws a geometric shape as below:
for i in range(1, 14):
    print("*" * (min(i, 7) - max(0, i-7)))

# Q no 7 :Find all of the words in a string that are less than 4 letters using list comprehension
words = "This is some random text to chk for less than 4 letters words.".split()
words_less_than_four = [word for word in words if len(word) < 4]
print(words_less_than_four)
