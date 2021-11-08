# Portfolio Optimizer (Python Program)

Explainer video: https://www.youtube.com/watch?v=2too70WLJUo&list=PLcJs7myZYvBBMXHgucfNKxhTqoHopfnmA&ab_channel=OptimizeEverything

Program uses Mean-Variance Portfolio Theory to create optimal portfolios and provides backtesting capabilities. 

**(1)** First, the user inputs a list of tickers and a period of time for which data is retrieved using YahooFinance's API. The UI flow takes into account whether data exists (i.e., whether the company was publicly traded during the period of time inputted).

<img width="1433" alt="Screen Shot 2021-11-08 at 11 16 37 AM" src="https://user-images.githubusercontent.com/61487056/140779279-97c0a132-d360-436f-91a1-0f4ef6174bce.png">

**(2)** Next, the algorithm provides the user with the "efficient frontier". Y-axis: daily returns, x-axis: lowest standard deviation possible for each daily return.

<img width="490" alt="Screen Shot 2021-11-08 at 11 18 13 AM" src="https://user-images.githubusercontent.com/61487056/140780272-f3c9011b-dbd5-4f65-8158-7af4740e0609.png">


**(3)**:
There are two options for backtesting:

(3a)
One allows the user to test how this model performs in different periods. The plot below shows the efficient frontier model developed using data from one date-range plotted in another date-range. Each point represents a portfolio, and is colored green if its return exceeds that of the model's prediction and red otherwise. The image shows the UI for testing the model's efficacy.

<img width="455" alt="Screen Shot 2021-11-08 at 11 21 05 AM" src="https://user-images.githubusercontent.com/61487056/140782466-a47eaf0f-72c1-49dc-9c6c-aeecf1b28187.png">

<img width="608" alt="Screen Shot 2021-11-08 at 11 20 21 AM" src="https://user-images.githubusercontent.com/61487056/140782362-c3428820-80e3-4793-a742-481aada0397a.png">

(3b)
The second backtesting file conducts Monte Carlo simulation, given any average daily return and standard deviation on daily returns.

<img width="478" alt="Screen Shot 2021-11-08 at 11 21 25 AM" src="https://user-images.githubusercontent.com/61487056/140780526-5b8b0ff0-e109-4f75-aed5-e6a010b295d3.png">

 
 
To run: make sure you have Pandas and Numpy installed, then run main to start (i.e. enter main() into python command line).
