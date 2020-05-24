#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interact with user
"""

import numpy as np
from prints import *

def get_portfolio_parameters():
    #creates list of tickers, split by spaces
    tickers = input('Enter the tickers of securities to include in this portfolio, seperated by a space: ')
    tickers = tickers.split(' ')
    
    # establish dates to optimize based on
    start1 = input('Enter a start date for the analysis (In format: 2020-1-28): ') 
    end1 = input('Enter an end date: ')

    return start1,end1,tickers
    

    
def backtest_or_restart():
    response = input('-Enter restart to change the tickers or the period the model uses.\n-Enter backtest to backtest \n\nEnter either backtest or restart: ')
    return response


def simulate_or_reality():
    print_line()
    print('\n-Enter real to get the actual return of the optimal allocation for any desired return during a different period than the model used\n-Enter simulate to conduct Monte Carlo simulation')
    response = input('Enter either real or simulate: ')
    print_line()
    return response

def backtesting_details(start1,end1):
    print('\n\nSimply enter a range of returns and a range of dates, and the weights of the optimal portfolios from the period %s to %s will be applied to the period entered.'%(start1,end1))

    quantity_rs = input('Enter how many portfolios to test: ')
    r1 = input('Enter the minimum return to test (%): ')
    r2 = input('Enter the maximum return to test (%): ')
    rs = np.linspace(float(r1)/100,float(r2)/100,int(quantity_rs))
    
    start2 = input('Enter beginning date for testing (format: year-month-day): ')
    end2 = input('Enter ending date for testing: ')
    
    print_line()
    return rs,start2,end2


def exit_or_cont():
    exit_or_cont = input('Enter continue to continue backtesting or end to end the session: ')
    if exit_or_cont == 'continue':
        return True
    else:
        return False
    
def initialize_MCsimulation():
    r = input('Enter the expected daily return (%): ')
    std = input('Enter the standard deviation of daily return (%): ')
    years = input('Enter how many years to simulate: ')
    n = input('Enter how many trials to run: ')
    return r,std,years,n
