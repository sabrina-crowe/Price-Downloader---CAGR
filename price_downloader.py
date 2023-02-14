import pandas as pd
import yfinance as yf

#activates the code upon button press
def download():
    #takes in the user input string of stocks
    tickerString = entry1.get()
    #splits them by comma, each ticker is a element in the list
    tickers = tickerString.split(", ")
    downloader(tickers)
    #tells the user when the task has been completed. This can get a little goofy if the program is used multiple times
    T.insert(tk.END, "Prices Downloaded!")

def downloader(tickers):
    #empty output dataframe
    outdf = pd.DataFrame()
    #pull start and end years
    start = entry2.get()
    end = entry3.get()
    #loop through list
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
    #create csv file
    name = entry4.get()
    outdf.to_csv(name+'.csv')

#GUI
import tkinter as tk

root = tk.Tk()
root.title("Stock Price Downloader")

label1 = tk.Label(root, text="Enter your tickers in a comma separated list:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter your start year:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

label3 = tk.Label(root, text="Enter your end year:")
label3.pack()
entry3 = tk.Entry(root)
entry3.pack()

label4 = tk.Label(root, text="Enter your file name:")
label4.pack()
entry4 = tk.Entry(root)
entry4.pack()

button = tk.Button(root, text="Download Data", command=download)
button.pack()

T = tk.Text(root, height=5, width=52)
T.pack()

label5 = tk.Label(root, text="Made with love, for Diddy")
label5.pack()

root.mainloop()
