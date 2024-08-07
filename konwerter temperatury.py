def celsius_na_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_na_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def konwerter_temperatury():
    print("Konwerter Temperatury")
    print("Wybierz konwersję:")
    print("1. Celsjusz na Fahrenheit")
    print("2. Fahrenheit na Celsjusz")
    
    while True:
        wybor = input("Wybierz (1/2): ")

        if wybor in ['1', '2']:
            if wybor == '1':
                celsius = float(input("Podaj temperaturę w stopniach Celsjusza: "))
                fahrenheit = celsius_na_fahrenheit(celsius)
                print(f"{celsius}°C to {fahrenheit:.2f}°F")
            elif wybor == '2':
                fahrenheit = float(input("Podaj temperaturę w stopniach Fahrenheita: "))
                celsius = fahrenheit_na_celsius(fahrenheit)
                print(f"{fahrenheit}°F to {celsius:.2f}°C")
            
            nastepna_konwersja = input("Czy chcesz wykonać kolejną konwersję? (tak/nie): ")
            if nastepna_konwersja.lower() != 'tak':
                break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    konwerter_temperatury()
