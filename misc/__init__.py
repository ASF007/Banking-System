from .config import *
from .decorations import *

import random
from datetime import datetime

import mysql.connector as mys

# connection object
con = mys.connect(host=HOST, user=USER, password=PASSWORD, db=DB_NAME)

# cursor
cur = con.cursor()

# ====================== database functions ======================


def get_records(name, id):
  """Gets records from our table"""

  cur.execute("SELECT * FROM bank WHERE name = '{}' AND id = {}".format(
    name, id))
  res = cur.fetchone()
  if res:
    return res  # will return a tuple like: (123456, 'Aman', 99999.99, 'Gold')
  else:
    return None  # no records were found :P


def make_account(name, amnt, item=None):
  """Makes a new account for the given user"""

  if not already_exists(name):
    if item == "y":
      item = input("Enter the item to store: ")
    else:
      item = None
    id = gen_id()
    q = "INSERT INTO bank VALUES({}, '{}', '{}', '{}')".format(
      id, name, amnt, item)
    cur.execute(q)
    con.commit()

    print("{}, Your account has been created with ID `{}`.".format(name, id))
  else:
    print(
      "\n[Error]: An account with that name already exists! Please login with your another name and ID instead.\n"
    )


def create_table():
  """Creates a table if none exists"""

  q = "CREATE TABLE IF NOT EXISTS bank(id int PRIMARY KEY, name VARCHAR(20), balance decimal(10,2), items VARCHAR(20))"
  cur.execute(q)


# ====================== helper functions ======================


def check_validity(balance, amnt_to_get):
  """
  Function which returns true if the w/d amnt is valid
  else false otherwise
  """
  if amnt_to_get > balance:
    #print("[Error]: You cannot withdraw more amnt then you have brokey.. ")
    return False
  else:
    return True


def show_data(record):
  """Shows the results in a readable manner."""
  _id, name, bal, item = record  # Unpacking our tuple
  to_display = data_ux.format(name.title(), bal, fmt_item(item), _id,
                              datetime.now())
  return to_display


def already_exists(_name, with_id=False, id=None):
  """Checks if an account already exists or not"""

  res = None
  if with_id and id:
    cur.execute("SELECT * FROM bank WHERE name = '{}' AND id = {}".format(
      _name, id))
    res = cur.fetchone()
  else:
    cur.execute("SELECT * FROM bank WHERE name = '{}'".format(_name))
    res = cur.fetchone()

  return res


def gen_id():  # optimized the code a bit and removed the unecessary for loop
  """Returns a random 4 digit unique id."""

  # NOS = ["0", "1", "2", "3"]
  st = ""
  for _ in range(5):
    n = random.randint(0,9)
    st += str(n)
  return int(st)


def fmt_item(_item):
  """Return a beautified string of our item"""

  if _item != "None":
    return _item
  else:
    return "No items stored."


# ============================================


#messin round don mind me - santo
def delete(name, id):
  """Deletes a pre-existing account from our db."""

  if already_exists(name):
    q = "delete from bank where name='{}' and id={}".format(name, id)
    cur.execute(q)
    con.commit()
    print(
      "\n{}, Your account has been deleted successfuly, please approach withdrawal counter to collect your cash and items."
      .format(name))
  else:
    print("\n[Error]: An account with those credentials doesn't exist.")


def deposit(name, id, amount):
  if not already_exists(name, True, id):
    print("\n[Error]: Invalid credentials supplied.\n")
  else:
    q = "update bank set balance=balance+{} where name='{}' and id={}".format(
      amount, name, id)
    cur.execute(q)
    con.commit()
    q = "select balance from bank where name='{}' and id={}".format(name, id)
    cur.execute(q)
    balance = cur.fetchone()[0]
    print(
      "\n{} OMR has been deposited succesfuly, your new balance is {}OMR\n".
      format(amount, float(balance)))


def withdraw(name, id, amount):
  if not already_exists(name, True, id):
    print("\n[Error]: Invalid credentials supplied.\n")
  else:
    q = "select balance from bank where name='{}' and id={}".format(name, id)
    cur.execute(q)
    balance = cur.fetchone()[0]

    if check_validity(balance, amount):
      q = "update bank set balance=balance-{} where name='{}' and id={}".format(
        amount, name, id)
      cur.execute(q)
      con.commit()
      q = "select balance from bank where name='{}' and id={}".format(name, id)
      cur.execute(q)
      balance = cur.fetchone()[0]
      print(
        "\n{} OMR has been withdrawn, please collect your money.\nYour new balance is {} OMR"
        .format(amount, float(balance)))
    else:
      print("\n[Error]: You cannot withdraw more amount than you have. \n")