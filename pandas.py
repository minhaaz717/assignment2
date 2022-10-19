{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2715\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 #Read the provided CSV file \'91data.csv\'92.\
import pandas as pd\
data = pd.read_csv("data.csv")\
data.head()\
#Show the basic statistical description about the data.\
data.describe()\
# Check if the data has null values.\
data.isnull().any()\
#Replace the null values with the mean\
data.fillna(data.mean(), inplace=True)\
data.isnull().any()\
#4Select at least two columns and aggregate the data using: min, max, count, mean.\
data.agg(\{'Duration':['min','max','count','mean'],'Pulse':['min','max','count','mean']\})\
#5Filter the dataframe to select the rows with calories values between 500 and 1000.\
data.loc[(data['Calories']>500)&(data['Calories']<1000)]\
#6Filter the dataframe to select the rows with calories values > 500 and pulse < 100.\
data.loc[(data['Calories']>500)&(data['Pulse']<100)]\
#7Create a new \'93df_modified\'94 dataframe that contains all the columns from df except for \'93Maxpulse\'94.\
df_modified = data[['Duration','Pulse','Calories']]\
df_modified.head()\
#8Delete the \'93Maxpulse\'94 column from the main df dataframe\
del data['Maxpulse']\
data.head()\
#9Convert the datatype of Calories column to int datatype.\
data['Calories'] = data['Calories'].astype(np.int64)\
data.dtypes\
#10Using pandas create a scatter plot for the two columns (Duration and Calories).\
data.plot.scatter(x='Duration',y='Calories',c='DarkBlue')\
}