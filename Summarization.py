import pandas
#Reading into CSV file
weather = pandas.read_csv('WEATHER.csv',skipfooter=1)
print(weather)
#Investigate range of values for random field
print(weather['Station.City'].unique())
#Filter the data
Year = weather[weather['Station.City']== 'Birmingham']
print(Year)
#Highest Temperature values
print(Year['Data.Temperature.Avg Temp'].value_counts()[:10])
#Group by month
date = Year.groupby('Date.Month')
print(len(date))
#Determine counts on each month
date_Count = date.size()
print(date_Count[0:10])
#Sort the counts in descending order
date_Count_sorted = date_Count.sort_values(ascending=False)
print(date_Count_sorted.head()) 