# PortfolioOptimizer
Portfolio optimization in Python

Program uses Markowitz mean return-variance portfolio theory to create optimal portfolios and provides backtesting capabilities. The user inputs a list of tickers and a period of time for which data is retrieved from YahooFinance's API. A model which outputs the lowest-variance portfolio for any given return is then created, along with a plot. This plot is known as the efficient frontier: the y-xis is daily returns and the x-axis is the lowest possible standard deviation possible for that daily return.

The function for backtesting then allows the user to test how this model performs in different periods. The user enters a second set of beginning and ending dates, and the program returns the model's performance in that period. For example, a model created using data from only 2019 would be revealed as insufficient if backtested in the first quarter of 2020.
 
 
 
 
  
  
   
To run: make sure you have Pandas and Numpy installed, then run main to start (i.e. enter main() into python command line).
