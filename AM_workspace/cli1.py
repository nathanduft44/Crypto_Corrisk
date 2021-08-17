import pandas as pd
import numpy as np
import csv
from pathlib import Path
import questionary


df_2017 = pd.read_csv(
    Path('2017_data.csv'),
)

final_2017_df = pd.DataFrame()
final_2017_df['BTC_Monthly_Close'] = df_2017['price_close']
final_2017_df['ETH_Monthly_Close'] = df_2017['price_close.1']
final_2017_df['ITC_Monthly_Close'] = df_2017['price_close.2']
final_2017_df['USDT_Monthly_Close'] = df_2017['price_close.3']
final_2017_df['XLM_Monthly_Close'] = df_2017['price_close.4']
final_2017_df['XRP_Monthly_Close'] = df_2017['price_close.5']
final_2017_df['ZEC_Monthly_Close'] = df_2017['price_close.6']
final_2017_df['DASH_Monthly_Close'] = df_2017['price_close.7']


monthly_2017_returns = pd.DataFrame()

monthly_2017_returns['BTC'] = final_2017_df['BTC_Monthly_Close'].pct_change().dropna()
monthly_2017_returns['ETH']= final_2017_df['ETH_Monthly_Close'].pct_change().dropna()
monthly_2017_returns['ITC'] = final_2017_df['ITC_Monthly_Close'].pct_change().dropna()
monthly_2017_returns['USDT'] = final_2017_df['USDT_Monthly_Close'].pct_change().dropna()
monthly_2017_returns['XLM'] = final_2017_df['XLM_Monthly_Close'].pct_change().dropna()
monthly_2017_returns['XRP'] = final_2017_df['XRP_Monthly_Close'].pct_change().dropna()
monthly_2017_returns['ZEC'] = final_2017_df['ZEC_Monthly_Close'].pct_change().dropna()
monthly_2017_returns['DASH'] = final_2017_df['DASH_Monthly_Close'].pct_change().dropna()

market_var_2017 = final_2017_df['BTC_Monthly_Close'].var()
market_cov_2017 = final_2017_df['BTC_Monthly_Close'].cov(final_2017_df['BTC_Monthly_Close'])

eth_cov_2017 = monthly_2017_returns['ETH'].cov(monthly_2017_returns['BTC'])
itc_cov_2017 = monthly_2017_returns['ITC'].cov(monthly_2017_returns['BTC'])
usdt_cov_2017 = monthly_2017_returns['USDT'].cov(monthly_2017_returns['BTC'])
xlm_cov_2017 = monthly_2017_returns['XLM'].cov(monthly_2017_returns['BTC'])
xrp_cov_2017 = monthly_2017_returns['XRP'].cov(monthly_2017_returns['BTC'])
zec_cov_2017 = monthly_2017_returns['ZEC'].cov(monthly_2017_returns['BTC'])
dash_cov_2017 = monthly_2017_returns['DASH'].cov(monthly_2017_returns['BTC'])

btc_beta_2017 = market_cov_2017 / market_var_2017
eth_beta_2017 = eth_cov_2017 / market_var_2017
itc_beta_2017 = itc_cov_2017 / market_var_2017
usdt_beta_2017 = usdt_cov_2017 / market_var_2017
xlm_beta_2017= xlm_cov_2017 / market_var_2017
xrp_beta_2017 = xrp_cov_2017 / market_var_2017
zec_beta_2017 = zec_cov_2017 / market_var_2017
dash_beta_2017 = dash_cov_2017 / market_var_2017

# ----------------------------------------------------------

df_2018 = pd.read_csv(
    Path('2018_data.csv'),
)

final_2018_df = pd.DataFrame()
final_2018_df['BTC_Monthly_Close'] = df_2018['price_close']
final_2018_df['ETH_Monthly_Close'] = df_2018['price_close.1']
final_2018_df['ITC_Monthly_Close'] = df_2018['price_close.2']
final_2018_df['USDT_Monthly_Close'] = df_2018['price_close.3']
final_2018_df['XLM_Monthly_Close'] = df_2018['price_close.4']
final_2018_df['XRP_Monthly_Close'] = df_2018['price_close.5']
final_2018_df['ZEC_Monthly_Close'] = df_2018['price_close.6']
final_2018_df['DASH_Monthly_Close'] = df_2018['price_close.7']
final_2018_df['ADA_Monthly_Close'] = df_2018['price_close.8']


monthly_2018_returns = pd.DataFrame()

monthly_2018_returns['BTC'] = final_2018_df['BTC_Monthly_Close'].pct_change().dropna()
monthly_2018_returns['ETH']= final_2018_df['ETH_Monthly_Close'].pct_change().dropna()
monthly_2018_returns['ITC'] = final_2018_df['ITC_Monthly_Close'].pct_change().dropna()
monthly_2018_returns['ADA'] = final_2018_df['ADA_Monthly_Close'].pct_change().dropna()
monthly_2018_returns['XLM'] = final_2018_df['XLM_Monthly_Close'].pct_change().dropna()
monthly_2018_returns['XRP'] = final_2018_df['XRP_Monthly_Close'].pct_change().dropna()
monthly_2018_returns['ZEC'] = final_2018_df['ZEC_Monthly_Close'].pct_change().dropna()
monthly_2018_returns['USDT'] = final_2018_df['USDT_Monthly_Close'].pct_change().dropna()
monthly_2018_returns['DASH'] = final_2018_df['DASH_Monthly_Close'].pct_change().dropna()

market_var_2018 = final_2018_df['BTC_Monthly_Close'].var()
market_cov_2018 = final_2018_df['BTC_Monthly_Close'].cov(final_2018_df['BTC_Monthly_Close'])

eth_cov_2018 = monthly_2018_returns['ETH'].cov(monthly_2018_returns['BTC'])
itc_cov_2018 = monthly_2018_returns['ITC'].cov(monthly_2018_returns['BTC'])
ada_cov_2018 = monthly_2018_returns['ADA'].cov(monthly_2018_returns['BTC'])
xlm_cov_2018 = monthly_2018_returns['XLM'].cov(monthly_2018_returns['BTC'])
xrp_cov_2018 = monthly_2018_returns['XRP'].cov(monthly_2018_returns['BTC'])
zec_cov_2018 = monthly_2018_returns['ZEC'].cov(monthly_2018_returns['BTC'])
usdt_cov_2018 = monthly_2018_returns['USDT'].cov(monthly_2018_returns['BTC'])
dash_cov_2018 = monthly_2018_returns['DASH'].cov(monthly_2018_returns['BTC'])

btc_beta_2018 = market_cov_2018 / market_var_2018
eth_beta_2018 = eth_cov_2018 / market_var_2018
itc_beta_2018 = itc_cov_2018 / market_var_2018
ada_beta_2018 = ada_cov_2018 / market_var_2018
xlm_beta_2018= xlm_cov_2018 / market_var_2018
xrp_beta_2018 = xrp_cov_2018 / market_var_2018
zec_beta_2018 = zec_cov_2018 / market_var_2018
usdt_beta_2018 = usdt_cov_2018 / market_var_2018
dash_beta_2018 = dash_cov_2018 / market_var_2018








# ---------------------------------------------------------------------------
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


market_var_2019 = btc_2019_df.var()
btc_var_2019 = btc_2019_df.var()
eth_var_2019 = eth_2019_df.var()
ltc_var_2019 = ltc_2019_df.var()
ada_var_2019 = ada_2019_df.var()
xlm_var_2019 = xlm_2019_df.var()
xrp_var_2019 = xrp_2019_df.var()
lisk_var_2019 = lisk_2019_df.var()
waves_var_2019 = waves_2019_df.var()
zec_var_2019 = zec_2019_df.var()
sc_var_2019 = sc_2019_df.var()
usdt_var_2019 = usdt_2019_df.var()
dash_var_2019 = dash_2019_df.var()
doge_var_2019 = doge_2019_df.var()

monthly_returns = final_2019_df.pct_change().fillna(0)

market_cov_2019 = monthly_returns['BTC_Monthly_Close'].cov(monthly_returns['BTC_Monthly_Close'])
eth_cov_2019 = monthly_returns['ETH_Monthly_Close'].cov(monthly_returns['BTC_Monthly_Close'])
ltc_cov_2019 = monthly_returns['LTC_Monthly_Close'].cov(monthly_returns['BTC_Monthly_Close'])
ada_cov_2019 = monthly_returns['ADA_Monthly_Close'].cov(monthly_returns['BTC_Monthly_Close'])
xlm_cov_2019 = monthly_returns['XLM_Monthly_Close'].cov(monthly_returns['BTC_Monthly_Close'])
xrp_cov_2019 = monthly_returns['XRP_Monthly_Close'].cov(monthly_returns['BTC_Monthly_Close'])
lisk_cov_2019 = monthly_returns['LISK_Monthly_Close'].cov(monthly_returns['BTC_Monthly_Close'])
waves_cov_2019 = monthly_returns['WAVES_Monthly_Close'].cov(monthly_returns['BTC_Monthly_Close'])
zec_cov_2019 = monthly_returns['ZEC_Monthly_Close'].cov(monthly_returns['BTC_Monthly_Close'])
sc_cov_2019 = monthly_returns['SC_Monthly_Close'].cov(monthly_returns['BTC_Monthly_Close'])
usdt_cov_2019 = monthly_returns['USDT_Monthly_Close'].cov(monthly_returns['BTC_Monthly_Close'])
dash_cov_2019 = monthly_returns['DASH_Monthly_Close'].cov(monthly_returns['BTC_Monthly_Close'])
doge_cov_2019 = monthly_returns['DOGE_Monthly_Close'].cov(monthly_returns['BTC_Monthly_Close'])

btc_beta_2019 = market_cov_2019 / market_var_2019
eth_beta_2019 = eth_cov_2019 / market_var_2019
ltc_beta_2019 = ltc_cov_2019 / market_var_2019
ada_beta_2019 = ada_cov_2019 / market_var_2019
xlm_beta_2019 = xlm_cov_2019 / market_var_2019
xrp_beta_2019 = xrp_cov_2019/ market_var_2019
lisk_beta_2019 = lisk_cov_2019 / market_var_2019
waves_beta_2019 = lisk_cov_2019/ market_var_2019
zec_beta_2019= zec_cov_2019 / market_var_2019
sc_beta_2019 = sc_cov_2019 / market_var_2019
usdt_beta_2019 = usdt_cov_2019 / market_var_2019
dash_beta_2019 = dash_cov_2019 / market_var_2019
doge_beta_2019 = doge_cov_2019 / market_var_2019

# --------------------------------------------------------------------------
df_2020 = pd.read_csv(
    Path('2020_sheet.csv'),
)

final_2020_df = pd.DataFrame()
final_2020_df['BTC_Monthly_Close'] = df_2020['price_close_BTC']
final_2020_df['ETH_Monthly_Close'] = df_2020['price_close_ETH']
final_2020_df['ITC_Monthly_Close'] = df_2020['price_close_ITC']
final_2020_df['ADA_Monthly_Close'] = df_2020['price_close_ADA']
final_2020_df['DOGE_Monthly_Close'] = df_2020['price_close_DOGE']
final_2020_df['XLM_Monthly_Close'] = df_2020['price_close_XLM']
final_2020_df['XRP_Monthly_Close'] = df_2020['price_close_XRP']
final_2020_df['LISK_Monthly_Close'] = df_2020['price_close_LISK']
final_2020_df['ZEC_Monthly_Close'] = df_2020['price_close_ZEC']
final_2020_df['SC_Monthly_Close'] = df_2020['price_close_SC']
final_2020_df['USDT_Monthly_Close'] = df_2020['price_close_USDT']
final_2020_df['DASH_Monthly_Close'] = df_2020['price_close_DASH']

monthly_2020_returns = pd.DataFrame()

monthly_2020_returns['BTC'] = final_2020_df['BTC_Monthly_Close'].pct_change().dropna()
monthly_2020_returns['ETH']= final_2020_df['ETH_Monthly_Close'].pct_change().dropna()
monthly_2020_returns['ITC'] = final_2020_df['ITC_Monthly_Close'].pct_change().dropna()
monthly_2020_returns['ADA'] = final_2020_df['ADA_Monthly_Close'].pct_change().dropna()
monthly_2020_returns['DOGE'] = final_2020_df['DOGE_Monthly_Close'].pct_change().dropna()
monthly_2020_returns['XLM'] = final_2020_df['XLM_Monthly_Close'].pct_change().dropna()
monthly_2020_returns['XRP'] = final_2020_df['XRP_Monthly_Close'].pct_change().dropna()
monthly_2020_returns['LISK'] = final_2020_df['LISK_Monthly_Close'].pct_change().dropna()
monthly_2020_returns['ZEC'] = final_2020_df['ZEC_Monthly_Close'].pct_change().dropna()
monthly_2020_returns['SC'] = final_2020_df['SC_Monthly_Close'].pct_change().dropna()
monthly_2020_returns['USDT'] = final_2020_df['USDT_Monthly_Close'].pct_change().dropna()
monthly_2020_returns['DASH'] = final_2020_df['DASH_Monthly_Close'].pct_change().dropna()

market_var_2020 = final_2020_df['BTC_Monthly_Close'].var()
market_cov_2020 = final_2020_df['BTC_Monthly_Close'].cov(final_2020_df['BTC_Monthly_Close'])

eth_cov_2020 = monthly_2020_returns['ETH'].cov(monthly_2020_returns['BTC'])
itc_cov_2020 = monthly_2020_returns['ITC'].cov(monthly_2020_returns['BTC'])
ada_cov_2020 = monthly_2020_returns['ADA'].cov(monthly_2020_returns['BTC'])
doge_cov_2020 = monthly_2020_returns['DOGE'].cov(monthly_2020_returns['BTC'])
xlm_cov_2020 = monthly_2020_returns['XLM'].cov(monthly_2020_returns['BTC'])
xrp_cov_2020 = monthly_2020_returns['XRP'].cov(monthly_2020_returns['BTC'])
lisk_cov_2020 = monthly_2020_returns['LISK'].cov(monthly_2020_returns['BTC'])
zec_cov_2020 = monthly_2020_returns['ZEC'].cov(monthly_2020_returns['BTC'])
sc_cov_2020 = monthly_2020_returns['SC'].cov(monthly_2020_returns['BTC'])
usdt_cov_2020 = monthly_2020_returns['USDT'].cov(monthly_2020_returns['BTC'])
dash_cov_2020 = monthly_2020_returns['DASH'].cov(monthly_2020_returns['BTC'])

btc_beta_2020 = market_cov_2020 / market_var_2020
eth_beta_2020 = eth_cov_2020 / market_var_2020
itc_beta_2020 = itc_cov_2020 / market_var_2020
ada_beta_2020 = ada_cov_2020 / market_var_2020
doge_beta_2020 = doge_cov_2020 / market_var_2020
xlm_beta_2020 = xlm_cov_2020 / market_var_2020
xrp_beta_2020 = xrp_cov_2020 / market_var_2020
lisk_beta_2020 = lisk_cov_2020 / market_var_2020
zec_beta_2020 = zec_cov_2020 / market_var_2020
sc_beta_2020 = sc_cov_2020 / market_var_2020
usdt_beta_2020 = usdt_cov_2020 / market_var_2020
dash_beta_2020 = dash_cov_2020 / market_var_2020
# -----------------------------------------------------



choice = questionary.select("choose the year:", choices=["2017","2018","2019","2020"]).ask()
if choice =="2019":    
    choice_2019 = questionary.select("choose the coin:", choices=('market_var','btc','eth','ltc', 'ada','xrp','xlm','lisk','waves','zec','sc','usdt','dash','doge')).ask()
    if choice_2019== 'market_var':
        print(f"Market varianve is:{market_var_2019}")
    elif choice_2019 == "btc" :
         print(f"BTC covariance and beta are:{market_cov_2019,btc_beta_2019}")
    elif choice_2019 == "eth":
         print(f"ETH covariance and beta are:{eth_cov_2019,eth_beta_2019}")    
    elif choice_2019 == "ltc":
         print(f"LTC covariance and beta are:{ltc_cov_2019,ltc_beta_2019}")
    elif choice_2019 == "ada":
         print(f"ADA covariance and beta are:{ada_cov_2019,ada_beta_2019}")        
    elif choice_2019 == "xrp":
         print(f"XRP covariance and beta are:{xrp_cov_2019,xrp_beta_2019}")
    elif choice_2019 == "xlm":
         print(f"XLM covariance and beta are:{xlm_cov_2019,xlm_beta_2019}")
    elif choice_2019 == "lisk":
         print(f"LISK covariance and beta are:{lisk_cov_2019,lisk_beta_2019}")
    elif choice_2019 == "waves":
         print(f"WAVES covariance and beta are:{waves_cov_2019,waves_beta_2019}")
    elif choice_2019 == "zec":
         print(f"ZEC covariance and beta are:{zec_cov_2019,zec_beta_2020}")
    elif choice_2019 == "sc":
         print(f"SC covariance and beta are:{sc_cov_2019,sc_beta_2019}")
    elif choice_2019 == "usdt":
         print(f"USDT covariance and beta are:{usdt_cov_2019,usdt_beta_2019}")    
    elif choice_2019 == "dash":
         print(f"DASH covariance and beta are:{dash_cov_2019,dash_beta_2019}")  
    elif choice_2019 == "doge":
         print(f"DOGE covariance and beta are:{doge_cov_2019,dash_beta_2019}")
#------------------------------------------------------------  
elif choice == "2020":
    choice_2020 = questionary.select("choose the coin:", choices=('market_var','btc','eth','ltc', 'ada','xrp','xlm','lisk','zec','sc','usdt','dash','doge')).ask()

    if choice_2020== 'market_var':
          print(market_var_2020)
    elif choice_2020 == "btc" :
          print(f"BTC covariance and beta are :{market_cov_2020,btc_beta_2020}")
    elif choice_2020 == "eth":
          print(f"ETH covariance and beta are:{eth_cov_2020,eth_beta_2020}")    
    elif choice_2020 == "ltc":
          print(f"LTC covariance and beta are:{itc_cov_2020,itc_beta_2020}")
    elif choice_2020 == "ada":
          print(f"ADA covariance and beta are:{ada_cov_2020,ada_beta_2020}")        
    elif choice_2020 == "xrp":
          print(f"XRP covariance and beta are:{xrp_cov_2020,xrp_beta_2020}")
    elif choice_2020 == "xlm":
          print(f"XLM covariance and beta are:{xlm_cov_2020,xlm_beta_2020}")
    elif choice_2020 == "lisk":
          print(f"LISK covariance and beta are:{lisk_cov_2020,lisk_beta_2020}")
    elif choice_2020 == "zec":
          print(f"ZEC covariance and beta are:{zec_cov_2020,zec_beta_2020}")
    elif choice_2020 == "sc":
          print(f"SC covariance and beta are:{sc_cov_2020,sc_beta_2020}")
    elif choice_2020 == "usdt":
          print(f"USDT covariance and beta are:{usdt_cov_2020,usdt_beta_2020}")    
    elif choice_2020 == "dash":
          print(f"DASH covariance and beta are:{dash_cov_2020,dash_beta_2020}")  
    elif choice_2020 == "doge":
          print(f"DOGE covariance and beta are:{doge_cov_2020,dash_beta_2020}")   

# --------------------------------------

elif choice == "2018":
     choice_2018 = questionary.select("choose the coin:", choices=('market_var','btc','eth','ltc', 'ada','xrp','xlm','zec','usdt','dash')).ask()

     if choice_2018== 'market_var':
        print(market_var_2019)
     elif choice_2018 == "btc" :
         print(f"BTC covariance and beta are: {market_cov_2018,btc_beta_2018}")
     elif choice_2018 == "eth":
         print(f"ETH covariance and beta are:{eth_cov_2018,eth_beta_2018}")    
     elif choice_2018 == "ltc":
         print(f"LTC covariance and beta are:{itc_cov_2018,itc_beta_2018}")
     elif choice_2018 == "ada":
         print(f"ADA covariance and beta are:{ada_cov_2018,ada_beta_2018}")        
     elif choice_2018 == "xrp":
         print(f"XRP covariance and beta are:{xrp_cov_2018,xrp_beta_2018}")
     elif choice_2018 == "xlm":
         print(f"XLM covariance and beta are:{xlm_cov_2018,xlm_beta_2018}")
     elif choice_2018 == "zec":
         print(f"ZEC covariance and beta are:{zec_cov_2018,zec_beta_2018}")
     elif choice_2018 == "usdt":
         print(f"USDT covariance and beta are:{usdt_cov_2018,usdt_beta_2018}")    
     elif choice_2018 == "dash":
         print(f"DASH covariance and beta are:{dash_cov_2018,dash_beta_2018}")  
#------------------------------------------------------------  

elif choice == "2017":
     choice_2017 = questionary.select("choose the coin:", choices=('market_var','btc','eth','ltc','xrp','xlm','zec','usdt','dash')).ask()

     if choice_2017== 'market_var':
        print(market_var_2017)
     elif choice_2017 == "btc" :
         print(f"BTC covariance and beta are: {market_cov_2017,btc_beta_2017}")
     elif choice_2017 == "eth":
         print(f"ETH covariance and beta are:{eth_cov_2017,eth_beta_2017}")    
     elif choice_2017 == "ltc":
         print(f"LTC covariance and beta are:{itc_cov_2017,itc_beta_2017}")
     elif choice_2017 == "xrp":
         print(f"XRP covariance and beta are:{xrp_cov_2017,xrp_beta_2017}")
     elif choice_2017 == "xlm":
         print(f"XLM covariance and beta are:{xlm_cov_2017,xlm_beta_2017}")
     elif choice_2017 == "zec":
         print(f"ZEC covariance and beta are:{zec_cov_2017,zec_beta_2017}")
     elif choice_2017 == "usdt":
         print(f"USDT covariance and beta are:{usdt_cov_2017,usdt_beta_2017}")    
     elif choice_2017 == "dash":
         print(f"DASH covariance and beta are:{dash_cov_2017,dash_beta_2017}")