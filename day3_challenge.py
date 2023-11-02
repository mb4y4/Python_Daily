#currency converter


exchange_rates = {
    'USD': 1.0,
    'EUR': 0.85,
    'GBP': 0.73,
    'JPY': 114.47,
    'KES': 150.0,  
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Currency not supported or invalid."

    exchange_rate = exchange_rates[to_currency] / exchange_rates[from_currency]
    converted_amount = amount * exchange_rate
    return converted_amount

def main():
    print("Currency Converter")
    amount = float(input("Enter the amount: "))
    from_currency = input("From currency (e.g., USD, EUR, GBP, KES): ").upper()
    to_currency = input("To currency (e.g., USD, EUR, GBP, KES): ").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency)
    if isinstance(converted_amount, str):
        print(converted_amount)
    else:
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()
