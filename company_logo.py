"""
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. 
They are now trying out various combinations of company names and logos based on this condition. Given a string S, which is the company name in lowercase letters, 
your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,


Sample Input

aabbbccde


b 3
a 2
c 2

"""

from operator import itemgetter
from collections import Counter, OrderedDict

if __name__ == "__main__":
    company_name = input()


    #use counter to get dictionary of the all the elements in the strings and their count as values
    name_dict = Counter(list(company_name))

    #because sorted keeps the original order of sorted items when the sorted keys are the same, I have to sort the keys firsts in ascending order.
    s = sorted(name_dict.items(), key=itemgetter(0))


    #using sorted and passing itemgetter to get sort based on the values. Reverse flag set to sort in descending order
    sorted_name_tuple = sorted(s, key=itemgetter(1), reverse=True)

    #use ordered dict so that the order is maintained.
    sorted_name_dict = OrderedDict({ k:v for k, v in sorted_name_tuple})

    
    #print only the first 3 items 
    for i in list(sorted_name_dict.keys())[:3]:
        print( i , sorted_name_dict[i])

