SQL aggregate functions are used to compute values based on multiple rows in tables, creating new columns in the output. Let's explore some examples:

1. **Total Sales:**
   To find the total amount of all sales, we can use the `SUM` function to add up the price-times-quantity computations from every line of the `OrderLines` table.

    ```sql
    SELECT SUM(unitSalePrice * quantity) AS totalsales
    FROM orderlines;
    ```

    Output:
    ```plaintext
    Sales
    132.75
    ```

2. **Total for Each Order:**
   To compute the total for each order, we need to add up order lines and group the totals for each order using the `GROUP BY` clause.

    ```sql
    SELECT custID, orderDate, SUM(unitSalePrice * quantity) AS total
    FROM orderlines
    GROUP BY custID, orderDate;
    ```

    Output:
    ```plaintext
    Order totals
    5678    2003-07-14    11.95
    9012    2003-07-14    45.15
    5678    2003-07-18    18.00
    5678    2003-07-20    57.65
    ```

    Other frequently-used aggregate functions include `MIN` (minimum value), `MAX` (maximum value), and `AVG` (average value).

3. **Counting Rows:**
   The `COUNT` function can be used to count the number of rows in a grouping. To count all rows, we use `COUNT(*)`.

    ```sql
    SELECT COUNT(*)
    FROM orders;
    ```

    Output:
    ```plaintext
    Orders
    4
    ```

4. **Counting Groups of Rows:**
   We can count groups of rows with identical values in a column. Here, we find out how many times each product has been ordered.

    ```sql
    SELECT prodname AS "product name", 
           COUNT(prodname) AS "times ordered"
    FROM products NATURAL JOIN orderlines
    GROUP BY prodname;
    ```

    Output:
    ```plaintext
    Product orders
    Hammer, framing, 20 oz.        3
    Saw, crosscut, 10 tpi          1
    Screwdriver, Phillips #2, 6 inch    2
    Pliers, needle-nose, 4 inch    1
    ```

5. **Filtering Groups with HAVING:**
   The `HAVING` clause is used to filter groups based on the results of the group function. For example, we could ask for only those products that have been sold more than once.

    ```sql
    SELECT prodname AS "product name", 
           COUNT(prodname) AS "times ordered"
    FROM products NATURAL JOIN orderlines
    GROUP BY prodname
    HAVING COUNT(prodname) > 1;
    ```

