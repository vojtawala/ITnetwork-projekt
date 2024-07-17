# Vytvoření třídy pro pojištěnou osobu
class Pojisteny:
    def __init__(self, jmeno, prijmeni, vek, telefon): # Potřebuji vždy jméno, příjmení, věk a telefonní číslo
        if not jmeno or not prijmeni:
            raise ValueError("Jméno a příjmení nesmí být prázdné.")  # Vytvoření podmínky, že pokud někdo nezadá jméno nebo příjmení, tak vyskočí error
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    # Metoda která vrátí/uloží danou osobu --> Nevypíše jí, to by tam muselo být "print"
    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}\t{self.vek}\t{self.telefon}"


# Třída pro správu pojištěných osob
class EvidencePojistenych:
    def __init__(self):
        # Inicializuje/vytvoří prázdný seznam pojištěných osob
        self.pojisteni = []

    # Metoda, která přidá nového pojištěnce do seznamu a to pomocí třídy "Pojisteny"
    def pridat_pojisteneho(self, pojisteny):
        self.pojisteni.append(pojisteny) #(seznam)+přidat+(pojisteny)

    # Metoda, která vrátí/uloží do seznamu osobu, která byla přes třídu "Pojisteny" vložena
    def vypsat_vsechny_pojistene(self):
        return self.pojisteni

    #Metoda, která hledá pojištěnou osobu podle jména a příjmení
    def vyhledat_pojisteneho(self, jmeno, prijmeni):
        for pojisteny in self.pojisteni: #Cyklus, který tvrdí, že pro každou osobu vytvořenou třídou "Pojisteny" v seznamu "self.pojisteni"
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni: #která má stejné jméno a příjmení
                return pojisteny #Vypíše jeho údaje
        return None


# Třída pro komunikaci s uživatelem prostřednictvím konzole
class KonzoloveUI:
    def __init__(self):
        # Inicializuje instanci třídy EvidencePojistenych
        self.evidence = EvidencePojistenych() # Odkazuje na to, že když se zavolá funkce "self.evidence", tak proběhne celá třída "EvidencePojistenych"

    # Zobrazí hlavní menu aplikace
    def zobrazit_menu(self):
        print("-----------------------------")
        print("Evidence pojištěných")
        print("-----------------------------")
        print("Vyberte si akci:")
        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Konec")

    # Metoda, která vytvoří nového pojištěnce a to tak, že předá informace třídě "Pojisteny", pojí se na tu třídu.
    def pridat_noveho_pojisteneho(self):
        jmeno = input("Zadejte jméno pojištěného: ")
        prijmeni = input("Zadejte příjmení: ")
        vek = int(input("Zadejte věk: "))
        telefon = input("Zadejte telefonní číslo: ")
        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon) #Zde předá informace pro třídu "Pojisteny"
        self.evidence.pridat_pojisteneho(pojisteny) #Spouští metodu "pridat_pojisteneho" z třídy "EvidencePojistenych" = Jednodušše ho přidá do seznamu
        print("Data byla uložena. Pokračujte libovolnou klávesou...")

    # Metoda, která vypíše všechny pojištěné osoby ze seznamu
    def vypsat_vsechny_pojistene(self):
        for pojisteny in self.evidence.vypsat_vsechny_pojistene(): #Cyklus, který vypíše všechny "pojisteny" ze třídy "self.evidence" uložené pomocí metody "vypsat_vsechny_pojistene"
            print(pojisteny)
        input("Pokračujte libovolnou klávesou...")

    # Metoda, která hledá pojištěnou osobu podle jména a příjmení
    def vyhledat_pojisteneho(self):
        jmeno = input("Zadejte jméno pojištěného: ")
        prijmeni = input("Zadejte příjmení: ")
        pojisteny = self.evidence.vyhledat_pojisteneho(jmeno, prijmeni)
        if pojisteny:
            print(pojisteny)
        else:
            print("Pojištěný nebyl nalezen.")
        input("Pokračujte libovolnou klávesou...")

    # Spustí hlavní smyčku aplikace
    def spustit(self):
        while True:
            self.zobrazit_menu()
            volba = input()
            if volba == "1":
                self.pridat_noveho_pojisteneho()
            elif volba == "2":
                self.vypsat_vsechny_pojistene()
            elif volba == "3":
                self.vyhledat_pojisteneho()
            elif volba == "4":
                break
            else:
                print("Neplatná volba, zkuste to znovu.")


# Hlavní část programu
if __name__ == "__main__":
    # Vytvoří instanci třídy KonzoloveUI a spustí aplikaci
    ui = KonzoloveUI()
    ui.spustit()
