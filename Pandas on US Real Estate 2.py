import pandas as pd
df=pd.read_csv("Real_Estate_Sales_2001-2022_GL-Short.csv",delimiter=',')

print(df)
print("df - data types:",df.dtypes)
print("df.info():",df.info())

print("Last Three Rows:")
print(df.tail(3))

print("First Three Rows:")
print(df.head(3))

print("Summary of Statistics of DataFrame using describe() method",df.describe())

print("Counting the rows and columns in DataFrame using shape():",df.shape)

address=df['Address']
print("access the name column:df:")
print(address)

address_propertytype=df[['Address','Property Type']]
print("access multiple columns:df:")
print(address_propertytype)

#Using .loc starts here:
second_row=df.loc[1]
print("Selecting a single row using .loc")
print(second_row)

second_row2=df.loc[[2,4]]
print("Selecting multiple rows using .loc")
print(second_row2)

second_row3=df.loc[1:5]
print("Selecting a slice of rows using .loc")
print(second_row3)

second_row4=df.loc[df['Town']=='Ansonia']
print("Conditional selection of rows using .loc")
print(second_row4)

second_row5=df.loc[:2,'Town']
print("Selecting a single column using .loc")
print(second_row5)

second_row6=df.loc[:2,['Town','Property Type']]
print("Selecting multiple columns using .loc")
print(second_row6)

second_row7=df.loc[:3,'List Year':'Address']
print("Selecting a slice of columns using .loc")
print(second_row7)

second_row8=df.loc[df['Town']=='Ansonia','Town':'Property Type']
print("Combined row and column selection using .loc")
print(second_row8)

#Using .loc with index_col starts here
df_index_col=pd.read_csv("Real_Estate_Sales_2001-2022_GL-Short.csv",delimiter=',',index_col='Serial Number')

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())

second_row9=df_index_col.loc[2020225]
print("Selecting a single row using .loc")
print(second_row9)

second_row10=df_index_col.loc[[2020225,200500]]
print('Selecting multiple rows using .loc')
print(second_row10)

second_row11=df_index_col.loc[2020177:200500]
print("Selecting a slice of rows using .loc")
print(second_row11)

second_row12=df_index_col.loc[df_index_col['Town']=='Bristol']
print("Conditional selection of rows using .loc")
print(second_row12)

second_row13=df_index_col.loc[:2020090,'Town']
print("Selecting a single column using .loc")
print(second_row13)

second_row14=df_index_col.loc[:2020348,['Town','Residential Type']]
print("Selecting multiple columns using .loc")
print(second_row14)

second_row15=df_index_col.loc[:2020348,'Town':'Property Type']
print("Selecting a slice of columns using .loc")
print(second_row15)

second_row17=df_index_col.loc[df_index_col['Town']=='Essex','Town':'Property Type']
print('Combined row and column selection using .loc')
print(second_row17)

#Using .iloc starts here:
second_row18=df_index_col.iloc[1]
print("Selecting a single row using .iloc")
print(second_row18)

second_row19=df_index_col.iloc[[1,3,5]]
print("Selecting a slice of rows using .iloc")
print(second_row19)

second_row20=df_index_col.iloc[2:5]
print("Selecting a slice of rows using .iloc")
print(second_row20)

second_row21=df_index_col.iloc[:3,3]
print("Selecting a single column using .iloc")
print(second_row21)

second_row22=df_index_col.iloc[:3,[2,7]]
print("Selecting multiple columns using .iloc")
print(second_row22)

second_row23=df_index_col.iloc[:3,1:7]
print("Selecting a slice of columns using .iloc")
print(second_row23)

second_row24=df_index_col.iloc[[1,3,6],2:5]
print("Combined row and column selection using .iloc")
print(second_row24)

df.loc[len(df.index)]=[207411,2024,"20/07/24","Brentwood","79 Main St",457383.23,837929.59,0.52214,"Residential","Three Family","None","None","None",-73.28675]
print("Modified DataFrame - add a new row:")
print(df)

df.drop(1,axis=0,inplace=True)
df.drop(index=2,inplace=True)
df.drop([3,5],axis=0,inplace=True)
print("Modified DataFrame - Remove Rows:")
print(df)

df.drop('Date Recorded',axis=1,inplace=True)
df.drop(columns='Non Use Code',inplace=True)
df.drop(['Assessor Remarks','OPM remarks'],axis=1,inplace=True)
print("Modified DataFrame - delete - Date Recorded - Non Use Code - Assessor Remarks - OPM remarks, columns:")
print(df)

df.rename(columns={'List Year':'List Year Change'},inplace=True)
df.rename(mapper={'Town':'Town Change','Address':'Address Change'},axis=1,inplace=True)
print("Modified DataFrame - Rename Columns:")
print(df)

df.rename(index={0:7},inplace=True)
df.rename(mapper={4:50,10:140},axis=0,inplace=True)
print("Modified DataFrame - Rename Row Labels:")
print(df)

selected_rows = df.query('`Town Change` == "Ansonia" or `Residential Type` == "Three Family"')
print(selected_rows.to_string())
print(len(selected_rows))

print(df.columns.to_list())

sorted_df=df.sort_values(by='Sales Ratio')
print(sorted_df.to_string(index=False))

df1=df.sort_values(by=['Assessed Value','Sale Amount'])
print("Sorting by Assessed Value and then by Sale Amount (ascending):")
print(df1.to_string(index=False))

grouped=df.groupby('Town Change')['Sale Amount'].sum()
print(grouped.to_string)
print("grouped:",len(grouped))

df_cleaned=df.dropna()
print("Cleaned Data:",df_cleaned)

df.fillna("None",inplace=True)
print("Data after filling NaN with None:",df)

data=[19,65,98,33]
array1=pd.array(data)
print(array1)

int_array=pd.array([1,22,33,55,61],dtype=int)
print(int_array)








