import seaborn as sns 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df=pd.read_csv('FastFoodRestaurants.csv',delimiter=',')

print(df.dtypes)
dffilter=df.head(10)

sns.set_theme(style='whitegrid')
g=sns.displot(data=dffilter,x='name',y='city',hue='province',kind='hist')
g.figure.suptitle("sns.displot - name - city - province ")
plt.show()

sns.set_theme(style='darkgrid')
g=sns.displot(data=dffilter,x='latitude',kind='kde')
g.figure.suptitle("sns.displot - latitude - kde")
plt.show()

sns.set_theme(style='white')
g=sns.kdeplot(data=dffilter,x='longitude')
g.figure.suptitle("sns.kdeplot - longitude")
plt.show()

sns.set_theme(style='dark')
g=sns.histplot(data=dffilter,x='address',y='latitude',hue='city',multiple="stack")
g.figure.suptitle("sns.histplot - address - latitude - city - multiple")
plt.show()

sns.set_theme(style='ticks')
g=sns.scatterplot(data=dffilter,x='longitude',y='latitude')
g.figure.suptitle("sns.scatterplot - longitude - latitude")
plt.show()

sns.set_theme(style='darkgrid',rc={'axes.facecolor':'grey','grid.color':'white'})
g=sns.lineplot(data=dffilter,x='city',y='latitude')
g.figure.suptitle("sns.lineplot - city - latitude")
plt.show()

sns.set_theme(style='whitegrid',rc={'axes.facecolor':'blue','grid.color':'black'})
g=sns.barplot(data=dffilter,x='city',y='name')
g.figure.show("sns.barplot - city - name")
plt.show()

sns.set_theme(style='whitegrid')
g=sns.catplot(data=dffilter,x='province',y='name')
g.figure.suptitle("sns.catplot - province - name")
plt.show()

glue=dffilter.pivot(columns='city',values='latitude')
g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue) - columns(city) - values(latitude)")
plt.show()


