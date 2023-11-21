import pandas as pd

#upload the data
df = pd.read_csv('salaries_by_college_major.csv')
df.head()

#data exploration and data cleaning
df.shape
df.columns
df.isna()
df.tail()
clean_df = df.dropna()
clean_df.tail()

#accessing columns and cells

clean_df['Starting Median Salary'].max()
clean_df['Starting Median Salary'].idxmax()
clean_df['Starting Median Salary'][43]
clean_df['Undergraduate Major'].loc[43]
clean_df.loc[43]

print(clean_df['Mid-Career Median Salary'].max())
print(f"Index for the max mid career salary: {clean_df['Mid-Career Median Salary'].idxmax()}")
clean_df['Undergraduate Major'][8]

print(clean_df['Starting Median Salary'].min())
clean_df['Undergraduate Major'].loc[clean_df['Starting Median Salary'].idxmin()]

clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()]

#sorting values and adding columns

# clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
# clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
clean_df.head()

low_risk = clean_df.sort_values('Spread')
low_risk[['Undergraduate Major', 'Spread']].head()

highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()

highest_spread = clean_df.sort_values('Spread', ascending=False)
highest_spread[['Undergraduate Major', 'Spread']].head()

highest_spread = clean_df.sort_values('Mid-Career Median Salary', ascending=False)
highest_spread[['Undergraduate Major', 'Mid-Career Median Salary']].head()

#grouping and pivoting data with pandas

clean_df.groupby('Group').count()

pd.options.display.float_format = '{:,.2f}'.format
clean_df.groupby('Group').mean()

