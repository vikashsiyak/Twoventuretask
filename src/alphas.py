import numpy as np
import pandas as pd

def alpha_1_pairs(df):
    df['signal'] = (df['close'] - df['close'].rolling(20).mean()) / df['close'].rolling(20).std()
    return df['signal']

def alpha_2_breakout(df):
    df['signal'] = np.where(df['close'] > df['close'].rolling(10).max(), 1, -1)
    return df['signal']

def alpha_3_mtf(df):
    df['signal'] = np.sign(df['close'].rolling(30).mean() - df['close'].rolling(60).mean())
    return df['signal']

def alpha_4_rebalance(df):
    df['signal'] = np.random.choice([-1, 1], len(df))
    return df['signal']

def alpha_5_orderbook(df):
    df['signal'] = np.sign(np.random.randn(len(df)))
    return df['signal']

