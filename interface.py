from data_in import Data_entry
from cela_tabulka import Vypis
from najdi import Najdi

print("-------------------------\n Evidence Pojištěných\n-------------------------")
action = 0


while action !=4:
    action = int(input("Vyberte si akci:\n 1 - Přidat nového pojistného\n 2 - Vypsat všechny pojištěné\n 3 - Vyhledat pojištěného\n 4 - Konec\n"))
    if action == 1:

        print("\nData byla uložena. Pokračujte libovolnou klávesou...")
        input()
    elif action == 2:


        print("\nVšechna data z tabulky byla vypsána. Pokračujte libovolnou klávesou...")
        input()
    elif action == 3:
        najdi()

        print("\nVšechny řádky, které se shodují s tímto jménem a přímením byly vypsány. Pokračujte libovolnou klávesou...")
        input()

