import sys
import requests


URL = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=04299be4b44441f1eba7bda16471284fbd977ccef9fcd6484cca14bd06d113c2"


def main():

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument" if len(sys.argv) == 1 else "Too many command-line arguments")

    try:
        coins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get(URL, timeout=30)
        response.raise_for_status()  #turns HTTP error status codes (404/500...) into an exception so you can handle it cleanly
        json_file = response.json()
        usd_price = float(json_file["data"]["priceUsd"])
    except (requests.RequestException, KeyError, TypeError, ValueError):
        sys.exit("Error fetching Bitcoin price")

    amount = coins * usd_price
    print(f"${amount:,.4f}")


if __name__ == '__main__':
    main()

