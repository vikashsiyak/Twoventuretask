import pandas as pd, numpy as np
dates = pd.date_range('2025-01-01', periods=1000, freq='H')
df = pd.DataFrame({'close': 100 + np.cumsum(np.random.randn(1000))}, index=dates)
df.to_csv('data/prices.csv')

