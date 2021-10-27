"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given  scores. Store them in a list and find the score of the runner-up.

input 5  
2 3 6 6 5

answer 5


"""




if __name__ == '__main__':
    input_length = int(input())

    input_list = list(map(int, input().split()))

    

    input_list = list(set(input_list))

    input_list.sort()


    print (input_list[-2])



    

