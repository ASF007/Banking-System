from misc import (
  create_table, 
  make_account, 
  show_data, 
  get_records, 
  ux, delete, 
  deposit, 
  withdraw, 
  purchase
)

create_table()  # creates an table automatically for you on runtime

promt = "y"  # we start with a yes..

while promt.lower(
) == "y":  
  print(ux)
  choice = int(input(">>> Enter your option [1-7]: "))

  if choice == 1:  # displaying record
    name = input("\nEnter your account's name: ")
    id = input("Enter the Unique ID of your account: ")

    records = get_records(
      name.lower(), id)  # we store names as .lower() to avoid duplication
    if records:
      print(show_data(records))
      print()
    else:
      print(
        "\n[Error]: Either you entered wrong info or an account with those credentials doesn't exist!\n"
      )

  elif choice == 2:  # creating record
    name = input("\nEnter the name for your account: ")
    amount = float(input("How much amount would you like to deposit: "))
    item = input(
      "Would you also like to store any item in our secure vault? [y/n]: ")
    make_account(name.lower(), amount, item.lower())
    print()

  elif choice == 3:
    name = input("\nEnter your account's name: ")
    id = input("Enter the Unique ID of your account: ")
    delete(name.lower(), id)

  elif choice == 4:
    name = input("\nEnter your account's name: ")
    id = input("Enter the Unique ID of your account: ")
    item = input("Enter the item to be purchased: ")
    cost = float(input("Enter the cost of the item to be purchased: "))
    purchase(name,id,item,cost)
    print()

  elif choice == 5:
    name = input("\nEnter your account's name: ")
    id = input("Enter the Unique ID of your account: ")
    amount = float(input("Enter the amount to be withdrawn: "))
    deposit(name, id, amount)
    print()

  elif choice == 6:
    name = input("\nEnter your account's name: ")
    id = input("Enter the Unique ID of your account: ")
    amount = float(input("Enter the amount to be withdrawn: "))
    withdraw(name, id, amount)

  elif choice == 7:
    print(
      "\nThanks for banking with National Bank, See you next time!"
    )  
    break

  else:  
    print("\n[Error]: Invalid Option Given! Please select [1-7]\n")

  promt = input("\nDo you wish to proceed? [y/n]: ")
  print()

else:  
  print("\nThanks for banking with National Bank, See you next time!")
