import pandas as pd
import numpy as np
import csv
from pathlib import Path
import questionary

df_2019 = pd.read_csv(
    Path('2019_data.csv')
).set_index('Month')

final_2019_df = pd.DataFrame()
final_2019_df['BTC_Monthly_Close'] = df_2019['price_close']
final_2019_df['ETH_Monthly_Close'] = df_2019['price_close.1']
final_2019_df['LTC_Monthly_Close'] = df_2019['price_close.2']
final_2019_df['ADA_Monthly_Close'] = df_2019['price_close.3']
final_2019_df['XLM_Monthly_Close'] = df_2019['price_close.4']
final_2019_df['XRP_Monthly_Close'] = df_2019['price_close.5']
final_2019_df['LISK_Monthly_Close'] = df_2019['price_close.6']
final_2019_df['WAVES_Monthly_Close'] = df_2019['price_close.7']
final_2019_df['ZEC_Monthly_Close'] = df_2019['price_close.8']
final_2019_df['SC_Monthly_Close'] = df_2019['price_close.9']
final_2019_df['USDT_Monthly_Close'] = df_2019['price_close.10']
final_2019_df['DASH_Monthly_Close'] = df_2019['price_close.11']
final_2019_df['DOGE_Monthly_Close'] = df_2019['price_close.12']

btc_2019_df = final_2019_df['BTC_Monthly_Close'].pct_change().fillna(0)
eth_2019_df = final_2019_df['ETH_Monthly_Close'].pct_change().fillna(0)
ltc_2019_df = final_2019_df['LTC_Monthly_Close'].pct_change().fillna(0)
ada_2019_df = final_2019_df['ADA_Monthly_Close'].pct_change().fillna(0)
xlm_2019_df = final_2019_df['XLM_Monthly_Close'].pct_change().fillna(0)
xrp_2019_df = final_2019_df['XRP_Monthly_Close'].pct_change().fillna(0)
lisk_2019_df = final_2019_df['LISK_Monthly_Close'].drop(
    labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October']).pct_change().fillna(0)
waves_2019_df = final_2019_df['WAVES_Monthly_Close'].drop(
    labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September']).pct_change().fillna(0)
sc_2019_df = final_2019_df['SC_Monthly_Close'].drop(
    labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September']).pct_change().fillna(0)
zec_2019_df = final_2019_df['ZEC_Monthly_Close'].pct_change().fillna(0)
usdt_2019_df = final_2019_df['USDT_Monthly_Close'].pct_change().fillna(0)
dash_2019_df = final_2019_df['DASH_Monthly_Close'].pct_change().fillna(0)
doge_2019_df = final_2019_df['BTC_Monthly_Close'].pct_change().fillna(0)


market_var = btc_2019_df.var()
btc_var = btc_2019_df.var()
eth_var = eth_2019_df.var()
ltc_var = ltc_2019_df.var()
ada_var = ada_2019_df.var()
xlm_var = xlm_2019_df.var()
xrp_var = xrp_2019_df.var()
lisk_var = lisk_2019_df.var()
waves_var = waves_2019_df.var()
zec_var = zec_2019_df.var()
sc_var = sc_2019_df.var()
usdt_var = usdt_2019_df.var()
dash_var = dash_2019_df.var()
doge_var = doge_2019_df.var()


choice = questionary.select("choose:", choices=('market_var','btc_var','eth_var','ltc_var', 'ada_var','xrp_var','xlm_var','lisk_var','waves_var','zec_var','sc_var','usdt_var','dash_var','doge_var')).ask()

print(f"your var is:{choice}")

if choice == 'market_var':
    print(market_var)
elif choice == "btc_var" :
    print(btc_var)
elif choice == "eth_var":
    print(eth_var)    
elif choice == "ltc_var":
    print(ltc_var)
elif choice == "ada_var":
    print(ada_var)        
elif choice == "xrp_var":
    print(xrp_var)
elif choice == "xlm_var":
    print(xlm_var)
elif choice == "lisk_var":
    print(lisk_var)
elif choice == "waves_var":
    print(waves_var)
elif choice == "zec_var":
    print(zec_var)
elif choice == "sc_var":
    print(sc_var)
elif choice == "usdt_var":
    print(usdt_var)    
elif choice == "dash_var":
    print(dash_var)  
elif choice == "doge_var":
    print(doge_var)      

