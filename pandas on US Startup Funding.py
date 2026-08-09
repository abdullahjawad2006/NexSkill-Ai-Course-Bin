import pandas as pd
df=pd.read_csv("startup_growth_investment_data.csv",delimiter=',')

print(df)
print("df-data types",df.dtypes)
print("df.info():",df.info())

print("Last Three Rows:")
print(df.tail(3))

print("First Three Rows:")
print(df.head(3))

print("Summary of Statistics of DataFrame using describe() method",df.describe())

print("Counting the rows and columns in DataFrame using shape():",df.shape)

industry=df['Industry']
print("access the name column:df:")
print(industry)

industry_country=df[['Industry','Country']]
print("access multiple columns:df:")
print(industry_country)

#Using .loc starts here
second_row=df.loc[1]
print("Selecting a single row using .loc")
print(second_row)

second_row2=df.loc[[1,3]]
print("Selecting multiple rows using .loc")
print(second_row2)

second_row3=df.loc[1:5]
print("Selecting a slice of rows using .loc")
print(second_row3)

second_row4=df.loc[df['Industry']=='SaaS']
print("Conditional selection of rows using .loc")
print(second_row4)

second_row5=df.loc[:2,'Industry']
print('Selecting a single column using .loc')
print(second_row5)

second_row6=df.loc[:2,['Industry','Country']]
print("Selecting multiple columns using .loc")
print(second_row6)

second_row7=df.loc[:3,'Industry':'Number of Investors']
print("Selecting a slice of columns using .loc")
print(second_row7)

second_row8=df.loc[df['Industry']=='SaaS','Industry':'Number of Investors']
print("Combined row and column selection using .loc")
print(second_row8)


#using .loc with index_col starts
df_index_col=pd.read_csv('startup_growth_investment_data.csv',delimiter=',',index_col='Year Founded')

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())
df_index_col=df_index_col[~df_index_col.index.duplicated()]

second_row9=df_index_col.loc[2012]
print("Selecting a single row using .loc")
print(second_row9)

second_row10=df_index_col.loc[[2012,2006]]
print("Selecting multiple rows using .loc")
print(second_row10)

second_row11=df_index_col.loc[2006:2017]
print("Selecting a slice of rows using .loc")
print(second_row11)

second_row12=df_index_col.loc[df_index_col['Industry']=='Fintech']
print("Conditional selection of rows using .loc")
print(second_row12)

second_row13=df_index_col.loc[:2011,'Industry']
print('Selecting a single column using .loc')
print(second_row13)

second_row14=df_index_col.loc[:2011,['Industry','Country']]
print('Selecting multiple columns using .loc')
print(second_row14)

second_row15=df_index_col.loc[:2016,'Industry':'Number of Investors']
print("Selecting a slice of columns using .loc")
print(second_row15)

second_row16=df_index_col.loc[df_index_col['Industry']=='Fintech','Industry':'Number of Investors']
print('Combined row and column selection using .loc')
print(second_row16)

#Using .iloc starts here:
second_row17=df_index_col.iloc[0]
print("Selecting a single row using .iloc")
print(second_row17)

second_row18=df_index_col.iloc[[1,3,5]]
print("Selecting multiple rows using .iloc")
print(second_row18)

second_row19=df_index_col.iloc[2:5]
print('Selecting a slice of rows using .iloc')
print(second_row19)

second_row20=df_index_col.iloc[:2,4]
print('Selecting a single column using .iloc')
print(second_row20)

second_row21=df_index_col.iloc[:2,[2,5]]
print("Selecting multiple columns using .iloc")
print(second_row21)

second_row22=df_index_col.iloc[:2,2:4]
print("Selecting a slice of columns using .iloc")
print(second_row22)

second_row23=df_index_col.iloc[[1,3,5],2:5]
print("Combined row and column selection using .iloc")
print(second_row23)

df.loc[len(df.index)]=["Startup_1000",'AGI',10,15648478.75,5000000000,69,"Pakistan",2026,300.15]
print("Modified DataFrame - add a new row:")
print(df)

df.drop(1,axis=0,inplace=True)
df.drop(index=2,inplace=True)
df.drop([3,5],axis=0,inplace=True)
print("Modified DataFrame - Remove Rows:")
print(df)

df.drop('Funding Rounds',axis=1,inplace=True)
df.drop(columns='Growth Rate (%)',inplace=True)
df.drop(['Startup Name','Number of Investors'],axis=1,inplace=True)
print("Modified DataFrame - delete Funding Rounds - Growth Rate (%) - Startup Name - Number of Investors - columns:")
print(df)

df.rename(columns={'Industry':'IndustryName'},inplace=True)
df.rename(mapper={'Investment Amount (USD)':'Investment Amount (PKR)','Valuation (USD)':'Valuation (PKR)'},axis=1,inplace=True)
print("Modified DataFrame Rename RowNames:")
print(df)

df.rename(index={0:5},inplace=True)
df.rename(mapper={1:7,2:8},axis=0,inplace=True)
print("Modified DataFrame Rename Row Labels:")
print(df)


selected_rows=df.query('IndustryName == "Fintech" or `Valuation (PKR)` > 500000000 ')
print(selected_rows.to_string())
print(len(selected_rows))

sorted_df=df.sort_values(by='Valuation (PKR)')
print(sorted_df.to_string(index=False))

df1=df.sort_values(by=['Investment Amount (PKR)','Valuation (PKR)'])
print("Sorting by Investment Amount (PKR) - Valuation (PKR) - ascending:")
print(df1.to_string(index=False))

grouped=df.groupby('IndustryName')['Valuation (PKR)'].sum()
print(grouped.to_string())
print("grouped:",len(grouped))

df_cleaned=df.dropna()
print("Cleaned Data:",df_cleaned)

df.fillna('0',inplace=True)
print("Data after filling NaN with 0:")

data=[10,20,30,40]
array1=pd.array(data)
print(array1)

int_array=pd.array([90,80,70,60,50,40],dtype=int)
print(int_array)









