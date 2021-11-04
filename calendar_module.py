"""
You are given a date. Your task is to find what the day is on that date.

input 

08 05 2015

output

WEDNESDAY)

"""

from  calendar import day_name , weekday


if __name__ == "__main__":
    input_month , input_day, intput_year = list(map(int, input().split()))

    day_int = weekday(year=intput_year,day=input_day, month=input_month)

    day = day_name[day_int]

    print( day.upper())


    