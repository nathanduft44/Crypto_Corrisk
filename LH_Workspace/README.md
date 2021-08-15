# Crypto Corrisk

## Overview

Crypto currencies have recently been in the spotlight in today's financial world. We're seeing major adoption and capital investments pooring into the markets from financial institutions and retail investors all over the world. Since Bitcoin's creation in 2009, there are now a whopping 11,257 cryptocurrencies in the market!

We've chosen our top 10 coins to evaluate and provide historical price correlation in comparison to Bitcoin's. For this project, we've collected data for the time periods with the highest volatility; the start of the first bull run in 2016, to the current 2021 bull run.

* Bitcoin (BTC)
* Zcash (ZEC)
* Ethereum (ETH)
* Dash 
* XRP
* Siacoin (SC)
* Stellar Lumen (XLM)
* Tether (USDT)
* Lisk (LSK)
* Cardano (ADA)
* Doge Coin

## Objective
We want to create a bridge between legacy financial risk analysis with on-chain metrics. 
To reach our goal, we're creating a mechanism for our users to measure potential risk based off our techincal analysis.
This will allow users to make educated and well-informed decisions by evaluating historical price movements from the data provided in a user-friendly application.

## Requirements

## Navigating & How-to-Use

## Steps of Development
* 1. Using CoinGecko API, we were able to collect historical closing prices and compile them into one dataframe.
* 2. Calculated the variance and covariance of each coin compared to Bitcoin, finding the Beta.
* 3. Utilized heatmaps to visually compare the correlation of price movement for each coin.

## Findings
* Were the correlations between the top cryptocurrencies by market cap stronger or weaker during months of significant downward price movement? (look at 2017 and 2021 May specifically)
* Were there any unique correlation patterns in price movements depending on Market Cap (ie, large market cap, medium market cap, small market cap)
* How did trends in correlation change before and after major market bull runs
* How do the potential ranges of portfolio growth compare between [] via 10 year Monte carlo simulations

# Installation
    $ git clone git@github.com:nathanduft44/Crypto_Corrisk.git
    
    
# License
Licensed under the [MIT License] (LICENSE)
