import seaborn as sns 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('Real_Estate_Sales_2001-2022_GL-Short.csv',delimiter=',')

print(df.dtypes)
dffilter=df.head(10)

sns.set_theme(style='whitegrid')
g=sns.displot(data=dffilter,x='Town',y='Sale Amount',hue='Residential Type',kind='hist')
g.figure.suptitle("sns.displot-Town-Sale Amount-Residential Type")
plt.show()

sns.set_theme(style='darkgrid')
g=sns.displot(data=dffilter,x='Sale Amount',kind='kde')
g.figure.suptitle("sns.displot-Sale Amount-kde")
plt.show()

sns.set_theme(style='dark')
g=sns.histplot(data=dffilter,x='Town',y='Sale Amount',hue='Residential Type',multiple="stack")
g.figure.suptitle("sns.histplot-Town-Sale Amount-Residential Type")
plt.show()

sns.set_theme(style='ticks')
g=sns.scatterplot(data=dffilter,x='Sales Ratio',y='Sale Amount')
g.figure.suptitle("sns.scatterplot-Sales Ratio-Sale Amount")
plt.show()

sns.set_theme(style='darkgrid',rc={'axes.facecolor':'green','grid.color':'black'})
g=sns.lineplot(data=dffilter,x='Residential Type',y='Sale Amount')
g.figure.suptitle("sns.lineplot-Residential Type-Sale Amount")
plt.show()

sns.set_theme(style='whitegrid',rc={'axes.facecolor':'white','grid.color':'red'})
g=sns.barplot(data=dffilter,x='Town',y='Assessed Value')
g.figure.show("sns.barplot-Town-Assessed Value")
plt.show()

sns.set_theme(style='whitegrid')
g=sns.catplot(data=dffilter,x='Residential Type',y='Sale Amount')
g.figure.suptitle("sns.catplot-Residential Type-Sale Amount")
plt.show()

glue=dffilter.pivot(columns='Town',values='Assessed Value')
g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)-Town-Assessed Value")
plt.show()

