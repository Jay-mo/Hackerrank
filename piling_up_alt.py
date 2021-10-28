"""
There is a horizontal row of  cubes. The length of each cube is given. 
You need to create a new vertical pile of cubes. The new pile should follow these directions: if

cube[i] is on top of cube[j], then sideLength[j] >= sideLength[i]

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. 
Print Yes if it is possible to stack the cubes. Otherwise, print No.


Input format

The first line contains a single integer T, the number of test cases.
For each test case, there are 2 lines.
The first line of each test case contains n, the number of cubes.
The second line contains n space separated integers, denoting the sideLengths of each cube in that order.
"""

from collections import deque


if __name__ == '__main__':
    number_of_testCases = int(input())

    

    for i in range(number_of_testCases):
        number_of_cubes = int(input())
        list_of_cubes = deque([ int(i) for i in input().split() ])


        new_list = []

        last_element = max(list_of_cubes)

        while len(list_of_cubes) > 0:

            if list_of_cubes[-1] >= list_of_cubes[0] and list_of_cubes[-1] <= last_element:

                last_element = list_of_cubes.pop()
                print(list_of_cubes)


            elif list_of_cubes[0] > list_of_cubes[-1] and list_of_cubes[0] <= last_element:

                last_element = list_of_cubes.popleft()
                print(list_of_cubes)

                # if len(new_list) > 0 and new_list[-1] < list_of_cubes[-1]:
                # new_list.append(list_of_cubes[0])
                
            else:
                print ('No')
                break
        else:
            print("Yes")