# PortfolioOptimizer
Portfolio optimization in Python

Markowitz maean return-variance portfolio theory is used to create the optimal portfolio. The user inputs a list of tickers and beginning and ending dates between which data is retrieved from YahooFinance's API. A model which outputs the lowest-variance portfolio for any given return is then created, along with a plot of this. This plot is known as the efficient frontier: the y-xis is a return and the x-axis is the lowest possible standard deviation.

The function for backtesting then allows the user to test how this model performs in different periods. The user enters a second set of beginning and ending dates, and the program returns the return and standard deviation of the model's optimal portfolio. For example, a model created in 2019 would not perform well in the first quarter of 2020.

Run main to start (i.e. enter main() into python command line).
