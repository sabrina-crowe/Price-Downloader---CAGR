## Price Downloader -- CAGR
Simple program to download prices and output .csv file containing price data from last trading day of each year for desired tickers. 
This program was created for personal use to make calculating CAGR in Excel more efficient. Plans include making it more user-friendly and incorporating a GUI.

### UPDATE 2/14:
There is now a gui! The zip file can be downloaded [here](https://drive.google.com/file/d/1li8405Z5KHfaWGrTXwWrun2BqabAyK1a/view?usp=sharing)
(Yes it's a little large. It has all my libraries included -- I will figure out the dependencies to reduce the size later)

The interface and instructions should be fairly intuitive. Enjoy!

### Use

The program will ask you how many tickers you are interested in. Enter an integer.
You will be asked to enter each ticker one at a time, then asked to provide a start and end year. Make sure the ticker has price data within those years.
Once done, a .csv file named 'output' will be written to the program's working directory.

### Packages

pandas and yfinance are used in this program.
