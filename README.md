# DiDi_Business_Case

# Generalities

1. Change the CSV path to read the data. 
2. The code generate 3 CSV (Avg_day,growth_index,number_tickets_month), change the path to generate correctly. 

# Clean Data

1. Convert 2091 values to 2021 if it's >2091-06-02 
2. Drop values >2021-06-02, create week number

Questions 

# 1. Write the SQL queries necessary to generate a list of the five cities that have the highest average number of tickets the last three weeks. The result table should also contain that average per city.

I use the last three months because the last 3 weeks didn’t had enough data, the result is in the 'number_tickets_month.csv'

# 2. Use SQL to discover which day of the week there are usually more tickets on average in the top 10 cities.

I used two methods with the same result, one is with average tickets per day, and the other was using the mode, the result table is 'Avg_day.csv'

# 3. How was the percentage of growth of the amount of tickets week over week for the last four weeks of the data? Use SQL too.

To calculate this, I used the midpoint method because the first two weeks didnt have any tickets, with another method you have to divided by 0 and with the midpoint method you divided by the average.

# 5. If we could share with you the content of each ticket (the description of what happened and the conversation between the customer and the Customer Experience agents), what could you propose to improve the experience of each customer? What could you propose to optimize the time that the agent spends in each case?

Relate groups of keywords to a specific topic, measure recurrence and create default, answers and compensations.

# 6. What other data would you want to join in order to get more insights to increase the customer satisfaction?

Satisfaction rate, tickets per user, frecuency of use, rate to drivers, distance traveled, money spent, avg wait time for a driver, time of orders, orders canceled

# 8. We want to build up a model to predict “Possible Churn Users” for DiDi Rides APP (e.g. no trips in the past 4 weeks). Please list all features that you can think about and the data mining or machine learning model or other methods you may use for this case.

I would start with an exploration of the data if it fits to use decision trees and random forest, or maybe a similar but more optimized algorithm like XGBOOST. 

Some of the possible features I would use would be: frequency of use, avg wait time for a driver, orders cancelled.

I would start with these features by analyzing correlations with possible churn, to establish weights or new features.




NOTE: For the first two questions, a real number have to consider the total rides per city, to obtain a statistic significance, a relationship between the total rides and total tickets.
