def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def main():
    print("=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit & Kelvin")
    print("2. Fahrenheit to Celsius & Kelvin")
    print("3. Kelvin to Celsius & Fahrenheit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        c = float(input("Enter temperature in Celsius: "))
        print(f"Fahrenheit: {celsius_to_fahrenheit(c):.2f}")
        print(f"Kelvin: {celsius_to_kelvin(c):.2f}")

    elif choice == "2":
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"Celsius: {fahrenheit_to_celsius(f):.2f}")
        print(f"Kelvin: {fahrenheit_to_kelvin(f):.2f}")

    elif choice == "3":
        k = float(input("Enter temperature in Kelvin: "))
        print(f"Celsius: {kelvin_to_celsius(k):.2f}")
        print(f"Fahrenheit: {kelvin_to_fahrenheit(k):.2f}")

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
