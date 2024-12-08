# Importera nödvändiga moduler
import monitor
import alarm

# Huvudmeny-funktion för att hantera programflödet
def huvudmeny():
    # Starta en oändlig loop för menyhantering
    while True:
        # Skriv ut menyalternativ
        print("\nÖvervaknings- och larmsystem")
        print("1. Starta övervakning")
        print("2. Lista aktiv övervakning")
        print("3. Skapa larm")
        print("4. Visa konfigurerade larm")
        print("5. Starta övervakningsläge")
        print("6. Avsluta programmet")
        
        # Hämta användarens val
        användarval = input("Ange ditt val (1-6): ")
        
        # Hantera olika menyval
        if användarval == '1':
            # Starta övervakning
            monitor.start_monitoring()
        elif användarval == '2':
            # Lista aktuell övervakning
            monitor.list_active_monitoring()
        elif användarval == '3':
            # Skapa nytt larm
            alarm.create_alarm()
        elif användarval == '4':
            # Visa konfigurerade larm
            alarm.show_alarms()
        elif användarval == '5':
            # Starta övervakningsläge med konfigurerade larm
            monitor.start_monitoring_mode(alarm.get_alarms())
        elif användarval == '6':
            # Avsluta programmet
            print("Avslutar programmet...")
            break
        else:
            # Hantera ogiltigt val
            print("Ogiltigt val. Försök igen.")

# Huvudinmatningspunkt för programmet
if __name__ == "__main__":
    # Starta huvudmenyn när scriptet körs direkt
    huvudmeny()