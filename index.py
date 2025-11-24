def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

def convert_temperature(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == to_unit:
        return value

    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            return celsius_to_fahrenheit(value)
        elif to_unit == "kelvin":
            return celsius_to_kelvin(value)
    elif from_unit == "fahrenheit":
        if to_unit == "celsius":
            return fahrenheit_to_celsius(value)
        elif to_unit == "kelvin":
            return fahrenheit_to_kelvin(value)
    elif from_unit == "kelvin":
        if to_unit == "celsius":
            return kelvin_to_celsius(value)
        elif to_unit == "fahrenheit":
            return kelvin_to_fahrenheit(value)
    raise ValueError("Invalid conversion units.")

if __name__ == "__main__":
    print("Temperature Converter")
    print("Supported units: Celsius, Fahrenheit, Kelvin")
    value = float(input("Enter value: "))
    from_unit = input("From unit: ").strip()
    to_unit = input("To unit: ").strip()
    try:
        result = convert_temperature(value, from_unit, to_unit)
        print(f"{value} {from_unit.title()} = {result:.2f} {to_unit.title()}")
    except Exception as e:
        print("Error:", e)