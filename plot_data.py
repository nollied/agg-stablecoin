import pandas as pd
import matplotlib.pyplot as plt
from get_data import DATA_DIRECTORY, CRYPTOS, get_path
from functools import reduce
from collections import defaultdict


def plot_currency(ticker):
    field = 'high'
    df = pd.read_csv(get_path(ticker))
    df.plot(x='dt', y=field)
    plt.show()


def plot_averages(cryptos=CRYPTOS, num_days=1):
    # TODO: docstring

    if num_days <= 0:
        raise ValueError("num_days must be greater than 0")

    dfs = [pd.read_csv(get_path(ticker)) for ticker in cryptos]
    day_values = defaultdict(list)

    for df in dfs:
        dts = df['dt']
        highs = df['high']
        last_day = dts[0]
        day_cycle = 0

        for dt, high in zip(dts, highs):
            day_values[last_day].append(high)

            # each value is averaged over the previous `num_days`
            day_cycle = (day_cycle + 1) % num_days
            if day_cycle == 0:
                last_day = dt

    X = []
    Y = []
    for day, values in day_values.items():
        X.append(day)
        Y.append(reduce(lambda x, y: x + y, values) / len(values))

    plt.plot(range(len(X)), Y)
    plt.show()



if __name__ == "__main__":
    plot_averages()
    # for ticker in CRYPTOS:
    #     plot_currency(ticker)
    #     break
