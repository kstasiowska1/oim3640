import yfinance as yf

# stock = yf.Ticker("AAPL")
# info = stock.info
# print(type(info))

# print(info.keys()) #to show the keys when you dont have the name
# print(len(info)) #shows how many attributes there are
# print(info['shortName'])
# print(info['longName'])
# print(info['currentPrice'])

# #print(info['longBusinessSummary'])

# print(info['longBusinessSummry'].split())
# #print('iPhone' in info['longBusinessSummary']).split #wont work becuase there is a comma
# #print('iPhone' in info['longBusinessSummary'])

# print(info['city'])
# #info['city'][0] = 'c' #doesnt work, its a string
# info['city'] = 'Wellesley'
# print(info['city'])

# info['founder'] = 'Robert'
# print(info['founder'])

# for k, v in info.items():
#     print(k, v)

tickers = ['AAPL', 'NVDA', 'MSFT']
prices = {}
for t in tickers:
    prices[t] = yf.Ticker(t).info['currentPrice']

print(prices)

print(sorted(prices)) #create a new list of the keys in prices, sorted alphabetically
print(sorted(prices.values())) #creates a new list of the values in prices, sorted from largest to smallest
print(sorted(prices.values(), reverse = True)) #sorting in reverse

# how to sort stocks by values, but still to show key:value
# total value of all 3 stocks
print(sum(prices.values()))

# without using 'sum'
total = 0
for price in prices.values():
    total += price
print(total)

# how to add Google to the list
tickers.append('GOOG')
print(tickers)
tickers = {}
for t in tickers:
    prices[t] = yf.Ticker(t).info['currentPrice']
print(prices)

