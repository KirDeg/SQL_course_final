## The case of using python script with quering to PostreSQL

There is a table exist with a name "prices". This table consist of three columns: "product" - names of products,"price" - prices of products, "date_start" - date from which the relevant product price comes into force. 

1.
* Write a query, that returns a list with relevant prices(the latest date in "date_start" for each product("product") 
* Write a function, that take price of the product and return tuple like ([date_start1, date_start2,...],[price1, price2,...]). date_start(n) - date, sorted in ascending order, price(n) - corresponding price of the product. With each call the function should call to DB, choosing necessary data. A format of the output dates is arbitrary. 

Example of function:

>>>my_func('A')
>>>(['2018-05-11','2019-01-01',...],[27, 20, ...])

2. 
Add to ou
