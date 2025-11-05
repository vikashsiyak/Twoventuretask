import pandas as pd, numpy as np

bt = pd.read_csv('data/backtest_results.csv', index_col=0)
sandbox = bt.copy()
sandbox['live_pnl'] = bt.iloc[:, 0] + np.random.normal(0, 2, len(bt))  # +/- 2 noise
sandbox.to_csv('data/sandbox_results.csv')

