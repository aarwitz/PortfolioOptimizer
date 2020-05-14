#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 11:30:40 2019

@author: aaronhorwin
"""

import numpy as np
from prints import *


def np_calc_portfolio_return(mean_returns,weights):
    """
    Input a 1d arrays of returns and weights
    Return float of return
    """
    #transpose weights    
    r=np.dot(mean_returns,weights)
    return r


def calc_multiple_portfolio_stdevs(covar,weights):
    portfolio_stdevs=np.zeros(len(weights))
    for i in range(len(weights)):
        stdev=calc_portfolio_stdev(covar,weights[i])
        portfolio_stdevs[i]=stdev
    return portfolio_stdevs

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
    """
    array_ones = np.ones(len(covar))  # creates a 1x3 array containing ones
    i_covar=np.linalg.inv(covar)   # takes matrix inverse of covar
    Lambda = np.dot(np.dot(array_ones,i_covar),array_ones)    # adds up the inverse of the variances
    return np.dot(array_ones,i_covar)*1/Lambda  # multiplies each variance by the inverse of Lambda


def calc_efficient_portfolios(mean_returns,covar,rs):
    """
    input a 1d array of returns, 2d array of covar, and 1d of r's
    returns a 1d array of the standard deviations and a 2d array
    of  the weights of the minimum variance portfolio for each 
    return in rs
    """
    sigmas=np.zeros(len(rs))
    weights=np.zeros((len(rs),len(mean_returns)))
    returns=rs
    for i in range(len(rs)):
        w=calc_min_variance_portfolio(mean_returns,covar,rs[i])
        sigma=calc_portfolio_stdev(covar,w)
        r=w@mean_returns
        
        # input the  sigmas and weights to their arrays
        sigmas[i]=sigma
        weights[i]= w
        
    print()
    return sigmas,weights,returns


def calc_min_variance_portfolio(e,covar,r):
    """
    Input 1d array of expected returns, 2d array of covariance,
    and float of desired return, r
    Returns a 1d array of the weights for the minimum
    variance portfolio, given the desired return
    """
    mu=np.array(e).reshape(len(e),1)

    # adds a colum of ones next to the expected returns
    mu_ones = (np.insert(mu,1,1,axis=1))
    
    #take inverse of covariance
    i_covar=np.linalg.inv(covar)
    
    #transpose mu_ones
    t_mu_ones=np.transpose(mu_ones)
    
    # A multiplies the expected returns and the covariance matrix
    # the bottom row is the sum of that multiplication
    A=np.dot(np.dot(t_mu_ones,i_covar),mu_ones)
    i_A=np.linalg.inv(A)

    # this returns a matrix of the weights for the minimum variance
    weights = np.dot(np.dot(np.dot(i_covar,mu_ones),i_A),np.array([[r],[1]]))
    
    # flatten into 1d array for purpose of dot products
    weights=weights.flatten()
    
    return weights