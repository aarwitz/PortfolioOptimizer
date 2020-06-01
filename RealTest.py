#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test model in other period than modcel uses
"""

import numpy as np

from prints import print_realtest_results
from user import backtesting_details
from matrix_manip import calc_min_variance_portfolio, calc_portfolio_stdev
from plots import plot_points


def realtest(r,stds,mean_returns,covar,start2,end2,tickers):
    """
    Takes in 2d array of weights of all the calculated efficient portfolios,
    applies them to a set of different dates for purpose of testing predictability
    """
    
    # Get allocation weights of minimum variance portfolio for r during model time period
    weights = calc_min_variance_portfolio(mean_returns,covar,r)
    
    # Get data during backtesting time period
    from find_optimized_portfolio import process_data
    stds_new,mean_returns_new,covar_new,tickers,start2,end2=process_data(start2,end2,tickers)
    
    # Dot backtesting period's returns with model's weights to get the portfolio's return
    # during backtest period
    realtest_r = weights @ mean_returns_new
    # Get stdev during backtest period
    realtest_std=calc_portfolio_stdev(covar_new,weights)

    return realtest_r,realtest_std, weights, tickers, start2, end2


def realtest_frontier(stds,mean_returns,covar,start1,end1,tickers):
    # Interact with user to choose a predictability test region (dates) and a range of returns
    rs,start2,end2 = backtesting_details(start1,end1)
    count = len(rs)
    
    realtest_rs = np.zeros(count)
    realtest_stds = np.zeros(count)

    # gets min variance portfolio stats for list of desired returns, rs
    for i in range(count):
        realtest_r,realtest_std,weights,tickers,start2,end2=realtest(rs[i],stds,mean_returns,covar,start2,end2,tickers)
        print_realtest_results(realtest_r,realtest_std,rs[i],weights,tickers,start1,end1,start2,end2,i)
        # Input returns and stdevs of each portfolio into list
        realtest_rs[i]=realtest_r
        realtest_stds[i]=realtest_std
    
    # print and plot results of backtest
    plot_points(realtest_stds,realtest_rs,rs)
    

