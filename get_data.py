from fastquant import get_crypto_data
import os


BASE = "USDT"
START_DATE = "2018-12-01"
END_DATE ="2022-3-9"

DATA_DIRECTORY = f'data/{BASE}_{START_DATE}_{END_DATE}'
CRYPTOS = ['BTC', 'ETH', 'XRP', 'BCH', 'LTC']


def download_csvs(directory, crypto_tickers):
    os.makedirs(directory, exist_ok=True)

    for ticker in crypto_tickers:
        fn = f'{ticker}.csv'
        path = os.path.join(directory, fn)

        if os.path.exists(path):
            continue

        df = get_crypto_data(f'{ticker}/{BASE}', START_DATE, END_DATE)
        df.to_csv(path)


if __name__ == "__main__":
    download_csvs(DATA_DIRECTORY, CRYPTOS)