"""
Basically, namedtuples are easy to create, lightweight object types.
They turn tuples into convenient containers for simple tasks.
With namedtuples, you don’t have to use integer indices for accessing members of a tuple.


Dr. John Wesley has a spreadsheet containing a list of student's IDs , marks , class  and name.

Your task is to help Dr. Wesley calculate the average marks of the students.


sample input

5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   


sample input

5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5

"""


from collections import namedtuple

if __name__ == "__main__":
    number_of_students = int(input())
    col_1, col_2, col_3, col_4 = input().split()
    Student = namedtuple('Student', f'{col_1} {col_2} {col_3} {col_4} ')

    total_marks = 0

    for i in range(number_of_students):

        value_1, value_2, value_3, value_4 = input().split()

        student = Student(value_1,value_2,value_3,value_4)

        total_marks += int(student.MARKS)


    average = total_marks / number_of_students

    print(f'{average:.2f}')
        
        