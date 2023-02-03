from datetime import datetime, timedelta #henter tiden
def sleep_function():
    sleep_hours = int(input("How many hours do you want to sleep? "))  # Spørg for tal som indsættes til variablen
    current_time = datetime.now()  # Nuværende tid kobles til variablen
    wakeup_time = current_time + timedelta(hours=sleep_hours)  # Beregner hvornår du vågner igen.
    print("Current time:", current_time.strftime("%H:%M:%S"))  # Printer nuværende tidspunkt
    print("Wakeup time:", wakeup_time.strftime("%H:%M:%S"))  # Printer tiden efter du har sovet.
    print("This is a function")

sleep_function()





