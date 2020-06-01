#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prints
"""

from matrix_manip import *
from user import *

#
def print_glob_min_variance(w_glob_min,r_glob_min,tickers,mean_returns,covar,stds,start1,end1):
    
    # calculate the stdev of minimum variance portfolio
    var=(w_glob_min@covar)@np.transpose(w_glob_min)
    p_std=np.sqrt(var)
    
    
    print('\nIn the period from ' + start1 + ' to ' + end1 + ', the inputted securities had the following average daily returns and standard deviations:')
    for x in range(len(tickers)):
        print(str(tickers[x]) + ": r = " + '{0:.{1}f}'.format((mean_returns[x]*100),4) + "%, std = " + '{0:.{1}f}'.format((stds[x]*100),4) +"%")
    print("\nBased on data from that period, the allocation the portfolio with the smallest variance is as follows (where negatives indicate short positions):")
    print_allocations(w_glob_min,tickers)
    print('\nThis portfolio has a daily return of: '+ '{0:.{1}f}'.format((r_glob_min*100),4) + '%')
    print(' and a daily standard deviation of: '+ '{0:.{1}f}'.format((p_std*100),4) + '%')
    print_line()


def print_allocations(w,tickers):
    for x in range(len(tickers)):
        print(str(tickers[x]) + ': ' + '{0:.{1}f}'.format((w[x]*100),4)+'%')
        
        
def print_realtest_results(r,std,r_test,weights,tickers,start1,end1,start2,end2,i):
    print('\n\nBacktest %d'%(i+1)) #1 bcuz python index starts at 0
    if r>r_test:
        print('**Portfolio has higher returns than the model predicted')
    elif r<r_test:
        print('**Portfolio has lower returns than the model predicted')
    else:
        print('**The portfolio performed as predicted')
    print('\nAllocations of optimal portfolio that returns %.4f%% daily from %s to %s:'%(r_test*100,start1,end1))
    print_allocations(weights,tickers)
    print('\nThat portfolio performs as follows from %s to %s:'%(start2,end2))
    print('Return: ' + '{0:.{1}f}'.format((r*100),4) + '%')
    print('Standard deviation: ' + '{0:.{1}f}'.format((std*100),4) + '%')
    print_line()
    
def print_portfolio(r,std):
    print('Return: %f'%r)
    print('Standard Deviation: %f'%std)
    
def print_line():
    print('_'*90)
    
def print_missing_tickers(tickers,date1,date2):
    print_line()
    print('\nThe following tickers were not listed on at least one trading day during the period entered:\n')
    for ticker in tickers:
        print(ticker)
    print('\nAll entered tickers are listed during period: %s to %s'%(date1,date2))