
shopping_list = []
def main():
    while True:
        ans = input('''
what would you like to do with your shopping list?
Enter the corresponding number.
1- Add to the list.
2- Remove from the list.
3- View the list
-4 Quit            
''')
        
        if ans == '1':
            add_item() # calling the add_item() function to add to the list.
        elif ans == '2':
            remove_item() # calling the remove_item() function to remove from the list
        elif ans == '3':
            view_list() # calling the view_list() function to show the shopping list
        elif ans == '4':
            print("Thank you, have a great day!")
            break # breaks out of the funciton
def add_item():
    ans = input("What would you like to add? ")
    shopping_list.append(ans)
def remove_item():
    ans = input("What would you like to remove? ")
    shopping_list.remove(ans)
def view_list():
    print("Here is you shopping list: ")
    print(shopping_list)

main()