-- 1) What is the total sales amount for each category of products?

SELECT 	
	round(sum(sales)::numeric,2) AS total_sales,
	category
FROM 
	superstore
GROUP BY 
	category;
	
-- 2) What is the average sales amount for each sub-category of office supplies products?
SELECT 	
	ROUND(AVG(Sales)::numeric, 2) AS total_sales,
	Sub_Category,
	category
FROM 
	superstore
WHERE 
	category='Office Supplies'
GROUP BY 
	Sub_Category,category;

--3) Which customer has the highest total sales amount and what is their customer ID?
SELECT 	
	round(sum(sales)::numeric,2) AS total_sales,
	Customer_Name,
	Customer_ID
FROM 
	superstore
GROUP BY 
	Customer_Name,Customer_ID
ORDER BY 
	total_sales DESC
LIMIT 5;


--4) What is the total sales amount for each state in the United States?

SELECT 	
	round(sum(sales)::numeric,2) AS total_sales,
	Country,
	State
FROM 
	superstore
GROUP BY 
	Country,State
ORDER BY 
	total_sales DESC;
	
-- 5) How many orders were shipped via each mode of shipment and what was the total sales amount for each mode?
SELECT 	
	round(sum(sales)::numeric,2) AS total_sales,
	Ship_Mode,
	count(*) AS total_orders_shipped
FROM 
	superstore
GROUP BY 
	Ship_Mode;
	
-- 6) What is the average sales amount for each product in the furniture category?
SELECT 	
	round(avg(sales)::numeric,2) AS avg_sales,
	Category,
	Product_Name
FROM 
	superstore
WHERE 
	Category='Furniture'
GROUP BY 
	Category,Product_ID,Product_Name;

-- 7) Which product had the highest sales amount and what was its name?
SELECT 	
	round(sum(sales)::numeric,2) AS total_sales,
	Product_Name
FROM 
	superstore
GROUP BY 
	Product_Name
ORDER BY 
	total_sales DESC
LIMIT 5;

-- 8) What is the total sales amount for each year in the data?
SELECT 	
	round(sum(sales)::numeric,2) AS total_sales,
	DATE_PART('year',Order_Date) AS order_year
FROM 
	superstore
GROUP BY 
	order_year;
	
-- 9) What is the total sales amount for each segment of customers?
SELECT 	
	round(sum(sales)::numeric,2) AS total_sales,
	Segment
FROM 
	superstore
GROUP BY 
	Segment;
	
-- 10) What is the total sales amount for each country in the data?
SELECT 	
	round(sum(sales)::numeric,2) AS total_sales,
	Country
FROM 
	superstore
GROUP BY 
	Country;

-- 11) What percentage of total orders were shipped on the same date?
SELECT COUNT(*) * 100.0 / (SELECT COUNT(*) FROM orders) AS percentage_shipped_on_same_day
FROM 
    orders
WHERE 
    Order_Date = Ship_Date;

-- 12) Name top 3 customers with highest total value of orders.
SELECT 
    Customer_Name, 
    SUM(Sales) AS Total_Sales 
FROM 
    superstore 
GROUP BY 
    Customer_Name 
ORDER BY 
    Total_Sales DESC 
LIMIT 3;

-- 13) Find the top 5 items with the highest average sales per day.
SELECT Product_Name,AVG(Sales/DATEDIFF(Order_Date)) AS Avg_Sales_Per_Day 
FROM superstore
GROUP BY Product_Name
ORDER BY Avg_Sales_Per_Day DESC
LIMIT 5;


-- 14) Write a query to find the average order value for each customer, and 
 rank the customers by their average order value.

SELECT Customer_Name,AVG(Sales) AS average_order_value
FROM superstore
GROUP BY Customer_Name
ORDER BY average_order_value DESC;

-- 15) Give the name of customers who ordered highest and lowest orders from each city.
SELECT 
    City,
    MAX(Customer_Name) AS Customers_with_highest_orders,
    MIN(Customer_Name) AS Customers_with_lowest_orders,
    MAX(Sales) AS Highest_order,
    MIN(Sales) AS lowest_order
FROM 
    superstore
GROUPBY 
    City

-- 16) What is the most demanded sub-category in the west region?
SELECT 
    COUNT(*) AS num_of_orders ,
    Sub_Category
FROM 
    superstore
WHERE
    Region='West'
GROUP BY 
    Sub_Category
ORDER BY 
    num_of_orders DESC
LIMIT 1;

-- 17) Which order has the highest number of items? And which order has the highest cumulative value?
SELECT 
    Order_ID,
    COUNT(*) AS Num_of_items,
    SUM(Sales) AS cumulative_value
FROM 
    superstore
GROUP BY 
    Order_ID
ORDER BY
    Num_of_items DESC
LIMIT 1;

-- 18) Which order has the highest cumulative value?
SELECT 
    Order_ID,
    SUM(Sales) AS cummative_value
FROM 
    superstore
GROUP BY 
    Order_ID
ORDER BY
    cummative_value DESC
LIMIT 1;


-- 19) Which city is least contributing to total revenue?
SELECT City, SUM(Sales) as TotalRevenue
FROM superstore
GROUP BY City
ORDER BY TotalRevenue ASC
LIMIT 1;


-- 20) What is the average time for orders to get shipped after order is placed?
SELECT 
    AVG(DATEDDIFF(Ship_Date,Order_Date)) AS Avg_Shipping_time
FROM 
    superstore;

-- 21) Which segment places the highest number of orders from each state and which segment places the largest individual orders from each state?
SELECT 
    State, 
    Segment AS High_order_segment, 
    SUM(1) AS Total_orders, 
    Segment AS Larger_order_segment, 
    MAX(Sales) AS Larger_order
FROM 
    superstore
GROUP BY 
    State,
    Segment;

-- 22) Find all the customers who individually ordered on 3 consecutive days where each day’s total order was more than 50 in value
SELECT DISTINCT Customer_Name
FROM superstore
WHERE Sales > 50 AND Order_Date IN (
    SELECT DISTINCT Order_Date
    FROM superstore
    WHERE Sales > 50
    GROUP BY Order_Date
    HAVING COUNT(DISTINCT Customer_Name) >= 3
)
GROUP BY Customer_Name, Order_Date
HAVING COUNT(DISTINCT Order_Date) >= 3;


-- 23) Find the maximum number of days for which total sales on each day kept rising

SELECT COUNT(*) AS NumDays
FROM (
    SELECT Order_Date, SUM(Sales) AS TotalSales
    FROM superstore
    GROUP BY Order_Date
    HAVING SUM(Sales) > (
        SELECT SUM(Sales)
        FROM superstore
        WHERE Order_Date = (
            SELECT MIN(Order_Date)
            FROM superstore
        )
    )
    AND Order_Date <= (
        SELECT MAX(Order_Date)
        FROM superstore
    )
    ORDER BY Order_Date ASC
) AS T1
JOIN (
    SELECT Order_Date, SUM(Sales) AS TotalSales
    FROM superstore
    GROUP BY Order_Date
    HAVING SUM(Sales) > (
        SELECT SUM(Sales)
        FROM superstore
        WHERE Order_Date = (
            SELECT MIN(Order_Date)
            FROM superstore
        )
    )
    AND Order_Date <= (
        SELECT MAX(Order_Date)
        FROM superstore
    )
    ORDER BY Order_Date ASC
) AS T2
ON T1.Order_Date = DATEADD(day, -1, T2.Order_Date);
