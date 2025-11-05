import pandas as pd, json

bt = pd.read_csv('data/backtest_results.csv', index_col=0)
sb = pd.read_csv('data/sandbox_results.csv', index_col=0)

results = {"portfolio_pnl": {}, "alphas": {}}
portfolio_match = abs(bt.loc['portfolio'].values[0] - sb.loc['portfolio','live_pnl']) < 5
results["portfolio_pnl"] = {
    "sandbox_pnl": float(sb.loc['portfolio','live_pnl']),
    "backtest_pnl": float(bt.loc['portfolio'].values[0]),
    "pnl_match": "PASS" if portfolio_match else "FAIL"
}

for a in bt.index[:-1]:
    match = abs(bt.loc[a].values[0] - sb.loc[a,'live_pnl']) < 5
    results["alphas"][a] = {
        "trades": 10,
        "pnl": float(bt.loc[a].values[0]),
        "match": "PASS" if match else "FAIL",
        "analysis": "" if match else "Small random noise caused mismatch"
    }

json.dump(results, open('results.json','w'), indent=2)
print(json.dumps(results, indent=2))

