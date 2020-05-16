#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This program finds the efficient frontier according to Markowitz mean return-variance theory.
The portfolio is then backtesed by testing it on random dates, and evaluating its performance

Call main to begin program
"""

from DF_helper import *
from prints import  *
from plots import *
from user import *

import matplotlib.pyplot as plt
import numpy as np

def main():
    """
    Begin program
    """
    start1,end1,tickers = get_portfolio_parameters()
    
    optimal_portfolios = find_optimal_portfolios(start1,end1,tickers)
    
    # Ask user whether to backtest or restart
    next_step = backtest_or_restart()
    if next_step =='backtest':
        backtest(start1,end1,tickers)
    elif next_step == 'restart':
        main()
    
def find_optimal_portfolios(start1,end1,tickers):
    """
    Input start,end,tickers, and a list of desired returns
    Returns the weights corresponding to the
    minimum variance portfolio, in matrix format
    """
    prices=get_prices(start1,end1,tickers)
    returns=get_returns(prices)
    stds=returns.std()
    mean_returns = np_take_mean_of_returns(returns)
    covar=covar_to_np(returns)

    #get array of weights for each ticker of min var portfolio
    w_glob_min = calc_global_min_variance_portfolio(covar)
    #dot weights with returns to get array of min var portfolio
    r_glob_min=np_calc_portfolio_return(mean_returns,w_glob_min)
    
    #print 
    print_glob_min_variance(w_glob_min,r_glob_min,tickers,mean_returns,covar,stds,start1,end1)

    # define a list of returns to find minimumn stdev for
    range_rs=.001
    quantity_rs=40
    rs = np.linspace(r_glob_min-range_rs,r_glob_min+range_rs,quantity_rs)
    
    # get the standard deviation, returns, and allocation weights of the minimum
    # variance portfolio for each return in rs
    sigmas,weights,returns = calc_efficient_portfolios(mean_returns,covar,rs)
    
    plot_efficient_frontier(sigmas,returns)
    
    
    
def backtest(start1,end1,tickers):
    """
    Takes in 2d array of weights of all the calculated efficient portfolios,
    applies them to a set of different dates for purpose of testing predictability
    """
    # interact with user to choose a predictability test region (dates) and a return value (for purpose of choosing allocations)
    desired_return,start2,end2=backtesting_details(start1,end1)
    
    prices=get_prices(start1,end1,tickers)
    returns=get_returns(prices)
    covar=covar_to_np(returns)
    mean_returns=np_take_mean_of_returns(returns)
    
    st,weights,rett = calc_efficient_portfolios(mean_returns,covar,[desired_return])
    
    # Get returns for second time period
    prices=get_prices(start2,end2,tickers)
    returns=get_returns(prices)
    covar=covar_to_np(returns)
    mean_returns=np_take_mean_of_returns(returns)
    
    # Dot returns with weights, get stdev
    r = weights @ mean_returns
    s=calc_portfolio_stdev(covar,weights)
    
    print('Allocations of optimal portfolio that returns %.2f%% daily from %s to %s:'%(desired_return*100,start1,end1))
    print_allocations(weights[0],tickers)
    print('\nThat portfolio performs as follows from %s to %s:'%(start2,end2))
    print('Return: ' + '{0:.{1}f}'.format((r[0]*100),4) + '%')
    print('Standard deviation: ' + '{0:.{1}f}'.format((s[0][0]*100),4) + '%')
    
    if r[0]>desired_return:
        print('\nPortfolio had higher returns than the model predicts')
    elif r[0]<desired_return:
        print('\nPortfolio had lower returns than the model predicts')
    else:
        print('\nThe portfolio performed as predicts')
    
    # asks if user wants to test model in another period
    new = exit_or_cont()
    if new:
        backtest(start1,end1,tickers)
    
    
