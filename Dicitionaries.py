monthConversions = {
  "Jan": "January",
  "Feb": "February",
  "Mar": "March",
  "Apr": "April",
  "May": "May",
  "Jun": "June",
  "Jul": "July",
  "Aug": "August",
  "Sep": "September",
  "Oct": "October",
  "Nov": "November",
  "Dec": "December"
}

print(monthConversions.get("Apr"))
#Creating a dictionary with multiple values
from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
d['b'].append(5)

print(d.get('b'))

#Keeping Dictionaries in order
from collections import OrderedDict
d = OrderedDict()
d['Ian'] = 1
d['Duncan'] = 2
d['Tira'] = 3
d['Thuku'] = 4

print(d.get('Ian'))

#Calculating with Dictionaries
prices = {
 'ACME': 45.23,
 'AAPL': 612.78,
 'IBM': 205.55,
 'HPQ': 37.20,
 'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print(min_price,max_price)

#Ranking the data above
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)