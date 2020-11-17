from USER import *
from ADVISOR import *
from ALLTD import *


currentUser = users()

print('''
                                    Welcome to the Chia Stock Advisor
                                    
                                    We currently have the following tools
                                                    Momentum
                                                    Correlation
                                                    Volatility
''')
watchlist = []

while True:
    ticker = input('Please continue to enter your tickers or hit enter to stop: ')
    if len(ticker) == 0:
        break
    else:
        watchlist.append(ticker)

tdInfo = tdAction()
quotes = tdInfo.quote(tickerList=watchlist)
historicalData = tdInfo.history(tickerList=watchlist)
print('\n')

userStrats = []

print('Please choose one or more strategies to get a report on or hit enter to stop')
while True:
    strat = input('Enter here: ')
    print('\n')

    if len(strat) > 0:
        userStrats.append(strat)
    else:
        break

adviseeData = advisor(dataset=historicalData, tickers=watchlist)

if 'momentum' in userStrats:
    userMomentum = adviseeData.momentum()
    print(userMomentum)
if 'correlation' in userStrats:
    userCorrelaiton = adviseeData.correlation()
if 'volatility' in userStrats:
    userVolatility = adviseeData.volatility()






