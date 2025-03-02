import csv
import os

# Load exchange rates from CSV
def load_rates(filename):
    rates = {}
    currency_names = {}
    
    try:
        with open(filename, 'r', encoding='utf-8-sig', errors='replace') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header

            for row in reader:
                if len(row) < 3:  # Ensure at least three columns exist
                    continue
                
                currency_code = row[0].strip().upper()  # First column: Currency code
                currency_name = row[1].strip()  # Second column: Currency name
                try:
                    rate = float(row[2])  # Third column: Exchange rate
                    rates[currency_code] = rate
                    currency_names[currency_code] = currency_name  # Store full name
                except ValueError:
                    print(f"Skipping invalid rate for {currency_code}: {row[2]}")  # Show actual error value
    
    except FileNotFoundError:
        print("Error: 'currency.csv' not found.")
        exit()

    return rates, currency_names

# Convert USD to target currency
def convert(amt, cur, rates):
    return amt * rates.get(cur, None)

# Main program
def main():
    filename = "currency.csv"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(script_dir, filename)

    rates, currency_names = load_rates(path)

    if not rates:
        print("No exchange rates available.")
        return

    try:
        usd = float(input("How much dollar do you have? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    cur = input("What currency you want to have? ").strip().upper()

    if cur in rates:
        result = convert(usd, cur, rates)
        currency_full_name = currency_names.get(cur, cur)  # Get full name or fallback to code
        print(f"\nDollar: {usd} USD")
        print(f"{currency_full_name}: {result:.2f}")  # Rounded to 2 decimal places
    else:
        print("Currency not found in exchange rates.")

if __name__ == "__main__":
    main()