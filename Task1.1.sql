SELECT product, price
FROM prices 
WHERE 
product  IN  (SELECT product FROM (SELECT product, MAX(date_start)
FROM prices
GROUP BY product) AS A) 
AND
date_start IN (SELECT p1 FROM (SELECT product, MAX(date_start) AS p1
FROM prices
GROUP BY product) AS B);