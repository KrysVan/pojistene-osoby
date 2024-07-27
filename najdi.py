import sqlite3

conn = sqlite3.connect("C:\pojisteni\pojisteni.db")

cur = conn.cursor()

class Najdi():
    name = str(input("Prosím zadejte jméno: "))
    while name == "":
        print("Nezadali jste jméno!")
        name = str(input("Prosím zadejte jméno: "))
    surname = str(input("Prosím zadejte příjmení: "))
    while surname == "":
        print("Nezadali jste příjmení!")
        surname = str(input("Prosím zadejte příjmení: "))

    def data_find(name, surname):
        cur.execute('SELECT * FROM databaze')
        items = cur.fetchall()
        for item in items:
            if item[0] == name and item [1] == surname:
                   print(item[0] + "\t " + item[1] + "\t " + item[2] + "\t " + item[3])

    data_find(name, surname)
    conn.commit()