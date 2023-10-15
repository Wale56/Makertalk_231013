#!/usr/bin/env python
# coding: utf-8
# https://www.youtube.com/watch?v=e4wIdB1gkS4&t=183s

# Für diese Demo wird das Streamlit Framework verwendet:
# https://streamlit.io/

import yfinance as yf
import pandas as pd
import streamlit as st
from pandas.tseries.offsets import DateOffset


# Evaluate data df in the time spread n (months)
def get_ret(df, n):
    previous_prices = df[:df.index[-1] -
                          DateOffset(months=n)].tail(1).squeeze()
    recent_prices = df.loc[df.index[-1]]
    ret_df = recent_prices / previous_prices - 1
    return previous_prices.name, ret_df


# Read the tickerlist
tickers = pd.read_html('https://en.wikipedia.org/wiki/'
                       'List_of_S%26P_500_companies')[0].Symbol
tickers = tickers.to_list()


# Read the data only once!
@st.cache_data
def getdata():
    df = yf.download(tickers, start='2020-01-01')
    df = df['Close']
    return df


df = getdata()

st.title('Index component performance of the S&P500')
# st.title('How cool ist that!?')

n = st.number_input('Please provide the performance horizon in months:',
                    min_value=1, max_value=24)

date, ret_df = get_ret(df, n)
winners, losers = ret_df.nlargest(10), ret_df.nsmallest(10)
winners.name, losers.name = 'winners', 'losers'

st.table(winners)
st.table(losers)

winnerpick = st.selectbox('Pick a winner to visualize:', winners.index)
st.line_chart(df[winnerpick][date:])
loserpick = st.selectbox('Pick a loser to visualize:', losers.index)
st.line_chart(df[loserpick][date:])

