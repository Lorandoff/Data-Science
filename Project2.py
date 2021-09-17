#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install yfinance')
get_ipython().system('pip install requests_cache')
import yfinance as yf
import requests_cache
import streamlit as st
session = requests_cache.CachedSession("yfinance.cache")
session.headers["User-agent"] = "my-program/1.0"
ticker = yf.Ticker("ATVI", session = session)
#display(ticker.options)
atvi = yf.Ticker("ATVI")
dataa = atvi.options
#display(dataa)
#display(atvi.options)
#display(list(atvi.option_chain("2021-08-20")))
dataa = pd.DataFrame()
dataa = dataa.append(atvi.option_chain("2021-08-20"))
#dataa.info()
#data["contractSymbol"] = data["contractSymbol"].astype("str").str.split(" ")

ticker = st.text_input("Ticker: ")
date = st.text_input("Дата('год-месяц-день'): ")
data = pd.DataFrame()
data = data.append(yf.Ticker(ticker).option_chain(date))
#display(data)
def category(row):
    if "C" in row:
        return "Calls"
    else: 
        return "Pulls"


data["contractSymbol"] = data["contractSymbol"].apply(category)
data_new = data[["contractSymbol","strike","lastPrice","volume","openInterest"]]
#display(data_new)
data_calls = data_new[data_new["contractSymbol"] == "Calls"]
#display(data_calls)
data_pulls = data_new[data_new["contractSymbol"] == "Pulls"]
#display(data_pulls)
data_full = data_calls.merge(data_pulls, on = "strike", how = "outer")
data_full = data_full.dropna()
data_full["умножение_x"] = data_full["volume_x"] * data_full["lastPrice_x"]
data_full["умножение_y"] = data_full["volume_y"] * data_full["lastPrice_y"]
data_full["difference_x"] = data_full["умножение_x"] - data_full["умножение_y"]
data_full["difference_op_vol"] = data_full["openInterest_y"] - data_full["openInterest_x"]
data_full = data_full.reindex(columns = ["difference_x","умножение_x","contractSymbol_x","lastPrice_x","volume_x","openInterest_x","strike","contractSymbol_y","lastPrice_y","volume_y","openInterest_y","умножение_y","difference_op_vol"])
display(data_full)

