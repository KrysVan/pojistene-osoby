from classes import UzivatelskeRozhrani

rozhrani = UzivatelskeRozhrani()

print("-------------------------\n Evidence Pojištěných\n-------------------------")


def eventLoop():
    action = 0
    while True:
        try:
            action = int(input(
                "Vyberte si akci:\n 1 - Přidat nového pojistného\n 2 - Vypsat všechny pojištěné\n 3 - Vyhledat pojištěného\n 4 - Konec\n"))
        except:
            print('Musite zadat cislo')
            continue
        if action == 1:
            rozhrani.pridani()
            print("\nData byla uložena. Pokračujte klávesou enter...")
        elif action == 2:
            rozhrani.vypis()
            print("\nVšechna data z tabulky byla vypsána. Pokračujte klávesou enter...")
        elif action == 3:
            rozhrani.vyhledani()
            print("\nVšechny řádky, které se shodují s tímto jménem a přímením byly vypsány. Pokračujte klávesou enter...")
        elif action == 4:
            break
        input()

if __name__ == '__main__':
   eventLoop()


