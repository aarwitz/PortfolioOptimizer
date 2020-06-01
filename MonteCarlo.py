
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file contains contains the MCStockSimulator class. It
is used to generate stock returns and values.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import show
import statistics


class MCStockSimulator:
    """
    This is the base class for option pricing using
    Monte Carlo simulation. It includes the methods
    for generating lists of returns and stock values.
    """
    
    def __init__(self,t,r,sigma,s=100,nper_per_year=250):
        """
        Creates an object for base class using
        Monte Carlo Simulation
        Variables:
            s = beginning value
            t = years
            r = daily expected return (%)
            sigma = standard deviation of daily returns (%)
            nper_per_year = trading days in a year
        """
        self.t=t
        self.r=r/100
        self.sigma=sigma/100
        self.s=int(s)
        self.nper_per_year=int(nper_per_year)
        
    def __repr__(self):
        """
        Creates a printout, displaying each
        attribute of the object
        """
        
        format_s=format_s="(s=$" + '{0:.{1}f}'.format(self.s, 2)
        format_t=", t=" + '{0:.{1}f}'.format(self.t, 2)
        format_r = " (years), r=" + '{0:.{1}f}'.format(self.r*100, 4)
        format_sigma=", sigma=" + '{0:.{1}f}'.format(self.sigma*100, 4)
        format_nper=", nper_per_year="+str(self.nper_per_year)
        
        return "StockSimulator " + format_s+format_t+format_r+format_sigma+format_nper
    
    
    def generate_simulated_stock_returns(self):
        """
        This method simulates returns using randomly
        selected Z-scores from a numpy's random.normal()
        """
        returns=np.zeros(int(self.nper_per_year*self.t))
        
        # below for-loop simulates a return using the formula for discrete periods,
        # then puts the value into the numpy array
        for x in range(len(returns)): 
            sim_return=self.r+(np.random.normal()*self.sigma)
            returns[x]=sim_return
        return returns
    
    def generate_simulated_stock_values(self):
        """
        Creates a list of stock values based on the simulated
        returns from the generate_simulated_stock_returns 
        method above
        """
        a=np.zeros(int(self.nper_per_year*self.t+1))
        a[0]=self.s
        returns=self.generate_simulated_stock_returns()
        for x in range(len(a)-1):
            a[x+1]=a[x]*(1+returns[x])
        return a
        
    def plot_simulated_stock_values(self, num_trials = 1):
        """
        This method plots the values of the stock,
        using the above method, generate_simulated_stock_values
        """
        dt=1/self.nper_per_year
        array_periods=np.arange(0,self.t+dt,dt)   # array has to go until self.t+dt to get the last value
        final_values=np.zeros(num_trials)
        for x in range(num_trials):
            points=self.generate_simulated_stock_values()
            plt.plot(array_periods,points)
            final_values[x]=points[-1]
        plt.xlabel('Time (Years)')
        plt.ylabel('Value ($)')
        plt.show
        median=statistics.mean(final_values)
        mean=statistics.median(final_values)
        print('Median = %.2f, Mean = %.2f'%(median,mean))
        show(block=False) # plot during program runtimes