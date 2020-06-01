#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Performs matrix operations on processed data
Lagrangian used to find minimum variance portfolios
"""

import numpy as np


def np_calc_portfolio_return(mean_returns,weights):
    """
    Input a 1d arrays of returns and weights
    Return float of return
    """
    #transpose weights    
    r=np.dot(mean_returns,weights)
    return r


def calc_portfolio_stdev(covar,weights):
    """
    Input a 2d np array covar, 1d np array weights
    Return float of stdev
    """
    var=(weights@covar)@np.transpose(weights)
    stdev=np.sqrt(var)
    return stdev


def calc_global_min_variance_portfolio(covar):
    """
    Input 2d np array covar
    Returns a 1d array of weights corresponding to the
    minimum variance portfolio
    
    A * z = b --> z = A^-1 * b
    """
    # Get dimension
    n = len(covar)
    
    # creates a 1xn 2d array containing 0's
    row = np.array([np.ones(n)])
    # creates an nx1 2d array containin n-1 0's and one 1
    col = np.concatenate((row.T,np.array([[0]])),axis=0)
    
    # Concat row below covar matrix
    A_with_bottom_row=np.concatenate((2*covar,row),axis=0)
    # Concat col beside covar matrix
    A = np.concatenate((A_with_bottom_row,col),axis=1)
    
    # b is vector of linear equation's solutions
    b=np.concatenate((np.zeros([n,1]),np.array([[1]])),axis=0)

    # Solve by inverting A
    z = np.linalg.solve(A,b)
    
    # Flatten into 1d
    z=z.flatten()
    
    return z[:-1]



def efficient_frontier(mean_returns,covar,rs):
    """
    input a 1d array of returns, 2d array of covar, and 1d of r's
    returns a 1d array of the standard deviations and a 2d array
    of  the weights of the minimum variance portfolio for each 
    return in rs
    """
    sigmas=np.zeros(len(rs))
    weights=np.zeros((len(rs),len(mean_returns)))
    # returns=rs
    for i in range(len(rs)):
        weights[i]=calc_min_variance_portfolio(mean_returns,covar,rs[i])
        sigmas[i]=calc_portfolio_stdev(covar,weights[i])
    return sigmas,weights



def calc_min_variance_portfolio(e,covar,r):
    """
    Input 1d array of expected returns, 2d array of covariance,
    and float of desired return, r
    Returns a 1d array of the weights for the minimum
    variance portfolio, given the desired return
    """
    n = len(covar)
    
    # vectors of ones
    ones = np.array([np.ones(n)])
    ones_T = ones.T
    
    # Transpose expected returns
    e_T = np.array([e]).T

    # Create cols
    col1 = np.concatenate((e_T,[[0]],[[0]]),axis=0)
    col2 = np.concatenate((ones_T,[[0]],[[0]]),axis=0)
    
    # Concat everything into one matrix
    A_with_bottom_rows=np.concatenate((2*covar,[e],ones),axis=0)
    A = np.concatenate((A_with_bottom_rows,col1,col2),axis=1)

    # Create b
    zeros = np.array([np.zeros(n)]).T
    b = np.concatenate((zeros,np.array([[r]]),np.array([[1]])),axis=0)
    
    # Solve by inverting A
    z = np.linalg.solve(A,b)
    
    # Flatten into 1d
    z=z.flatten()
    
    return z[:-2]


# def simulate


def daily_to_annual(daily_r):
    """
    Input daily return as a percent
    Returns that return on an annual basis as a percent
    """
    annual_r = (1+daily_r/100)**(365) - 1
    return annual_r*100