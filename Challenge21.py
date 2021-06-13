import sqlite3

def id_creator():
    cursor.execute("SELECT Members.UserID FROM Members")
    count = 1
    prev = 0
    for x in cursor.fetchall():
        current = x[0]
        if current - prev != 1:
            count = prev + 1
            break
        count += 1
        prev = current
    db.commit()
    print(count)
    return count
    
def add():
    userid = id_creator()
    name = input("Enter name: ")
    while True:
        try:
            phone = int(input("Enter phone number: "))
            break
        except ValueError:
            print("This is not a valid phone number")
    email = input("Enter email: ")
    postcode = input("Enter postcode: ")
    details = [userid, name, phone, email, postcode]
    for i in range(len(fields)):
        print(fields[i] + ": " + str(details[i]))
    while True:
        print("Are the correct (y/n)")
        user = input(">")
        user = user.lower()
        if user == "y":
            cursor.execute("""INSERT INTO Members(UserID, Name, Phone, Email, Postcode) VALUES(?, ?, ?, ?, ?)""", (userid, name, phone, email, postcode))
            db.commit()
            break
        elif user == "n":
            add()
        else:
            print("You did not enter y or n")

def search():
    name = input("Enter the name you would like to serch for: ")
    cursor.execute("""SELECT * FROM Members WHERE Name LIKE ?""", ["%" + name + "%"])
    x = cursor.fetchall()
    if len(x) > 0:
        for i in range(len(x)):
            y = x[i]
            for j in range(len(y)):
                field = fields[j]
                msg = field + ": " + str(y[j])
                print(msg)
            print("")
    else:
        print("None found")
    
fields = ["UserID", "Name", "Phone", "Email", "Postcode"]
db = sqlite3.connect("Members.db")
cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Members(
UserID integer PRIMARY KEY,
Name text NOT NULL,
Phone integer NOT NULL,
Email text NOT NULL,
Postcode text NOT NULL);""")

while __name__ == "__main__":
    print("""1. Add member
2. Search for members
3. Quit""")
    
    try:
        num = int(input(">"))
    except ValueError:
        num = 4
        
    if num == 1:
        add()
    elif num == 2:
        search()
    elif num == 3:
        break
    else:
        print("You did not enter a valid input.")

db.close()
