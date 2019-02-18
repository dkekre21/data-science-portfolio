# Lending-Club-Loan-Analysis-2007-2015
The goal of this analysis is to analyze Lending Club data and draw interesting insights. I have attempted to use external datasets to get more information out of the loan data.

## Inspriration

Peer-to-peer lending is arguably one of the greatest financial innovations of the past few years, especially for borrowers.
So, we were excited to find out how their loans performed and what their defaulter patterns looked like. Hence we decided to do deeper analysis on Lending club loan data because they are pioneer in the business.

## Introduction to Lending Club

[LendingClub](https://www.lendingclub.com) is the world’s leading online marketplace for connecting borrowers and investors. As explained by [Wikipedia](https://en.wikipedia.org/wiki/Lending_Club),
>Lending Club enables borrowers to create unsecured personal loans between $1,000 - $40,000. The standard loan period is three years. Investors can search and browse the loan listings on Lending Club website and select loans that they want to invest in based on the information supplied about the borrower, amount of loan, loan grade, and loan purpose. Investors make money from interest. Lending Club makes money by charging borrowers an origination fee and investors a service fee.

## Objective
To visualize the meaningful insights we get thorugh our analysis from the Lending club dataset under consideration. 

## Link to Nbviewer Python Notebook 
[Click here](http://nbviewer.jupyter.org/github/dkekre21/Lending-Club-Loan-Analysis-2007-2015/blob/master/Python%20Notebook/Lending%20Club%20-%20Data%20Visualization.ipynb)

## Links to Dataset
The [dataset](https://www.kaggle.com/husainsb/lendingclub-issued-loans) we analysed had lending club loan data from 2007 through 2015. Our data is a matrix of about 890 thousand observations and 74 variables. We have merged the below datasets with the parent dataset for our analysis:
* [Lending Club Loan data](https://www.kaggle.com/husainsb/lendingclub-issued-loans#lc_loan.csv)

* [US Population by State](https://www.census.gov/data/datasets/2017/demo/popest/state-total.html)
   
* [US State Names](https://www.kaggle.com/husainsb/lendingclub-issued-loans#us-state-codes.csv)
   
* [US Regions](https://github.com/dkekre21/Lending-Club-Loan-Analysis-2007-2015/blob/master/Region.csv)

## Tech-stack

* Matplotlib
* Plotly
* Wordcloud
* Python(pandas,numpy)

## Insights
> ### 1st Visualization : Riskier the loan, Higher the interest rate

![figure1](https://github.com/dkekre21/Lending-Club-Loan-Analysis-2007-2015/blob/master/Visualization/Average%20Interest%20Rate%20By%20Loan%20Grade%20(2007-2015).png)
* Loan Grade represents default risk in order from 'A' to 'G' as low to high risk. As it can be seen from the graph interest rates remain higher for riskier loan grades.
* Also, over the years interest rates have increased with higher rates for loans in grade C,D,E,F,G. We think it could be due to 2008 _Recession_. 
* For least risky loans, grade- A,B the interest rates have remained pretty much steady and eventually came down.

> ### 2nd Visualization : Best 5 Loan Borrowing States

![figure2](https://github.com/dkekre21/Lending-Club-Loan-Analysis-2007-2015/blob/master/Visualization/%25%20Loans%20Issued%20per%20State%20(2007-2015).png)
* As chart above shows more than 40% loans are issued to residents of _California, Newyork, Texas, Florida and Illinois_. Barely 500 loans combined are issued to residents of _Idaho, Iowa, North Dakota_ 

![figure3](https://github.com/dkekre21/Lending-Club-Loan-Analysis-2007-2015/blob/master/Visualization/Default%20Rate%20%26%20Total%20Loans%20vs%20States.png)
* There is no clear indication that states with highest number of loans borrowed _e.g. California_ have the tendency to default more compared to borrowers of other states.
* The perception of higher defaults in _California, Newyork, Texas, Florida,Illinois_  can be maily due to higher population size of these advanced states. Thus, even though the top five borrowing states have highest number of defaults, it is not complusively because of higher default rates.

> ### 3rd Visualization : Employee Title Analysis

![figure4](https://github.com/dkekre21/Lending-Club-Loan-Analysis-2007-2015/blob/master/Visualization/Job%20Title%20wordcloud.PNG)
* The above word cloud shows the top 40 employment titles for loans issued between 2007-2015. It seems borrowers with title Teachers and Managers take loans more often compared to other borrowers.

## Future Scope
* Predicting which loan could default and identify important predictors, using predictive modeling.
* Sentiment Analysis

