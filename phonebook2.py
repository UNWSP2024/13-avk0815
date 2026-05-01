import sqlite3

def connect():
    return sqlite3.connect("phonebook.db")

def add():
    name = input("Name: ")
    phone = input("Phone: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO Entries VALUES (?, ?)", (name, phone))
    conn.commit()
    conn.close()

def view():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM Entries")
    for row in cur.fetchall():
        print(row)

    conn.close()

def update():
    name = input("Name to update: ")
    phone = input("New phone: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE Entries SET Phone=? WHERE Name=?", (phone, name))
    conn.commit()
    conn.close()

def delete():
    name = input("Name to delete: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM Entries WHERE Name=?", (name,))
    conn.commit()
    conn.close()

while True:
    print("\n1 Add  2 View  3 Update  4 Delete  5 Exit")
    choice = input("Choice: ")

    if choice == "1":
        add()
    elif choice == "2":
        view()
    elif choice == "3":
        update()
    elif choice == "4":
        delete()
    elif choice == "5":
        break