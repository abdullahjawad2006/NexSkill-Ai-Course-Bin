import seaborn as sns 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

df=pd.read_csv('startup_growth_investment_data.csv',delimiter=',')

print(df.dtypes)
dffilter=df.head(10)

sns.set_theme(style='whitegrid')
g=sns.displot(data=dffilter,x='Industry',y='Number of Investors',hue='Country',kind='hist')
g.figure.suptitle("sns.displot-Industry-Number of Investors-Country-hist")
plt.show()

sns.set_theme(style='darkgrid')
g=sns.displot(data=dffilter,x='Funding Rounds',kind='kde')
g.figure.suptitle("sns.displot-Funding Rounds-kde")
plt.show()

sns.set_theme(style='white')
g=sns.kdeplot(data=dffilter,x='Number of Investors')
g.figure.suptitle("sns.kdeplot-Number of Investors")
plt.show()

sns.set_theme(style='dark')
g=sns.histplot(data=dffilter,x='Industry',y='Valuation (USD)',hue='Country',multiple="stack")
g.figure.suptitle("sns.histplot-Industry-Valuation(USD)-Country-Stack")
plt.show()

sns.set_theme(style='ticks')
g=sns.scatterplot(data=dffilter,x='Number of Investors',y='Investment Amount (USD)')
g.figure.suptitle("sns.scatterplot-Number of Investors-Investment Amount(USD)")
plt.show()

sns.set_theme(style='darkgrid',rc={'axes.facecolor':'green','grid.color':'black'})
g=sns.lineplot(data=dffilter,x='Industry',y='Funding Rounds')
g.figure.suptitle("sns.lineplot-Industry-Funding Rounds")
plt.show()

sns.set_theme(style='whitegrid',rc={'axes.facecolor':'yellow','grid.color':'black'})
g=sns.barplot(data=dffilter,x='Industry',y='Valuation (USD)')
g.figure.suptitle("sns.barplot-Industry-Valuation (USD)")
plt.show()

sns.set_theme(style="darkgrid")
g=sns.catplot(data=dffilter,x='Country',y='Number of Investors')
g.figure.suptitle("sns.catplot-Country-Number of Investors")
plt.show()

glue=dffilter.pivot(columns='Industry',values='Investment Amount (USD)')
g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)-Industry-Investment Amount(USD)")
plt.show()

