

def menu():
    print("0) Exit")
    print("1) Add")
    print("2) Delete")
    print("3) Show")
    print("4) PrintAll")
    selection = int(input("Your selection: "))
    
    return selection

def add_list(my_list, val):
    my_list.append(val)
    return my_list

def delete_list(my_list, index):
    if index < len(my_list) and index > -1:
        my_list.pop(index)
    else:
        print("!!! Please enter a valid index !!!\n")
        
    return my_list

def show_list(my_list, index):
    if index < len(my_list) and index > -1:
        print("The value on the index:")
        print(my_list[index] + "\n")
    else:
        print("!!! Please enter a valid index !!!\n")
        
def print_list(my_list):
    print("The list:")
    print(my_list + "\n")
        
if __name__ == "__main__":
    sel = 1
    list1 = []
    
    print("Welcome to my program")
    
    while sel != 0:
        selection = menu()
        if selection == 0:
            print("Good Bye")
            break
        
        elif selection == 1:
            value = input("Please enter the value you want to add: ")
            if value.isdigit():
                list1 = add_list(list1.copy(), int(value))
            else:
                print("!!! This list only accepts integers !!!\n")
        
        elif selection == 2:
            index = input("Please enter the index you want to delete: ")
            if index.isdigit():
                list1 = delete_list(list1.copy(), int(index))
            else:
                print("!!! Please enter an integer as index !!!\n")
                
        elif selection == 3:
            index = input("Please enter the index you want to see: ")
            if index.isdigit():
                show_list(list1.copy(), int(index))
            else:
                print("!!! Please enter an integer as index !!!\n")
                
        elif selection == 4:
            print_list(list1.copy())
        else:
            print("!!! You entered unknown operation !!!\n")
            