"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.


Your task is to determine the winner of the game and their score.

Function Description

Complete the minion_game in the editor below.

minion_game has the following parameters:

string string: the string to analyze
Prints

string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
Input Format

A single line of input containing the string .

Sample Input

BANANA
Sample Output

Stuart 12
"""

# from collections import Counter
# s = "BANANA"

# strings = [ s[i:j] for i in range(0,len(s)) for j in range(i+1, len(s) + 1) ]
# data = Counter(strings)
# Kevin = 0
# Steve = 0

# vowels = ('A','E','I','O','U')

# for word, value in data.items():

#     if word[0] in vowels:
#         Kevin += value
#     else:
#         Steve += value
    

# if Kevin > Steve:
#     print (f'Kevin {Kevin}')
# else:
#      print (f'Stuart {Steve}')



# from collections import Counter
# s = "BANANA"
# vowels = ('A','E','I','O','U')
# strings = [ s[i:j] for i in range(0,len(s)) for j in range(i+1, len(s) + 1) if s[i:j][0] in vowels]

# num_of_subtrings = ((len(s) + 1) * len(s)) / 2
# number_of_vowels = len(strings)
# number_of_consonants = num_of_subtrings - number_of_vowels
  

# if number_of_consonants > number_of_vowels:
#     print (f' Stuart {number_of_consonants:.0f}')
# else:
#      print (f' Kevin {number_of_vowels:.0f}')


def number_of_subtrings(string_length):
    numb_of_subtrings = ((string_length * (string_length + 1)) / 2)

    return numb_of_subtrings

def minion_game(string):
    # your code goes here

    vowels = ('A','E','I','O','U')

    vowels_substrings = 0
    consonant_substrings = 0

    total_substrings = number_of_subtrings(len(string))

    for i in range(len(string)):
        if string[i] in vowels:
            substring_length = len(string) - i

            vowels_substrings += substring_length



    consonant_substrings = total_substrings - vowels_substrings


    if consonant_substrings > vowels_substrings:
        print (f' Stuart {consonant_substrings:.0f}')
    elif consonant_substrings == vowels_substrings:
        print("Draw")
    else:
         print (f' Kevin {vowels_substrings:.0f}')


    





