import csv
from pathlib import Path
import questionary
import fire


def load_csv(csvpath):
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def load_crypto_data(file_path):
    csvpath = Path(file_path)
    return load_csv(csvpath)

def type_of_token():
    choice = questionary.select("choose:", choices=["BTC", "ETH" , "LTC", "ADA", "XLM" , "XRP", "ZEC" , "USDT" , "DASH"]).ask()
    print(f"You selected {choice}")




def run():
    file_path = Path("../AM_workspace/2019_data.csv")
    crypto_data = load_crypto_data(file_path)
    type_of_token()
    market_variance = market_var_value

if __name__ == "__main__":
    fire.Fire(run)