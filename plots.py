#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plot stuff
"""

import matplotlib.pyplot as plt
from matplotlib.pyplot import show

def plot_efficient_frontier(stds,returns):
    """
    Plots the efficient frontier of inputted tickers
    x-axis is standard deviation of portfolio
    y-axis is mean return of portfolio
    """

    #format numbers to display on axes
    returns = [x * 100 for x in returns]
    sigmas = [x * 100 for x in stds]
    
    
    plt.plot(sigmas,returns)
    plt.title('Efficient Frontier')
    plt.ylabel('Portfolio Expected Daily Return (%)')
    plt.xlabel('Portfolio Standard Deviation (%)')
    plt.show
    show(block=False) # plot during program runtime
    
    
def plot_points(std_test,r_test,r_predicted):
    """
    plots the frontier backtested at user-inputted dates,
    each point represents a optimized portfolio.
    
    """
    colors=[]
    for i in range(len(std_test)):
        std_test[i]=std_test[i]*100
        r_test[i]=r_test[i]*100
        r_predicted[i]=r_predicted[i]*100
        if r_test[i]>r_predicted[i]:
            colors += 'g'
        elif r_test[i] < r_predicted[i]:
            colors += 'r'
        else:
            colors += 'k'
        
    plt.scatter(std_test, r_test,c=colors)
    plt.title('Backtested Frontier')
    plt.ylabel('Portfolio Average Daily Return (%)')
    plt.xlabel('Portfolio Standard Deviation (%)')
    n = [x for x in range(1,len(r_test)+1)]
    for i, txt in enumerate(n):
        plt.annotate(txt, (std_test[i], r_test[i]))
    plt.show
    show(block=False) # plot during program runtime