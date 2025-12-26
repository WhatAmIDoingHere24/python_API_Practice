import yfinance as yf
import matplotlib.pyplot as plot
import numpy as np
import pandas as pd

time_interval = ["1mo","1yr"]
stock_time = ["Open","Close"]

wb_bun = yf.Ticker("FLO") #wonder bread
bb_bun = yf.Ticker("GRBMF") #bimbo bakeries
pf_bun = yf.Ticker("CPB") #pepridge farm, owned by cambell soup company

om_dog = yf.Ticker("KHC") #oscar myers, owned by kraft heinz company
kl_dog = yf.Ticker("TBHC") #kirkland

wb_bun_history = wb_bun.history(period=time_interval[0])
bb_bun_history = bb_bun.history(period=time_interval[0])
pf_bun_history = pf_bun.history(period=time_interval[0])

om_dog_history = om_dog.history(period=time_interval[0])
kl_dog_history = kl_dog.history(period=time_interval[0])

wb_bun_history_array = wb_bun_history[stock_time[0]].to_numpy()
bb_bun_history_array = bb_bun_history[stock_time[0]].to_numpy()
pf_bun_history_array = pf_bun_history[stock_time[0]].to_numpy()

om_dog_history_array = om_dog_history[stock_time[0]].to_numpy()                                                       
kl_dog_history_array = kl_dog_history[stock_time[0]].to_numpy()

bun_avg_array = (wb_bun_history_array + bb_bun_history_array + pf_bun_history_array)
dog_avg_array = (om_dog_history_array + kl_dog_history_array)

fig, ax = plot.subplots()

ax.scatter(
    [bun_avg_array],
    [dog_avg_array]
)

ax.set_xlabel("Stock price of buns")
ax.set_ylabel("Stock price of hotdogs")

plot.show()                           
