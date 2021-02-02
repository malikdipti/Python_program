import pandas as pd

whether_data={
    'day':['1/1/2017','1/1/2018','1/1/2019','1/1/2014'],
    'tempreture':['30','32','33','34'],
    'windspeed':['3','4','5','6'],
    'event':['rain','snow','sunny','snow']
}
df=pd.DataFrame(whether_data)
print(df)

#rows,columns=df.shape
#print(columns)
#print(df.head())               #print first 5 rows
#print(df.head(2))              #print first 2 rows
#print(df.tail())                #print last 5 rows
#print(df.tail(2))               #print last 2 rows
#print(df[2:5])                  #print 2-5 row
#print(df.columns)               #print columns names
#print(df.tempreture)                  #print perticular column data
#print(df['tempreture'])              #print perticular column data
#print(type(df.tempreture))           #print type of DataFrame ..<class 'pandas.core.series.Series'>
#print(df[['event','day','tempreture']])   #print perticular columns data
#print(df['tempreture'].max())          #print maximum value
#print(df['tempreture'].min())          #print minimum value
#print(df['tempreture'].mean())          #print Avarage value

#print(df['tempreture'].std())          #print standard deviation value
#print(df.describe())            #printing the statistic data
#print(df[df.tempreture>32])
#df.where( tempreture > 0 )
#print(df.mask)
#print(df[df.tempreture==df['tempreture'].max()]) #print maximum tempreture value total rows
#print(df[['day','tempreture']][df.tempreture==df['tempreture'].max()]) #print maximum tempreture value selected column
#df.set_index('day',inplace=True) #replce and set the index value as day value
#print(df)
#print(df.loc['1/1/2019'])
#print(df.reset_index(inplace=True))
#df.set_index('event',inplace=True)
#print(df)
#print(df.loc['snow'])



''' 
df=pd.read_csv("whether2.csv")
print(df)
'''