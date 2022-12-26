import vectorbt as vbt
import streamlit as st
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import yfinance as yf
import plotly.graph_objs as go

st.title('WebApp to make estrategy backtest trading!')

@st.cache
