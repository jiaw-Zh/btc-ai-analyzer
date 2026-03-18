import numpy as np
import pandas as pd


def sma(data, window):
    return data.rolling(window=window).mean()


def ema(data, window):
    return data.ewm(span=window, adjust=False).mean()


def macd(data, short_window=12, long_window=26, signal_window=9):
    ema_short = ema(data, short_window)
    ema_long = ema(data, long_window)
    macd = ema_short - ema_long
    signal = ema(macd, signal_window)
    return macd, signal


def rsi(data, window):
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))


def bollinger_bands(data, window, num_std_dev=2):
    rolling_mean = sma(data, window)
    rolling_std = data.rolling(window=window).std()
    upper_band = rolling_mean + (rolling_std * num_std_dev)
    lower_band = rolling_mean - (rolling_std * num_std_dev)
    return upper_band, lower_band
