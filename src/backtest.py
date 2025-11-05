import pandas as pd
from alphas import *

df = pd.read_csv('data/prices.csv', index_col=0, parse_dates=True)

alphas = {
  "alpha_1_pairs": alpha_1_pairs(df.copy()),
  "alpha_2_breakout": alpha_2_breakout(df.copy()),
  "alpha_3_mtf": alpha_3_mtf(df.copy()),
  "alpha_4_rebalance": alpha_4_rebalance(df.copy()),
  "alpha_5_orderbook": alpha_5_orderbook(df.copy())
}

results = {}
portfolio_returns = pd.Series(0, index=df.index)
for name, signal in alphas.items():
    ret = signal.shift(1) * df['close'].pct_change()
    pnl = ret.cumsum() * 1000  # 1000 capital
    results[name] = pnl.iloc[-1]
    portfolio_returns += ret

results['portfolio'] = portfolio_returns.cumsum() * 1000
pd.DataFrame.from_dict(results, orient='index').to_csv('data/backtest_results.csv')

