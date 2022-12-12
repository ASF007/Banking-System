from misc import create_table, make_account, show_data, get_records, ux, delete, deposit, withdraw, fmt_item

create_table()  # creates an table automatically for you on runtime

promt = "y"  # we start with a yes..

while promt.lower(
) == "y":  # the user now gets thrown in our loop until he yeets it :P
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
    print("🚧 National Bank E store is work in progress, come again later 🚧")

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
    )  # the user has lost all sanity and has decided to break free of our loop 💀
    break

  else:  # after being in our loop, the user is loosing sanity
    print("\n[Error]: Invalid Option Given! Please select [1-7]\n")

  promt = input("\nDo you wish to proceed? [y/n]: ")
  print()

else:  # the user got tired of our infinite loop and decided to YEET it
  print("\nThanks for banking with National Bank, See you next time!")