def swap(lis, a, b):
    temp = lis[a]
    lis[a] = lis[b]
    lis[b] = temp

def min_index(list1, starting_index):
    min_index = starting_index
    min_val = list1[starting_index]
    
    for i in range(starting_index, len(list1)):
        if min_val > list1[i]:
            min_val = list1[i]
            min_index = i
            
    return min_index


def sort(my_list):
    for i in range(len(my_list)):
        min_i = min_index(my_list, i)
        swap(my_list, min_i, i)
        
    return my_list
        

unsorted_list = [5, -1, 0, 10 ,20 ,5]
print(sort(unsorted_list.copy()))
print(unsorted_list)
        

