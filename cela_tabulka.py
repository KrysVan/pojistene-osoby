import sqlite3

conn = sqlite3.connect("C:\pojisteni\pojisteni.db")

cur = conn.cursor()
class Vypis():
    def vypis(self):
        cur.execute('SELECT * FROM databaze')
        items = cur.fetchall()

        print("Jméno     " + "\t\tPříjmení   " + "\tVěk   " + "\tTelefonní číslo   ")
        print("---------  " + "\t---------  " + "\t--- " + "\t----------------")
        for item in items:
            print(item[0] + "   \t\t" + item[1] + "\t\t " + item[2] + "\t\t " + item[3])

        conn.commit()
        cur.close()
