"""
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
"""


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def is_odd(number):
    if number % 2 != 0:
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        n = int(input("Kindly enter an interger: \n => ").strip())

        if is_odd(n):
            print("Weird")

        elif is_even(n):
            if n in range(2,6):
                print("Not Weird")

            elif n in range(6,21):
                print("Weird")
            elif n > 20:
                print("Not Weird")
    except ValueError as err:
        user_Input = err.args[0].split(":")[1]

        print(f'{user_Input} is not a valid interger')

        print("Kindly enter a valid integer")

    except:
        print("There was an error or none of the conditions were met")
        print("Good bye")


    


    