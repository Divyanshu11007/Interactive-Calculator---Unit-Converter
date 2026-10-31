import sys

KM_TO_MILES = 0.621371
MILES_TO_KM = 1.609344

CURRENCY_RATES = {
    "1": ("USD", "EUR", 0.92),
    "2": ("EUR", "USD", 1.09),
    "3": ("USD", "INR", 83.50),
    "4": ("INR", "USD", 0.012),
    "5": ("USD", "GBP", 0.79),
    "6": ("GBP", "USD", 1.27),
    "7": ("EUR", "INR", 90.80),
    "8": ("INR", "EUR", 0.011),
}


def get_number(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("That is not a valid number. Please try again.")


def get_operation(prompt, valid_options):
    while True:
        choice = input(prompt).strip()
        if choice in valid_options:
            return choice
        print("Invalid choice. Please enter one of: " + ", ".join(valid_options))


def format_result(value):
    if value == int(value):
        return str(int(value))
    return f"{value:.4f}".rstrip("0").rstrip(".")


def run_calculator():
    print("\n--- Arithmetic Calculator ---")
    operation = get_operation(
        "Choose an operation (+, -, *, /): ", ["+", "-", "*", "/"]
    )
    a = get_number("Enter the first number: ")
    b = get_number("Enter the second number: ")

    while operation == "/" and b == 0:
        print("Error: cannot divide by zero.")
        b = get_number("Enter a non-zero second number: ")

    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    else:
        result = a / b

    print(f"\n{format_result(a)} {operation} {format_result(b)} = {format_result(result)}")


def run_unit_converter():
    print("\n--- Unit Converter ---")
    choice = get_operation(
        "1. Kilometers -> Miles\n2. Miles -> Kilometers\n3. Celsius -> Fahrenheit\n4. Fahrenheit -> Celsius\nChoose an option (1-4): ",
        ["1", "2", "3", "4"],
    )

    if choice == "1":
        km = get_number("Enter distance in kilometers: ")
        miles = km * KM_TO_MILES
        print(f"\n{format_result(km)} km = {format_result(miles)} miles")
    elif choice == "2":
        miles = get_number("Enter distance in miles: ")
        km = miles * MILES_TO_KM
        print(f"\n{format_result(miles)} miles = {format_result(km)} km")
    elif choice == "3":
        c = get_number("Enter temperature in Celsius: ")
        f = c * 9 / 5 + 32
        print(f"\n{format_result(c)} °C = {format_result(f)} °F")
    else:
        f = get_number("Enter temperature in Fahrenheit: ")
        c = (f - 32) * 5 / 9
        print(f"\n{format_result(f)} °F = {format_result(c)} °C")


def run_currency_converter():
    print("\n--- Currency Converter (fixed sample rates) ---")
    for key, (from_cur, to_cur, rate) in sorted(CURRENCY_RATES.items()):
        print(f"{key}. {from_cur} -> {to_cur} (1 {from_cur} = {rate} {to_cur})")

    choice = get_operation(
        "Choose an option (1-8): ",
        [str(key) for key in CURRENCY_RATES],
    )
    from_cur, to_cur, rate = CURRENCY_RATES[choice]
    amount = get_number(f"Enter amount in {from_cur}: ")
    converted = amount * rate
    print(f"\n{format_result(amount)} {from_cur} = {format_result(converted)} {to_cur}")


def ask_play_again():
    while True:
        answer = input("\nBack to main menu? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer y or n.")


def main():
    print("=" * 40)
    print(" Interactive Calculator & Unit Converter ")
    print("=" * 40)

    while True:
        choice = get_operation(
            "\nMAIN MENU\n1. Arithmetic calculator\n2. Unit converter\n3. Currency converter\n4. Exit\nChoose an option (1-4): ",
            ["1", "2", "3", "4"],
        )

        if choice == "1":
            run_calculator()
        elif choice == "2":
            run_unit_converter()
        elif choice == "3":
            run_currency_converter()
        else:
            print("Goodbye!")
            sys.exit(0)

        if not ask_play_again():
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
