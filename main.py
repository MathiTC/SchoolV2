from datetime import datetime, timedelta #henter tiden
current_time = datetime.now()  # Nuværende tid kobles til variablen

# Kilde talvalidations kode https://github.com/Robotto/endnuNyereProjekt/blob/master/viTesterInput.py
def talvalidation(x):
    tastet = input(x)
    try:
        return float(tastet)
    except ValueError:
        print("Huskede du at skrive et tal? Prøv lige igen...")
        return talvalidation(x)



print("Welcome to the Sleep Calculator")
sleep_hours = talvalidation("How many hours do you want to sleep?")
wakeup_time = current_time + timedelta(hours=sleep_hours)  # Beregner hvornår du vågner igen.
print("Current time:", current_time.strftime("%H:%M:%S"))  # Printer nuværende tidspunkt
print("Wakeup time:", wakeup_time.strftime("%H:%M:%S"))  # Printer tiden efter du har sovet.
print("Thanks for using the Sleep Calculator")
