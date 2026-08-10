import seaborn as sns 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame({'x': np.arange(100), 'y': np.random.rand(100).cumsum()})

sns.set_theme(style='darkgrid')

sns.lineplot(x='x',y='y',data=data)
plt.show()

sns.set_theme(style='whitegrid')
sns.lineplot(x='x',y='y',data=data)
plt.show()

sns.set_theme(style='dark')
sns.lineplot(x='x',y='y',data=data)
plt.show()

sns.set_theme(style='white')
sns.lineplot(x='x',y='y',data=data)
plt.show()

sns.set_theme(style='ticks')
sns.lineplot(x='x',y='y',data=data)
plt.show()

sns.set_theme(style='darkgrid',rc={'axes.facecolor':'grey','grid.color':'white'})

sns.lineplot(x='x',y='y',data=data)
plt.show()

df=pd.read_csv('RealEstate-USA (1).csv',delimiter=',',index_col='zip_code')

print(df.dtypes)
dffilter=df.head(20)
dffilter100=df.head(100)

sns.set_theme(style="whitegrid")

g=sns.displot(data=dffilter,x='acre_lot',y='price',hue='city',kind='hist')
g.figure.suptitle("sns.displot(data=dffilter,x=acre_lot),y='price,hue=city,kind=hist)")

g.figure.show()
read=input("Wait for me....")

g=sns.displot(data=dffilter,x='price',kind='kde')
g.figure.suptitle("sns.dislot (data=dffilter,x=acre_lot,y=price,kind=kde)")
g.figure.show()
read=input("Wait for me....")

g=sns.kdeplot(data=dffilter,x='price')
g.figure.suptitle("sns.kdeplot (data=dffilter,x=price)")
g.figure.show()
read=input("Wait for me....")

g=sns.histplot(data=dffilter,x='acre_lot',y='price',hue='city',multiple="stack")
g.figure.suptitle("sns.histplpt (data=dffilter,x='acre_lot,y='price',hue='city',multiple=stack)")
g.figure.show()
read=input("Wait for me....")

g=sns.scatterplot(data=dffilter,x='acre_lot',y='price')
g.figure.suptitle("sns.scatterplot (x='acre_lot',y='price',data='dffilter')")
g.figure.show()
read=input("Wait for me....")

g=sns.lineplot(data=dffilter,x='acre_lot',y='price')
g.figure.suptitle("sns.lineplot(data=dffilter,x='acre_lot',y='price')")
g.figure.show()
read=input("Wait for me....")

g=sns.barplot(data=dffilter,x='acre_lot',y='price',legend=False)
g.figure.suptitle("sns.barplot(x=acre_lot,y=price,data=dffilter)")
plt.show()
read=input("Wait for me.....")

g=sns.catplot(data=dffilter,x='acre_lot',y='price')
g.figure.suptitle("sns.catplot (data=dffilter,x=acre_lot,y=price)")
plt.show()
read=input("Wait for me....")

glue=dffilter.pivot(columns='acre_lot',values='price')
g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)- glue=dffilter.pivot(columns=acre_lot,values=price)")
plt.show()
read=input("Wait for me....")

