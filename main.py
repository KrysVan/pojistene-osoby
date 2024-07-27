
from classes import UzivatelskeRozhrani

rozhrani = UzivatelskeRozhrani()

print("-------------------------\n Evidence Pojištěných\n-------------------------")
action = 0


while action !=4:
    action = int(input("Vyberte si akci:\n 1 - Přidat nového pojistného\n 2 - Vypsat všechny pojištěné\n 3 - Vyhledat pojištěného\n 4 - Konec\n"))
    if action == 1:
        rozhrani.pridani()
        print("\nData byla uložena. Pokračujte klávesou enter...")
        input()
    elif action == 2:
        rozhrani.vypis()
        print("\nVšechna data z tabulky byla vypsána. Pokračujte klávesou enter...")
        input()
    elif action == 3:
        rozhrani.vyhledani()
        print("\nVšechny řádky, které se shodují s tímto jménem a přímením byly vypsány. Pokračujte klávesou enter...")
        input()




