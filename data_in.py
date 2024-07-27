import sqlite3

conn = sqlite3.connect("C:\pojisteni\pojisteni.db")

cur = conn.cursor()

class Data_entry():
        def data_entry(name, surname, age, phone):
                cur.execute('INSERT INTO "databaze" VALUES(?, ?, ?, ?)', (name, surname, age, phone))
                conn.commit()

        name = str(input("Prosím zadejte jméno: "))
        while name == "":
                print("Nezadali jste jméno!")
                name = str(input("Prosím zadejte jméno: "))
        surname = str(input("Prosím zadejte příjmení: "))
        while surname == "":
                print("Nezadali jste příjmení!")
                surname = str(input("Prosím zadejte příjmení: "))
        age = str(input("Prosím zadejte věk: "))
        while age == "":
                print("Nezadali jste věk!")
                age = str(input("Prosím zadejte věk: "))
        phone = str(input("Prosím zadejte telefonní číslo: "))
        while phone == "":
                print("Nezadali jste telefonní číslo!")
                phone = str(input("Prosím zadejte telefonní číslo: "))

        data_entry(name, surname, age, phone)


cur.close()