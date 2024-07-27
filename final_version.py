class Data {
    def data_find(jmeno, prijmeni) {
        return //SQL string
    }

    def data_add(jmeno, prijmeni, vek, telefonniCislo) {
        // SQL INSERT INTO
    }

    def data_print()
}

class UzivatelskeRozhrani {
    def init(self):
        data = Data()

    def vypis() {

    }

    def pridani() {
        jmeno = input("Zadej jméno")
        prijmeni = input("Zadej příjmení")

        data_add(jmeno, prijmeni, vek, telefonniCislo)
    }

    def vyhledani() {
        jmeno = input("Zadej jméno k hledání? ")
        příjmení = input("Zadej příjmení k hledání? ")

        print(data.data_find(jmeno, prijmeni))
    }


main.py

rozhrani = UzivatelskeRozhrani()

while volba != 4:
    match:
        case 1:
            rozhrani.pridani()
        case 2:
