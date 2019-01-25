import sqlite3
import sys

def printArg():
  print(sys.argv[1])

loot_bag_db = '/Users/alfonsomiranda/workspace/python/exercises/bag_O_Loot/loot_bag.db'

def getToys():
  with sqlite3.connect(loot_bag_db) as conn:
    cursor = conn.cursor()

  for row in cursor.execute('SELECT * FROM Toy_Sac'):
    print(row)


def getKids():
  with sqlite3.connect(loot_bag_db) as conn:
    cursor = conn.cursor()

  for row in cursor.execute('SELECT * FROM Kids'):
    print(row)

    # Another way
  cursor.execute('SELECT * FROM Kids')
  toys = cursor.fetchall()
  print(toys)


def getKid(KidName):
  # print(KidName)
  # print(Kid['name'])
  # kidName = Kid['name']

  with sqlite3.connect(loot_bag_db) as conn:
    cursor = conn.cursor()

  cursor.execute(f'''SELECT k.*
                    FROM Kids k
                    WHERE k.Name = '{KidName}'
                    ''')

  CurrentKidObj = cursor.fetchone()
  if CurrentKidObj:
    print("This is the Kid: ", CurrentKidObj[0])
  else:
    print("This Kid was not found")
  return CurrentKidObj[0]


def getToy(ToyName):
  # print(ToyName)

  with sqlite3.connect(loot_bag_db) as conn:
    cursor = conn.cursor()

  cursor.execute(f'''SELECT ts.*
                    FROM Toy_Sac ts
                    WHERE ts.ToyName = '{ToyName}'
                    ''')

  CurrentToyObj = cursor.fetchone()
  if CurrentToyObj:
    print("This is the Toy: ", CurrentToyObj[2])
  else:
    print("This Toy was not found")

  toyId = CurrentToyObj[2]
  return toyId



def __addKid(kid):
  with sqlite3.connect(loot_bag_db) as conn:
    cursor = conn.cursor()

    try:
      cursor.execute(
        '''
        INSERT INTO Kids
        Values(?,?,?)
        ''', (None, kid["name"], kid["gender"])

      )
    except sqlite3.OperationalError as err:
      print("oops", err)


def __deleteToy(ToyName, KidName):
  with sqlite3.connect(loot_bag_db) as conn:
    cursor = conn.cursor()

    # kidId = getToy(ToyName)
    kidId = getKid(KidName)
    # kidId = getKid(KidName)


    print(kidId)
    print(ToyName)


    try:
      cursor.execute(
        f'''
        DELETE FROM Toy_Sac
        WHERE Toy_Sac.kidid = {kidId}
        AND Toy_Sac.ToyName = "{ToyName}"
        '''

      )
    except sqlite3.OperationalError as err:
      print("oops", err)


def cLine(user_input, Toy):
  # print(user_input.values())
  # print(user_input['command'], Toy)
  toyName = Toy['toyName']
  KidName = Toy['kidName']
  # print(KidName)
  # selectedKid = getKid(KidName)

  if user_input['command'] == 'add':
    if getKid(KidName):
      # print("Woopy")
      print("It went through normally")
      __addToy(Toy)

    else:
      newToy = Toy['toyName']
      newKid = Toy['kidName']
      newKidObj = {'name': Toy['kidName'], 'gender': 'M'}
      __addKid(newKidObj)
      __addToy(Toy)
      print(f"New Kid {newKid} and {newToy} were added to the Database!")


  elif user_input['command'] == 'Toy':
    getToy(toyName)


  elif user_input['command'] == 'Delete':
    __deleteToy(toyName, KidName)




  else:
    print("You must enter a valid command like 'add'")


def __addToy(Toy):
  with sqlite3.connect(loot_bag_db) as conn:
    cursor = conn.cursor()

    try:

      # print(Toy)
      name_of_kid = Toy["kidName"]
      # print(name_of_kid)

      cursor.execute(
        f'''
       INSERT INTO Toy_Sac
       SELECT ?,?,k.kidid,?
       FROM Kids k
       WHERE k.name = "{name_of_kid}"
        ''', (None, Toy["toyName"], 0)

      )

    except sqlite3.OperationalError as err:
      print("oops", err)



if __name__ == "__main__":
  # print(sys.argv)


# this adds what is written in the command line after python loot_bag.py "name" "gender"
  # addKid({
  #   "name": sys.argv[1],
  #   "gender": sys.argv[2]
  # })


  try:
    cLine(
      {"command": sys.argv[1]},

    {"toyName": sys.argv[2],
      "kidName": sys.argv[3]}
      )

  except IndexError:
    print('You need to add a damn Toy and a Kid, you chicken monkey!')



# to hard code it
  #  addKid({
  #   "name": "Jimmy",
  #   "gender": "M"
  # })

