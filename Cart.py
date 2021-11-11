# 1

def Questions():
    print("""
Enter 'Add' to add an item to your cart.
Enter 'View' to view all items in your cart.
Enter 'Remove' to Remove an item from your cart.
Enter 'Quit' to end program. \n""")
    print()


def cart():
    print("\nWelcome to your cart:")

    cart = []
    done = False

    while not done:
        Questions()
        print("What would you like to do?")
        prompt = input("Add | View | Remove | Quit ")
        if prompt.lower() == 'add':
            new_item = input("\nEnter the item you wish to add to cart: ")
            cart.append(new_item.title())
            input("\nItem added to cart. Press return to continue: ")
        elif prompt.lower() == 'view':
            print("\nHere is what currently is in your cart:")
            for item in cart:
                print(item)
            input('\nPress return to continue: ')
        elif prompt.lower() == 'remove':
            deleted_item = input(
                '\nEnter the item you want to have removed: ')
            cart.remove(deleted_item.title())
            input('\nItem removed from cart. Press return to continue: ')
        elif prompt.lower() == 'quit':
            print("\nThank you come again.")
            break
        else:
            input("\nInvalid. Press return to continue: ")


cart()


print()




