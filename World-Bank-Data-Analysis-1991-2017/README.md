# World-Bank-Data-Analysis-1991-2017
Examine the top 3 countries population-wise and analyze what are their trend and pain-points.

## Inspiration

I was curious to compare how top 3 populated countries of the world are differentiated in the standard of living and sustenance. India, China & United States are the three countries with highest population and interestingly they are at different steps of nation development. Below is the analysis to compare them on multiple metrics of real-world importance that matter to people's lives.
 
## Introduction to World Bank
[World Bank](https://data.worldbank.org/country) is a financial institution that provides loans to countries for capital projects.

> World Development Indicators (WDI) is the primary World Bank collection of development indicators, compiled from officially recognized international sources. It presents the most current and accurate global development data available, and includes national, regional and global estimates.[1] This statistical reference includes over 800 indicators covering more than 150 economies.

## Objective
Comparing cross-country statistics about development and people's lives around the globe and show the progress society is making through data visualization.

## Datasets Used
I have chosen 27 years time-series data starting 1991 - 2017. It includes three countries namely USA, India, China and average of World as a metric of comparison. Countries are compared on around 1500 metrics broken down by gender, age, employment sector, birth rate etc.

* [World Bank Metrics Data](https://github.com/dkekre21/World-Bank-Data-Analysis-1991-2017/blob/master/Datasets/API_Download_DS2_en_csv_v2_10077498.csv)
* [World Population Data](https://github.com/dkekre21/World-Bank-Data-Analysis-1991-2017/blob/master/Datasets/WorldPopulation.csv)

[Both datasets can also be directly downloaded from world bank website](https://data.worldbank.org/country)

## Link to Nbviewer Python Notebook 
Please check-out the link below to access complete python notebook along with plotly interactive maps:

[Click Here](http://nbviewer.jupyter.org/github/dkekre21/World-Bank-Data-Analysis-1991-2017/blob/master/Python%20Notebook/Project%202%20-World%20Bank%20Data%20Analysis%201991%20to%202017.ipynb)

## Tech-stack

* Matplotlib
* Plotly
* Python(pandas,numpy)

## Insights
> ### 1st Visualization : Analyze top three populated countries
![figure1](https://github.com/dkekre21/World-Bank-Data-Analysis-1991-2017/blob/master/Visualizations/World%20Population.png)
* As shown above the top three populated nations are China, India & USA in order. With China & India together constitute 36% of world population.

![figure2](https://github.com/dkekre21/World-Bank-Data-Analysis-1991-2017/blob/master/Visualizations/population%20growth%20rate.png)
* China is the most populated nation in 2017. However, India is second nation with over 1Billion. Current growth rate of 1.5% suggests that if Indian government does not put stringent methods in place it will become the most populated country beating.

> ### 2nd Visualization : Indian Paradox: Rising Education, Decrease in Women's Labor Force 

![figure5](https://github.com/dkekre21/World-Bank-Data-Analysis-1991-2017/blob/master/Visualizations/labor%20force%20gender%20gap.PNG)
* Focusing on India, there is a big decrease in female labor force starting 2005. It sounds strange because one won't expect a steady labor force participation in earlier years and suddenly its dropping in age of ambitious women!

![figure6](https://github.com/dkekre21/World-Bank-Data-Analysis-1991-2017/blob/master/Visualizations/education%20gender%20gap.PNG)

* It is paradoxical that for India the labor force participation has been declining since 2005, However since 2005 women participation in primary and lower secondary education has been increasing!
* It would be interesting to see female labor force participation by income group and level of education. However, the dataset is limited in capabilities to do so.
* Theory suggests that women have a curvilinear relationship between education and employment. 
    * It would mean that women with less eduation and less income would be compelled to have a job for sustenance.
    * On the other hand women with advanced education would be ambitious enough to participate in labor force.
    * It would be the women in between who do not meet the gap between mid level education and skilled job requirements.
    
> ### 3rd Visualization : Highest CO2 emission in United States

![figure4](https://github.com/dkekre21/World-Bank-Data-Analysis-1991-2017/blob/master/Visualizations/CO2%20emission.PNG)
* United States is well above World average in CO2 emmision, world average at 5% whereas USA CO2 emission rate is 20%.
* India is constantly below world average at around 0.9%
* BUT Is it the true picture? 
    * USA emits CO2, 2.2 times as China on per capita basis.But, China has 4.3 times as many people as USA! *Thus from overall perspective China emits over 70% more CO2 compared to US annually. India even greater *
    
![figure5](https://github.com/dkekre21/World-Bank-Data-Analysis-1991-2017/blob/master/Visualizations/CO2%20composition.png)
* Electricity and heat production stays the main source of CO2 emission across all three countries. 
* In United States, second contributing sector is transport unlike India & China where it is residential buildings. It makes sense because in USA buildings are constructed using wood, whereas in India it is always brick and mortar.
   

## Future Scope
* Time series forecasting
* Comparing World Population based on regions, low income-high income, and development.
