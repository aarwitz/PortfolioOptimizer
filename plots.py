#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 18:54:16 2019

@author: aaronhorwin
"""

import matplotlib.pyplot as plt
from matplotlib.pyplot import show

def plot_efficient_frontier(sigmas,returns):
    """
    Plots the efficient frontier of inputted tickers
    x-axis is standard deviation of portfolio
    y-axis is mean return of portfolio
    """

    #format numbers to display on axes
    returns = [x * 100 for x in returns]
    sigmas = [x * 100 for x in sigmas]
    
    
    plt.plot(sigmas,returns)
    plt.title('Efficient Frontier')
    plt.ylabel('Portfolio Expected Daily Return (%)')
    plt.xlabel('Portfolio Standard Deviation (%)')
    plt.show
    show(block=False)
    

def plot_frontiers(sigmas,returns,future_returns,future_sigmas):
    """
    Takes the list of points on the efficient frontier, and
    plots them into the future
    """
    
    
    for x in range(len(returns)):
        sigmas[x]=format_percentage(sigmas[x])
        returns[x]=format_percentage(returns[x])
        future_sigmas[x]=format_percentage(future_sigmas[x])
        future_returns[x]=format_percentage(future_returns[x])
    
    plt.subplot(211)
    plt.scatter(sigmas,returns)
    plt.xlabel("Standard Deviation (%)")
    plt.ylabel("Return (%)")
    plt.title('Training data: ' + start1+'-' + end1+', Applied to: ' +start2+'-'+end2)
    
    plt.subplot(212)
    plt.scatter(future_sigmas,future_returns)
    
    plt.xlabel("Standard Deviation (%)")
    plt.ylabel("Return (%)")



#
#def plot_efficient_frontier(covar,mean_returns,w_glob_min,r_glob_min):
#    """
#    Plots the efficient frontier of inputted stocks
#    """
#            
#    
#    # define a list of returns to find minimum sigma for
#    rs = np.linspace(r_glob_min-.0005,r_glob_min+.0005,10)
#    
#    # find the minimum standard deviation for each r in rs
##    portfolios=calc_efficient_portfolios(mean_returns,covar,rs)
#
#    sigmas,weights,returns = calc_efficient_portfolios(mean_returns,covar,rs)
#
#
#    # format rs and sigmas as dataframes for purpose of plotting
##    df_sigmas=pd.DataFrame(sigmas.T)
##    df_rs=pd.DataFrame(rs)
#
#    #plot    
#    plt.plot(sigmas,rs)
#    plt.title('Efficient Frontier')
#    plt.ylabel('Portfolio Expected Return (%)')
#    plt.xlabel('Portfolio Standard Deviation (%)')
#    plt.show
#    
#    return weights
