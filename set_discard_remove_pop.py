"""
https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
"""


if __name__ == "__main__":
    input_set_size = int(input())
    input_set = set(map(int, input().split()))

    number_of_commands = int(input())


    for i in range(number_of_commands):
        method, *value = input().split(" ")
        
        # if len(value) > 0:
        #     value = int(*value)

        if method in ("remove", "pop"):
            try:
                getattr(input_set,method)(int(*value)) if len(value) > 0 else getattr(input_set,method)()
                
            except:
                pass
        else:
            getattr(input_set,method)(int(*value)) if len(value) > 0 else getattr(input_set,method)()
    
    
    print(sum(input_set))