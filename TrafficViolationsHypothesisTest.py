import os
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest
pd.set_option('display.max_rows', 100000)
pd.set_option('display.max_colwidth', -1)

file = './Traffic_Violations_Final.csv'
df = pd.read_csv(file)
df = df.drop('Unnamed: 0', axis=1)

p_prop = {
    'WHITE': .438,
    'BLACK': .197,
    'ASIAN': .156,
    'HISPANIC': .196,
    'NATIVE AMERICAN': .007,
    'OTHER': .006
}

race = df[df['Violation Type'] == 'Citation']['Race'].value_counts()
total = len(df[df['Violation Type'] == 'Citation'])

print(f'CITATION COUNT BY RACE')
print('--------------------------')
print(race)
print('--------------------------')
print(f'TOTAL CITATIONS: {total}')

for var in race.index:
    count = race[var]
    prop = count/total
    stat, pval = proportions_ztest(count, total, p_prop[var])
    print('--------------------------')
    print(f'{var}:')
    print(f'     sample proportion: {"{:,.3f}".format(prop)}')
    print(f'     population proportion: {"{:,.3f}".format(p_prop[var])}')
    print(f'     z-statistic = {"{:,.2f}".format(stat)}')
    print(f'     p-value = {pval}')