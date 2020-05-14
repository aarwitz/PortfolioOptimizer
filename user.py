#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:37:10 2020

@author: aaronhorwin
"""



def get_portfolio_parameters():
    #creates list of tickers, split by spaces
    tickers = input('Enter the tickers of securities to include in this portfolio, seperated by a space: ')
    tickers = tickers.split(' ')
    
    # establish dates to optimize based on
    start1 = input('Enter a start date for the analysis (In format: 2020-1-28): ') 
    end1 = input('Enter an end date: ')

    return start1,end1,tickers
    
    
def backtest_or_restart():
    response = input('-Enter restart to change the tickers or the period the model uses data from.\n-Enter backtest to get the actual return of the optimal allocation for any desired return during a different period than the model used (i.e. backtesting).\n\nEnter either backtest or restart: ')
    return response

def backtesting_details(start1,end1):
    print('\n\nSimply enter your desired return and a range of dates, and the weights of the optimal portfolio from the period %s to %s will be applied to the period entered.'%(start1,end1))

    desired_return=float(input('Enter desired daily return as a %: '))/100
    start2 = input('Enter beginning date for testing (format: year-month-day): ')
    end2 = input('Enter ending date for testing: ')
    print('_'*100)
    return desired_return,start2,end2

def exit_or_cont():
    exit_or_cont = input('Enter new to test this same model during another period or end to end the session: ')
    if exit_or_cont == 'new':
        return True
    else:
        return False