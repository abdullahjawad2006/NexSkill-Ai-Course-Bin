import pandas as pd
df=pd.read_csv("FastFoodRestaurants.csv",delimiter=',')
print(df)

print("df - data types",df.dtypes)

print("df.info():",df.info())

print('Last Three Rows:')
print(df.tail(3))

print("First Three Rows:")
print(df.head(3))

print("Summary of Statistics of DataFrame using describe() method",df.describe())

print("Counting the rows and columns in DataFrame using shape():",df.shape)

city=df['city']
print("access the Name column:df:")
print(city)

city_country=df[['city','country']]
print("access multiple columns:df:")
print(city_country)

second_row=df.loc[1]
print("Selecting a single row using loc")
print(second_row)

second_row2=df.loc[[1,3]]
print("Selecting multiple rows using .loc")
print(second_row2)

second_row3=df.loc[1:5]
print("Selecting a slice of rows .loc")
print(second_row3)

second_row4=df.loc[df['city']=='Massena']
print("Conditional Selection of rows using .loc")
print(second_row4)

second_row5=df.loc[:3,'city']
print("Selecting a single column using .loc")
print(second_row5)

second_row6=df.loc[1:5,['city','country']]
print("Selecting multiple columns using .loc")
print(second_row6)

second_row7=df.loc[:3,'city':'name']
print("Selecting a slice of columns using .loc")
print(second_row7)

second_row8=df.loc[df['city']=='Massena','city':'name']
print("Combined row and column selection using .loc")
print(second_row8)

#Using .loc with index_col 
df_index_col=pd.read_csv("FastFoodRestaurants.csv",delimiter=',',index_col='postalCode')

df_index_col=df_index_col[~df_index_col.index.duplicated()]

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())

second_row9=df_index_col.loc["13662"]
print("Selecting a single row using .loc")
print(second_row9)

second_row10=df_index_col.loc[["13662","45011"]]
print("Selecting multiple rows using .loc")
print(second_row10)

second_row11=df_index_col.loc["13662":"45701"]
print("Selecting a slice of rows using .loc")
print(second_row11)

second_row12=df_index_col.loc[df_index_col['province']=='NY']
print("Conditional selection of rows using .loc")
print(second_row12)

second_row13=df_index_col.loc[:"41056",'province']
print('Selecting a single column using .loc')
print(second_row13)

second_row14=df_index_col.loc[:"41056",['city','country']]
print('Selecting multiple columns using .loc')
print(second_row14)

second_row15=df_index_col.loc[:"41056",'city':'keys']
print('Selecting a slice of columns using .loc')
print(second_row15)

second_row16=df_index_col.loc[df_index_col['city']=='Massena','city':'keys']
print("Combined row and column selection using .loc")
print(second_row16)

#Using .iloc
second_row17=df_index_col.iloc[0]
print('Selecting a single row using .iloc')
print(second_row17)

second_row18=df_index_col.iloc[[1,3,5]]
print("Selecting multiple rows using .iloc")
print(second_row18)

second_row19=df_index_col.iloc[2:5]
print("Selecting a slice of rows using .iloc")
print(second_row19)

second_row20=df_index_col.iloc[0:2,3]
print("Selecting a single column using .iloc")
print(second_row20)

second_row21=df_index_col.iloc[0:2,[2,4]]
print("Selecting multiple columns using .iloc")
print(second_row21)

second_row22=df_index_col.iloc[0:2,2:4]
print('Selecting a single column using .iloc')
print(second_row22)

second_row23=df_index_col.iloc[[1,3,5],2:4]
print("Selecting row and column selection using .iloc")
print(second_row23)

df.loc[len(df.index)]=["94 Main St","Las Angles","USA","us/ny/las angles/94 main st/-678289",1878389.889,-72.273883,"KFC",15015,"NY","https//kfc.com."]
print("Modified DataFrame - add a new row")
print(df)

df.drop(1,axis=0,inplace=True)
df.drop(index=2,inplace=True)
df.drop([3,5],axis=0,inplace=True)
print('Modified DataFrame - Remove Rows:')
print(df)

df.drop('province',axis=1,inplace=True)
df.drop(columns='country',inplace=True)
df.drop(['address','keys'],axis=1,inplace=True)
print("Modifies DataFrame - delete province - country - address - keys , column:")
print(df)

df.rename(columns={'city':'cityname'},inplace=True)
df.rename(mapper={'address':'addresschanged','name':'namechanged'},axis=1,inplace=True)
print("Modified DataFrame - Rename columns:")
print(df)

df.rename(index={0:5},inplace=True)
df.rename(mapper={1:6,2:10},axis=0,inplace=True)
print("Modified DataFrame - Rename Rows:")
print(df)

selected_rows=df.query('cityname == "Massena" or latitude > 60')
print(selected_rows.to_string())
print(len(selected_rows))

sorted_df=df.sort_values(by='latitude')
print(sorted_df.to_string(index=False))

grouped=df.groupby('cityname')['latitude'].sum()
print(grouped.to_string())
print("grouped:",len(grouped))

df_cleaned=df.dropna()
print("Cleaned Data:",df_cleaned)

df.fillna('0',inplace=True)
print('Data after filling NaN with 0:',df)

data=[2,4,6,8]
array1=pd.array(data)
print(array1)

int_array=pd.array([1,2,3,4,5],dtype='int')
print(int_array)









