Subqueries in SQL are used when you don't have enough information to determine the rows you want in a query. Let's explore this concept with a couple of examples:

1. **Finding Customers in the Same Zip Code Area as Wayne Dick:**
   - Suppose you want to find the names of customers who live in the same zip code area as Wayne Dick, but you don't know the zip code.
   - You can start with a subquery to find Wayne Dick's zip code:

    ```sql
    SELECT cZipCode
    FROM Customers
    WHERE cFirstName = 'Wayne' AND cLastName = 'Dick';
    ```

   - This returns the zip code 90840.
   - Now, you can use this result in the main query to find the customers:

    ```sql
    SELECT cFirstName, cLastName, cZipCode
    FROM Customers
    WHERE cZipCode = (SELECT cZipCode FROM Customers WHERE cFirstName = 'Wayne' AND cLastName = 'Dick');
    ```

   - This returns the names of customers Alvaro Monge and Wayne Dick who share the zip code 90840.

2. **Finding Products Above the Average Unit Sale Price:**
   - Suppose you want to find the product names and sale prices of products whose unit sale price is greater than the average of all products.
   - Start with a subquery to find the average unit sale price:

    ```sql
    SELECT AVG(unitSalePrice) FROM OrderLines;
    ```

   - This returns the average unit sale price, for example, 10.621428.
   - Now, use this result in the main query to find products above the average:

    ```sql
    SELECT DISTINCT prodName, unitSalePrice
    FROM Products NATURAL JOIN OrderLines
    WHERE unitSalePrice > (SELECT AVG(unitSalePrice) FROM OrderLines);
    ```

   - This returns products with unit sale prices above the average.

Subqueries can return a single value or multiple values, and they are enclosed in parentheses. They are a powerful tool to handle dynamic conditions and make queries more flexible.