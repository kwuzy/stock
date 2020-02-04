import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr

# get the stock
yf.pdr_override()
endDate = dt.datetime.now()
stock = input("Ticker Symbol: ")

#set a start date
start = input("Start Date: ")
if (start == ""):
    startYear = 2019
    startMonth = 1
    startDay = 1
    startDate = dt.datetime(startYear, startMonth, startDay)
else:
    splitYear = start.split('/')[2]
    splitMonth = start.split('/')[0]
    splitDay = start.split('/')[1]
    
    if (len(splitYear) == 2):
        splitYear = '20' + splitYear

    startYear = int(splitYear)
    startMonth = int(splitMonth)
    startDay = int(splitDay)
    startDate = dt.datetime(startYear, startMonth, startDay)

startExport = str(startMonth) + "." + str(startDay) + "." + str(startYear)
print(startDate)

#create the dataframe
df = pdr.get_data_yahoo(stock, startDate, endDate)

#print and export the data
print(df)
exportName = "C:\\Users\\kevin.wu\\Documents\\python\\exports\\" + stock + " " + startExport + ".xlsx"
print(exportName)
export_excel = df.to_excel(exportName)