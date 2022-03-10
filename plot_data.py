import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from get_data import DATA_DIRECTORY, CRYPTOS, START_DATE, END_DATE, get_path
from functools import reduce
from collections import defaultdict


def plot_currency(ticker):
    field = 'high'
    df = pd.read_csv(get_path(ticker))
    df.plot(x='dt', y=field)
    plt.show()


def plot_averages(title, cryptos=CRYPTOS, normalize=False, moving_avg_window=1):
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

    # calculate Y's moving average
    if moving_avg_window > 1:
        Y_avg = []
        for i in range(len(Y)):
            if i >= moving_avg_window:
                Y_avg.append(np.mean(Y[i - moving_avg_window:i]))
        plt.plot(range(len(Y_avg)), Y_avg)
    else:
        plt.plot(range(len(X)), Y)
    
    plt.xlabel(f'Days between {START_DATE} and {END_DATE}')
    plt.ylabel('Price (USD)')
    plt.title(title)

    plt.show()



if __name__ == "__main__":
    plot_averages('$BTC', ['BTC'])
    plot_averages('$AGG', moving_avg_window=1, normalize=True)
    plot_averages('$AGG (using a 1-year moving average)', moving_avg_window=365, normalize=True)

