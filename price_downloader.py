import pandas as pd
import yfinance as yf

#output dataframe
outdf = pd.DataFrame()

#list of tickers input by user, empty
tickers = []

#how many times to ask
count = int(input("How many tickers will you be entering? "))

#populates list
for i in range(count):
    ticker = str(input("Enter a ticker: "))
    tickers.append(ticker)

#parameters for pulling data
start = str(input("Enter the start year: "))
end = str(input("Enter the end year: "))

#loop through every ticker in list
for j in tickers:
    #created for formatting
    lf = pd.DataFrame()
    for i in range(int(start),int(end)+1):
        #downloads data
        tf = yf.download(j, start=(str(i)+'-12-28'), end=str(i+1)+'-1-02', progress=False)
        #adds last trading day of the year to the dataframe
        lf = pd.concat([lf, tf.tail(1)])
    #concats last trading day of year price data to output dataframe so that each ticker gets
    #own column
    outdf = pd.concat([outdf,lf['Adj Close']], axis = 1)

#names a column after each ticker
outdf.columns=tickers
print("Task Completed")

#create csv file
outdf.to_csv('output.csv')

