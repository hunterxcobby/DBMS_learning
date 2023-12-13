When working with SQL, functions are powerful tools to compute and manipulate data. In your order entry example, you mentioned two derived attributes: `/subtotal` in `OrderLines` and `/total` in `Orders`. Let's discuss how SQL functions can be used to compute these attributes.

**1. Computed Attribute in OrderLines (/subtotal):**
   - Assuming `/subtotal` is calculated based on the quantity and unit price of items in each order line.
   - SQL Example: `SELECT quantity * unit_price AS subtotal FROM OrderLines;`
   - Explanation: The `AS` keyword is used to give an alias to the computed result, and the `*` is the multiplication operator.

**2. Computed Attribute in Orders (/total):**
   - Assuming `/total` is calculated based on the sum of subtotals for all order lines in each order.
   - SQL Example: `SELECT order_id, SUM(quantity * unit_price) AS total FROM OrderLines GROUP BY order_id;`
   - Explanation: The `SUM` function is used to calculate the total by summing up the subtotals for each order_id. The `GROUP BY` clause groups the results by order_id.

**Note:**
   - SQL functions vary among database systems, so it's crucial to refer to your specific database software's reference manual for accurate syntax and usage.
   - Common SQL functions include mathematical operations (`SUM`, `AVG`, `MAX`, `MIN`), string functions, date functions, and more.

These SQL techniques with functions allow you to compute and derive valuable information from the stored data in your database, enhancing the flexibility and capability of your queries.