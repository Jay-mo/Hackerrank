
from collections import OrderedDict

if __name__ == '__main__':
    num_of_items = int(input())
    items = OrderedDict()

    for i in range(num_of_items):
        food_item, net_price = input().rsplit(None, 1)
        
        if food_item not in items:
            items[food_item] = [ int(net_price) , 1 ]
            
        else:   
            items[food_item] = [ int(net_price) , items.get(food_item)[1] + 1 ]

    for item, data in items.items():
        print( item, data[0] * data[1])