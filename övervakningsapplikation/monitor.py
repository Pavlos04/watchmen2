import psutil
import time

# En variabel för att hålla reda på om övervakning är aktiv
active_monitoring = False

# Funktion för att starta övervakning
def start_monitoring():
    # Använd globala variabler för att ändra statusen
    global active_monitoring
    # Sätt aktiv övervakning till True
    active_monitoring = True
    # Bekräftelsemeddelande
    print("Övervakning har startat.")

# Funktion för att lista aktuell systemövervakning
def list_active_monitoring():
    try:
        # Hämta CPU-användning i procent
        cpu_usage = psutil.cpu_percent()
        # Hämta minnesanvändning i procent
        memory_usage = psutil.virtual_memory().percent
        # Hämta diskanvändning i procent
        disk_usage = psutil.disk_usage('/').percent
        
        # Skriv ut användningsstatistik
        print(f"CPU Användning: {cpu_usage}%")
        print(f"Minne Användning: {memory_usage}%")
        print(f"Disk Användning: {disk_usage}%")
        
        # Returnera användningsstatistik för vidare bearbetning
        return cpu_usage, memory_usage, disk_usage
    except Exception as e:
        # Felhantering om något går fel vid övervakning
        print(f"Fel vid övervakning: {e}")
        return None

# Funktion för att starta övervakningsläge
def start_monitoring_mode(alarms):
    # Använd global variabel för övervakning
    global active_monitoring
    
    # Kontrollera om övervakning är aktiv
    if not active_monitoring:
        print("Ingen aktiv övervakning.")
        return
    
    try:
        # Starta en kontinuerlig övervakningsloop
        while True:
            # Hämta aktuell systemstatistik
            current_stats = list_active_monitoring()
            # Om statistik hämtades, kontrollera larm
            if current_stats:
                check_alarms(current_stats, alarms)
            # Vänta 1 sekund mellan övervakningscykler
            time.sleep(1)
    except KeyboardInterrupt:
        # Fånga avbrytning (Ctrl+C) för att stoppa övervakning
        print("\nÖvervakning avbruten.")
        active_monitoring = False

# Funktion för att kontrollera och utlösa larm
def check_alarms(current_stats, alarms):
    # Kontrollera om det finns statistik och konfigurerade larm
    if not current_stats or not alarms:
        return
    
    # Packa upp aktuell systemstatistik
    cpu_usage, memory_usage, disk_usage = current_stats
    
    # Gå igenom varje konfigurerat larm
    for alarm_type, level in alarms:
        # Kontrollera CPU-larm
        if alarm_type == "CPU" and cpu_usage > level:
            print(f"LARM: CPU-användning överstiger {level}%!")
        # Kontrollera minneslarm
        elif alarm_type == "Minnes" and memory_usage > level:
            print(f"LARM: Minnesanvändning överstiger {level}%!")
        # Kontrollera disklarm
        elif alarm_type == "Disk" and disk_usage > level:
            print(f"LARM: Diskanvändning överstiger {level}%!")