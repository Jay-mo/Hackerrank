"""
Perform append, pop, popleft and appendleft methods on an empty deque d

sample input 

6
append 1
append 2
append 3
appendleft 4
pop
popleft

sample output
1 2

"""
from collections import deque
#solution

if __name__ == '__main__':
    number_of_inputs = int(input())

    d = deque()

    for _ in range(number_of_inputs):
        deque_commands = input().split()

        if len(deque_commands) > 1:

            method , *value = deque_commands

            #another way to solve this
            #getattr(d,method)(*value)

            for i in value:

                exec(f'd.{method}({value.pop()})')

        else:
            method = deque_commands[0]
            exec(f'd.{method}()')

        #exec('d.'+ method + '(' + value + ')')

        # print(f'd.{method}({value})')

        

    print(*d)

        