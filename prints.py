#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 20:13:23 2019

@author: aaronhorwin
"""

from DF_helper import *
from matrix_manip import *
from user import *


#
def print_glob_min_variance(w_glob_min,r_glob_min,tickers,mean_returns,covar,stds,start1,end1):
    
    # calculate the stdev of minimum variance portfolio
    # isn't working on import for some reason
#    p_std=calc_portfolio_stdev(covar,w_glob_min)
    var=(w_glob_min@covar)@np.transpose(w_glob_min)
    p_std=np.sqrt(var)
    
    
    print()
    print('In the period from ' + start1 + ' to ' + end1 + ', the inputted securities had the following average daily returns and standard deviations:')
    for x in range(len(tickers)):
        print(str(tickers[x]) + ": r = " + '{0:.{1}f}'.format((mean_returns[x]*100),4) + "%, std = " + '{0:.{1}f}'.format((stds[x]*100),4) +"%")
    print()
    print("Based on data from that period, the allocation the portfolio with the smallest variance is as follows (where negatives indicate short positions):")
    print_allocations(w_glob_min,tickers)
    print('\nThis portfolio has a daily return of: '+ '{0:.{1}f}'.format((r_glob_min*100),4) + '%')
    print(' and a daily standard deviation of: '+ '{0:.{1}f}'.format((p_std*100),4) + '%')
    print('_'*100)

def print_allocations(w,tickers):
    for x in range(len(tickers)):
        print(str(tickers[x]) + ': ' + '{0:.{1}f}'.format((w[x]*100),4)+'%')