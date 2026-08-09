import pandas as pd
df=pd.read_csv("RealEstate-USA (1).csv",delimiter=',')
print(df)

print("df - data types",df.dtypes)

print("df.info():",df.info())

print("Last three Rows:")
print(df.tail(3))

print("First three Rwos:")
print(df.head(3))

print("Summary of Statistics of DataFrame using describe() method",df.describe())

print("Counting the rows and columns in DataFrame using shape():",df.shape)

street=df["street"]
print("access the name column:df:")
print(street)

street_city=df[['street','city']]
print("access multiple columns:df:")
print(street_city)

second_row=df.loc[1]
print("Selecting a single row using loc")
print(second_row)

second_row2=df.loc[[1,3]]
print("Selecting multiple rows using .loc")
print(second_row2)

second_row3=df.loc[1:5]
print("Selecting a slice of rows using .loc")
print(second_row3)

second_row4=df.loc[df['city']=='Adjuntas']
print("Conditional selection of rows using .loc")
print(second_row4)

second_row5=df.loc[:1,'state']
print("Selecting a single column using .loc")
print(second_row5)

second_row6=df.loc[0:5,['city','state']]
print("Selecting multiple columns using .loc")
print(second_row6)

second_row7=df.loc[0:5,'price':'acre_lot']
print("Selecting a slice of columns using .loc")
print(second_row7)

second_row8=df.loc[df["city"]=='Adjuntas','acre_lot':'city']
print("Combined row and column selection using .loc")
print(second_row8)

print("Case 2 using .loc with index_col - starts here")
df_index_col=pd.read_csv("RealEstate-USA (1).csv",delimiter=',',index_col='brokered_by')

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())
df_index_col = df_index_col[~df_index_col.index.duplicated()]

second_row9=df_index_col.loc[34632]
print("Selecting a single row using .loc")
print(second_row9)

second_row10=df_index_col.loc[[103379,1205]]
print("Selecting multiple rows using .loc")
print(second_row10)

second_row11=df_index_col.loc[103378:81909]
print("Selecting a slice of rows using .loc")
print(second_row11)

second_row12=df_index_col.loc[df_index_col['city']=='Adjuntas']
print("Conditional selection of rows using .loc")
print(second_row12)

second_row13=df_index_col.loc[:34632,'state']
print("Selecting a single column using .loc")
print(second_row13)

second_row14=df_index_col.loc[:34632,['city','state']]
print("Selecting multiple columns using .loc")
print(second_row14)

second_row15=df_index_col.loc[:34632,'bed':'state']
print("Selecting a slice of columns using .loc")
print(second_row15)

second_row16=df_index_col.loc[df_index_col['city']=='Adjuntas','bed':'state']
print("Combined row and column selection using .loc")
print(second_row16)

second_row17=df_index_col.iloc[0]
print("Selecting a single row using .iloc")
print(second_row17)

second_row18=df_index_col.iloc[[1,3,5]]
print("Selecting multiple rows using .iloc")
print(second_row18)

second_row19=df_index_col.iloc[2:5]
print("Selecting a slice of rows using .iloc")
print(second_row19)

second_row20=df_index_col.iloc[:,2]
print("Selecting a single column using .iloc")
print(second_row20)

second_row21=df_index_col.iloc[:,[2,4]]
print("Selecting multiple columns using .iloc")
print(second_row21)

second_row22=df_index_col.iloc[:,2:4]
print("Selecting a slice of columns using .iloc")
print(second_row22)

second_row23=df_index_col.iloc[[1,3,5],2:5]
print("Combined row and column selection using .iloc")
print(second_row23)

df.loc[len(df.index)]=[202606,"for_sale",108400,4,5,0.15,1407980,"Juana Diaz","Puerto Rico",786,2100,1400]
print("Modified DataFrame -add a new row")
print(df)

df.drop(1,axis=0,inplace=True)
df.drop(index=2,inplace=True)
df.drop([3,5],axis=0,inplace=True)
print("Modified DataFrame - Remove Rows:")
print(df)

df.drop('status',axis=1,inplace=True)
df.drop(columns='bath',inplace=True)
df.drop(['zip_code','prev_sold_date'],axis=1,inplace=True)
print("Modified DataFrame delete: status - bath - zip_code - prev_sold_date")
print(df)

df.rename(columns={'status':'status_changed'},inplace=True)
df.rename(mapper={'bed':'bed_changed','house_size':'house_size_changed'},axis=1,inplace=True)
print("Modified DataFrame - Rename:")
print(df)

df.rename(index={0:7},inplace=True)
df.rename(mapper={1:10,2:100},axis=0,inplace=True)
print("Modified DataFrame - Rename Row:")
print(df)

selected_rows=df.query('city=="Adjuntas" or acre_lot>0.15' )
print(selected_rows.to_string())
print(len(selected_rows))

sorted_df=df.sort_values(by='acre_lot')
print(sorted_df.to_string(index=False))

df1=df.sort_values(by=['acre_lot','street'])
print("Sorting by acre_lot ascending and then by street ascending:")
print(df1.to_string(index=False))

print(df.columns.tolist())





grouped=df.groupby('bed_changed')['acre_lot'].sum()
print(grouped.to_string())
print("grouped:",len(grouped))

df_cleaned=df.dropna()
print("Cleaned Data:\n",df_cleaned)

df.fillna(0,inplace=True)
print("\n Data after filling NaN with )0:\n",df)

data=[2,4,6,8]
array1=pd.array(data)
print(array1)

int_array=pd.array([1,2,3,4,5],dtype='int')
print(int_array)































