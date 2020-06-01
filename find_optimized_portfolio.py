#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This program finds the efficient frontier according to Markowitz mean return-variance theory.
The portfolio can then be backtested in two ways: applying the model to other periods
and conducting Monte Carlo simulation

*** Call main to begin program
"""

from DF_helper import *
from prints import  *
from plots import *
from user import *
from RealTest import realtest_frontier
from MonteCarlo import MCStockSimulator

import matplotlib.pyplot as plt
import numpy as np


#### S&P performance from 2001-1-1 to 2020-5-1:
#### avg. daily return: .0288% ; standard dev. of daily returns: 1.255%


def main():
    """
    Begins program; runs primary functions
    """
    # initial ui
    start1,end1,tickers = get_portfolio_parameters()
    
    # returns data needed for analysis
    stds,mean_returns,covar,tickers,start1,end1=process_data(start1,end1,tickers)
    
    # find allocation weights and return of the minimum variance portfolio
    w_glob_min,r_glob_min = find_global_min(stds,mean_returns,covar)
    
    # print info about avg stats for tickers & min variance portfolio given those tickers
    print_glob_min_variance(w_glob_min,r_glob_min,tickers,mean_returns,covar,stds,start1,end1)
    
    # get the standard deviation, returns, and allocation weights of the minimum
    # variance portfolio for each return in rs
    range_rs=.001
    quantity_rs=40
    rs = np.linspace(r_glob_min-range_rs,r_glob_min+range_rs,quantity_rs)
    efficient_stds,efficient_weights = efficient_frontier(mean_returns,covar,rs)
    
    # plot frontier
    plot_efficient_frontier(efficient_stds,rs)
    
    # choose what to do next
    sequence(stds,mean_returns,covar,start1,end1,tickers)

    
    
def process_data(start1,end1,tickers):
    """
    Input start,end dates and tickers
    Returns standard dev, mean_returns, and covar
    """
    prices,ticker,start1,end1=get_prices(start1,end1,tickers)
    returns=get_returns(prices)
    stds=returns.std()
    mean_returns = np_take_mean_of_returns(returns)
    covar=covar_to_np(returns)
    return stds,mean_returns,covar,tickers,start1,end1
    

def find_global_min(stds,mean_returns,covar):
    """
    Input start,end,tickers, and a list of desired returns
    Returns the weights corresponding to the
    minimum variance portfolio, in matrix  format
    """
    
    #get array of weights for each ticker of min var portfolio
    w_glob_min = calc_global_min_variance_portfolio(covar)
    #dot weights with returns to get array of min var portfolio
    r_glob_min=np_calc_portfolio_return(mean_returns,w_glob_min)
    
    return w_glob_min,r_glob_min


def sequence(stds,mean_returns,covar,start1,end1,tickers):
    """
    Ask user whether to backtest or restart
    """
    next_step = backtest_or_restart()
    if next_step =='backtest':
        backtest(stds,mean_returns,covar,start1,end1,tickers)
    elif next_step == 'restart':
        main()
        
def backtest(stds,mean_returns,covar,start1,end1,tickers):
    next_next_step = simulate_or_reality()
    if next_next_step == 'simulate':
        pars = initialize_MCsimulation() # Get simulation parameters
        r,std,years,n = [float(x) for x in pars] # Cast from string to float
        sim = MCStockSimulator(years,r,std) # Creates a simulation class
        sim.plot_simulated_stock_values(int(n)) # Plot simulations
        sequence(stds,mean_returns,covar,start1,end1,tickers)
        
    elif next_next_step == 'real':
        # Plot curve in other period than used by model
        realtest_frontier(stds,mean_returns,covar,start1,end1,tickers)
        sequence(stds,mean_returns,covar,start1,end1,tickers)
        
        
