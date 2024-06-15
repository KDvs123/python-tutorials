# You are given following list of stocks and their prices in last 3 days,

# Stock	 Prices
# info	[600,630,620]
# ril	[1430,1490,1567]
# mtl	[234,180,160]

# Write a program that asks user for operation. Value of operations could be,

# print: When user enters print it should print following,
# info ==> [600, 630, 620] ==> avg:  616.67
# ril ==> [1430, 1490, 1567] ==> avg:  1495.67
# mtl ==> [234, 180, 160] ==> avg:  191.33

stock_info={"info":[600,630,620],"ril":[1430,1490,1567],"mtl":[234,180,160]}

for k,v in stock_info.items():
    print(f"{k.lower()} ==> {v} ==> avg:  {sum(stock_info[k])/len(stock_info[k])}")

# add: When user enters 'add', 
# it asks for stock ticker and price.
#  If stock already exist in your list 
# (like info, ril etc) then it will 
# append the price to the list. 
# Otherwise it will create new entry 
# in your dictionary. 
# For example entering 'tata' and 
# 560 will add tata ==> [560] to the 
# dictionary of stocks.

stock_ticker=input("Enter a stock ticker: ")
stock_price=int(input("Enter the price of the stock: "))

if(stock_ticker in stock_info):
    stock_info[stock_ticker].append(stock_price)
else:
    stock_info[stock_ticker]=stock_price

