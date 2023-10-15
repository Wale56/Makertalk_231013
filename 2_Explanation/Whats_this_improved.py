import yfinance as yf
import pandas as pd
import streamlit as st
from pandas.tseries.offsets import DateOffset

# Read the tickerlist with full names
ticker_list = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
tickers = ticker_list.Symbol.to_list()
ticker_names = ticker_list.Security.to_list()

# Evaluate data df in the time spread n (months)
def get_ret(df, n):
    previous_prices = df[:df.index[-1] - DateOffset(months=n)].tail(1).squeeze()
    recent_prices = df.loc[df.index[-1]]
    ret_df = recent_prices / previous_prices - 1
    return previous_prices.name, ret_df

# Read the data only once!
@st.cache_data
def getdata():
    df = yf.download(tickers, start='2020-01-01')
    df = df['Close']
    return df

df = getdata()

st.title('Index component performance of the S&P500')

n = st.number_input('Please provide the performance horizon in months:', min_value=1, max_value=24)

date, ret_df = get_ret(df, n)
winners, losers = ret_df.nlargest(10), ret_df.nsmallest(10)
winners.name, losers.name = 'winners', 'losers'

# Map ticker symbols to ticker names
winners_names = [ticker_names[tickers.index(ticker)] for ticker in winners.index]
losers_names = [ticker_names[tickers.index(ticker)] for ticker in losers.index]

# Display tables with ticker names
st.table(pd.DataFrame({'Winners': winners_names, 'Returns': winners.values}))
st.table(pd.DataFrame({'Losers': losers_names, 'Returns': losers.values}))

winnerpick = st.selectbox('Pick a winner to visualize:', winners_names)
st.line_chart(df[winners.index[winners_names.index(winnerpick)]][date:])
loserpick = st.selectbox('Pick a loser to visualize:', losers_names)
st.line_chart(df[losers.index[losers_names.index(loserpick)]][date:])
