WITH dt AS(SELECT prices.product, sales.date, MAX(prices.date_start) AS date_start, sales.country
FROM sales, prices
WHERE date >= date_start and sales.product = prices.product
GROUP BY date, prices.product, sales.country),

dt1 AS (SELECT dt.product, dt.date, dt.date_start, country, price
FROM dt INNER JOIN prices 
ON dt.product = prices.product AND dt.date_start = prices.date_start),

results AS(SELECT dt1.product, dt1.date, sales.amount, dt1.country, dt1.price * sales.amount AS revenue
FROM dt1 INNER JOIN sales
ON dt1.product = sales.product AND dt1.date = sales.date AND dt1.country = sales.country
ORDER BY product, date)

SELECT * 
INTO revenue
FROM results;