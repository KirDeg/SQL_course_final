## The case of using python script with quering to PostreSQL

There is a table exist with a name "prices". This table consist of three columns: "product" - names of products,"price" - prices of products, "date_start" - date from which the relevant product price comes into force. 

1.
* Write a query, that returns a list with relevant prices(the latest date in "date_start" for each product("product") 
* Write a function, that take price of the product and return tuple like ([date_start1, date_start2,...],[price1, price2,...]). date_start(n) - date, sorted in ascending order, price(n) - corresponding price of the product. With each call the function should call to DB, choosing necessary data. A format of the output dates is arbitrary. 

Example of function:

>>>my_func('A')
>>>(['2018-05-11','2019-01-01',...],[27, 20, ...])

2. 
Add to our database another table - "sales", which consist of columns 'product', 'date', 'amount', 'country'.

Each row of this table characterizes number of sales('amount') of a specific product in some country for a certain date. 

Task:

Write a query, that make a table "revenue", which consist of columns: 'product', 'date', 'amount', 'country', 'revenue'.

A formula for calculating a revenue: revenue = sales.amount * prices.price

3.1. 
Write a function that plot pie chart by country in total revenue for the period. With each call the function should call to the table 'revenue' from the task 2, choosing necessary data. 

Example of call of the function:
my_func('2019-02-01','2019-05-01')

3.2. 
Write a function, that takes two dates(date_start, date_end), then makes and print a covariance matrix of sales between products for a certain period.  

