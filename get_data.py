from fastquant import get_crypto_data
import os


BASE = "USDT"
START_DATE = "2018-12-01"
END_DATE ="2022-3-9"

DATA_DIRECTORY = f'data/{BASE}_{START_DATE}_{END_DATE}'
CRYPTOS = ['BTC', 'ETH', 'BNB', 'XRP', 'LUNA', 'ADA', 'SOL', 'AVAX', 'DOT', 'DOGE', 'SHIB', 'MATIC', 'DAI', 'USDC']


def get_path(ticker):
    fn = f'{ticker}.csv'
    return os.path.join(DATA_DIRECTORY, fn)


def download_csvs(crypto_tickers):
    os.makedirs(DATA_DIRECTORY, exist_ok=True)

    for ticker in crypto_tickers:
        path = get_path(ticker)

        if os.path.exists(path):
            continue

        df = get_crypto_data(f'{ticker}/{BASE}', START_DATE, END_DATE)
        df.to_csv(path)


if __name__ == "__main__":
    download_csvs(CRYPTOS)