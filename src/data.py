import pandas as pd


with open("../data/raw/data.js") as f:
    data = eval(f.read())

dfs = []
for k,v in data.items():
    for kk, vv in v.items():
        dff = pd.DataFrame.from_records(vv, columns=['rate','min_range'])
        dff['status'] = kk
        dff['year'] = k
        dfs.append(dff)

df = pd.concat(dfs, ignore_index=True)

df['max_range'] = df.groupby(['status','year'])['min_range'].shift(-1)

df = df[['year','status','rate','min_range','max_range']]

df.to_csv('../data/processed/data.csv', index=False)
