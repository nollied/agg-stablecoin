import numpy as np
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


def plot_averages(cryptos=CRYPTOS, normalize=False):
    # TODO: docstring

    dfs = [pd.read_csv(get_path(ticker)) for ticker in cryptos]
    day_values = defaultdict(list)

    for df in dfs:
        dts = df['dt']
        highs = df['high']

        if normalize:
            highs /= np.linalg.norm(highs)

        for dt, high in zip(dts, highs):
            day_values[dt].append(high)

    X = []
    Y = []
    for day, values in day_values.items():
        X.append(day)
        Y.append(sum(values) / len(values))

    print(X)

    plt.plot(range(len(X)), Y)
    plt.show()



if __name__ == "__main__":
    plot_averages(['BTC'])
    plot_averages()
    # for ticker in CRYPTOS:
    #     plot_currency(ticker)
    #     break
