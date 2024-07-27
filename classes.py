import sqlite3

conn = sqlite3.connect("C:\pojisteni\pojisteni.db")

cur = conn.cursor()



class Data:
    def data_find(self, name, surname):
        items = cur.execute('SELECT * FROM databaze')
        for item in items:
            if item[0] == name and item[1] == surname:
                print(item[0] + "\t " + item[1] + "\t " + item[2] + "\t " + item[3])

    def data_add(self, name, surname, age, phone):
        cur.execute('INSERT INTO "databaze" VALUES(?, ?, ?, ?)', (name, surname, age, phone))
        conn.commit()

    def data_print(self):
        cur.execute('SELECT * FROM databaze')
        items = cur.fetchall()

        print("Jméno     " + "\tPříjmení   " + "\tVěk   " + "\tTelefonní číslo   ")
        print("---------  " + "\t---------  " + "\t--- " + "\t----------------")
        for item in items:
            print(item[0] + "   \t\t" + item[1] + "\t\t " + item[2] + "\t\t " + item[3])

        conn.commit()


class UzivatelskeRozhrani:
    def vypis(self):
        data = Data()
        data.data_print()

    def pridani(self):
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
        data = Data()
        data.data_add(name, surname, age, phone)

    def vyhledani(self):
        name = str(input("Prosím zadejte jméno: "))
        while name == "":
            print("Nezadali jste jméno!")
            name = str(input("Prosím zadejte jméno: "))
        surname = str(input("Prosím zadejte příjmení: "))
        while surname == "":
            print("Nezadali jste příjmení!")
            surname = str(input("Prosím zadejte příjmení: "))
        data = Data()
        data.data_find(name, surname)
