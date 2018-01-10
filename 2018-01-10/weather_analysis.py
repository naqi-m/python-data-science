import pandas as pd

df = pd.read_csv('kclt.csv')

pd.to_datetime(df.date).head()

pd.to_datetime(df.date).head()

df[df.actual_mean_temp == 81].info()

df[df['actual_mean_temp'] < 20].date

df[(df['actual_mean_temp'] < 20) | (df['actual_mean_temp'] > 86)][['date', 'actual_mean_temp']]

df[df.date > '2015-06-01'].head()


# add a new column called total = units = unit price

# df['Total'] = df['Units'] * df['Unit Price']

# shwo the mean, sum for each rep per region

# reg_rep = df.groupby(['Region', 'Rep'])['Total'].agg(['mean', 'sum', 'count'])

# group by just Region
# regions = df.groupby(['Region'])['Total'].agg(['sum']).reset_index()
# reps = df.groupby(['Region'])['Rep'].unique().to_frame().reset_index()

# merged = reps.merge(regions, on='Region').set_index('Region')

# new column of count distinct
# merged['Count Reps'] = merged['Rep'].str.len()
# merged['Count'] = merged.apply(lambda row: len(row['Rep']), axis=1)


# avg per rep
# merged['Average Per Rep'] = merged['sum'] / merged['Count Reps']
# merged['normalized'] = merged['sum'] / merged['Count']

# person with the largest total
# sales_reps = df.groupby(['Rep'])['Total'].agg(['sum'])


# top Rep
# top_rep = sales_reps.idxmax()['sum']
