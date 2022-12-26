import vectorbt as vbt
import streamlit as st
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import yfinance as yf
import plotly.graph_objs as go
import time
from datetime import date, datetime

st.title('WebApp to make estrategy backtest trading!')

ticker = st.text_input('Enter the ticker symbol of the stock you want to backtest')
periodo = st.date_input('Periodo', date(2022, 1, 1), min_value=date(2000, 1, 1), max_value=datetime.now())
interval = st.selectbox('Intervalo', ['1m', '2m', '5m', '15m', '30m','1h', '2h', '4h', '6h', '8h', '12h', '1d','2d' ,'3d', '1wk', '1mo','3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'])

if st.button('Get Data'):
    st.write('Getting data...')
    data = vbt.YFData.download(ticker, periodo, interval=interval).get()
    st.write('Data downloaded!')
    st.write(data)
    prices = data['Close']
    volume = data['Volume']



Indicators = st.selectbox('Indicadores', ['MACD', 'RSI', 'Stochastic', 'MA'])
mr = st.slider('Media Rapida', 0, 200, 50)
ml = st.slider('Media Lenta', 0, 200, 50)

media_rapida = vbt.Indicators.run(prices, mr)
media_lenta = vbt.Indicators.run(prices, ml)

lower = Indicators.lower()
#entrada = media_rapida.{lower}_above(media_lenta)
#saida = media_rapida.{lower}_below(media_lenta)

#pf_macd = vbt.Portfolio.from_signals(prices, entrada, saida)
