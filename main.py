from transaction import Transaction

trnsct_123 = Transaction()

while True:
    print('''\nWelcome!
    Please select the menu.
    1. Add item to cart
    2. Check order
    3. Update item name in cart
    4. Update item price in cart
    5. Update item quantity in cart
    6. Delete an item in cart
    7. Delete all items.
    8. Check out order
    9. Quit program
    ''')

    user_input = input("chosen menu: ")
    if user_input == "1":
        item_name = input("item name: ")
        item_price = input("item price: ")
        item_qty = input("item quantity: ")
        trnsct_123.add_item(item_name, item_qty, item_price)

    elif user_input == "2":
        trnsct_123.check_order()

    elif user_input in ["3", "4", "5"]:
        item_name_update = input("item name to be updated: ")
        if trnsct_123.search_name(item_name_update): 
            if user_input == "3":
                new_name = input("new name: ")
                trnsct_123.update_name(item_name_update, new_name)
            elif user_input == "4":
                new_price = input("new price: ")
                trnsct_123.update_price(item_name_update, new_price)
            else:
                new_qty = input("new quantity: ")
                trnsct_123.update_qty(item_name_update, new_qty)
        else:
            print(f'{item_name_update} is not found in cart.')

    elif user_input == "6":
        item_name_delete = input("item name to be deleted: ")
        if trnsct_123.search_name(item_name_delete):
            trnsct_123.delete_item(item_name_delete)
        else:
            print(f'{item_name_delete} is not found in cart.')

    elif user_input == "7":
        trnsct_123.reset_transaction()

    elif user_input == "8":
        trnsct_123.check_out()
        
    elif user_input == "9":
        print("Thank you for shopping here.")
        print("Clossing the program ...")
        break
    
    else:
        print("Selected menu is not available. Please reinput available menu.")
