# PortfolioOptimizer

Program uses Mean-Variance Portfolio Theory to create optimal portfolios and provides backtesting capabilities. The user inputs a list of tickers and a period of time for which data is retrieved using YahooFinance's API. A model which outputs the lowest-variance portfolio for any given return is then created, along with a plot known as the efficient frontier. On the y-xis is daily returns and on the x-axis is the lowest standard deviation possible for each daily return.

There are two options for backtesting. One allows the user to test how this model performs in different periods. The user enters a second set of beginning and ending dates, and the program returns the model's performance in that period. For example, a model created using data from only 2019 would be revealed as insufficient if backtested in the first quarter of 2020. The second backtesting file conducts Monte Carlo simulation, given any average daily return and standard deviation on daily returns.
 
 
 
 
Summary: Portfolio optimization in Python.
  
   
To run: make sure you have Pandas and Numpy installed, then run main to start (i.e. enter main() into python command line).
