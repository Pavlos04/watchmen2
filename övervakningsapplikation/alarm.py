# Lista för att lagra konfigurerade larm (en tom lista där vi kommer att spara våra larm)
alarms = []

# Funktion för att skapa ett nytt larm
def create_alarm():
    # Visa menyalternativ för olika larmtyper
    print("Välj larmtyp att konfigurera:")
    print("1. CPU användning")  # Alternativ för CPU-larm
    print("2. Minnesanvändning")  # Alternativ för minnesanvändningslarm
    print("3. Diskanvändning")  # Alternativ för diskanvändningslarm
    
    # Hämta användarens val av larmtyp
    choice = input("Ange ditt val (1-3): ")
    
    # Variabel för att lagra larmtypen
    alarm_type = ""
    
    # Mappa användarens val till respektive larmtyp
    if choice == '1':
        alarm_type = "CPU"  # Om val 1, sätt larmtyp till CPU
    elif choice == '2':
        alarm_type = "Minnes"  # Om val 2, sätt larmtyp till minnes
    elif choice == '3':
        alarm_type = "Disk"  # Om val 3, sätt larmtyp till disk
    else:
        # Felhantering för ogiltigt val
        print("Ogiltigt val, vänligen välj mellan 1-3.")
        return

    try:
        # Be användaren ange larmnivå och konvertera till heltal
        level = int(input("Ställ in nivå för alarm mellan 0-100: "))
        
        # Kontrollera att nivån är inom det tillåtna intervallet
        if 0 <= level <= 100:
            # Lägg till larmet i listan med larmtyp och nivå
            alarms.append((alarm_type, level))
            # Bekräftelsemeddelande
            print(f"Larm för {alarm_type} satt till {level}%.")
        else:
            # Felmeddelande om nivån är utanför intervallet
            print("Felaktig nivå, vänligen ange en siffra mellan 0-100.")
    
    except ValueError:
        # Fånga fel om användaren inte anger en numerisk nivå
        print("Felaktig inmatning. Ange en numerisk nivå.")

# Funktion för att visa konfigurerade larm
def show_alarms():
    # Kontrollera om det inte finns några larm
    if not alarms:
        print("Inga larm konfigurerade.")
    else:
        # Visa varje konfigurerat larm
        # Sortera larmen för bättre överblick
        for alarm_type, level in sorted(alarms):
            print(f"{alarm_type} larm {level}%")
    
    # Vänta på användarens input innan återgång till menyn
    input("Tryck 'Enter' för att återgå till menyn.")

# Funktion för att hämta de konfigurerade larmen
def get_alarms():
    # Returnera hela larm-listan
    return alarms