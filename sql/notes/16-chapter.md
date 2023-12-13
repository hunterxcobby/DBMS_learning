In SQL, functions are employed to compute values or manipulate data, especially when the information needed is not directly stored in the database. Here are some key concepts:

1. **Computed Columns:**
   - Computed columns can be created in the output table using computations in the `SELECT` clause.
   - Example: Finding the subtotal for each line of the `OrderLines` table based on the unit sale price and quantity.

     ```sql
     SELECT custID, orderDate, UPC, unitSalePrice * quantity
     FROM orderlines;
     ```

   - Computation can also include constants, such as `unitSalePrice * 1.06` to find the sale price plus sales tax.
   - Column headings or aliases can be created for clarity using the `AS` keyword.

     ```sql
     SELECT custID, orderDate, UPC, 
       unitSalePrice * quantity AS subtotal
     FROM orderlines;
     ```

2. **Aggregate Functions:**
   - Aggregate functions in the `SELECT` clause compute values based on multiple rows, creating new columns in the output.
   - Example: Calculating the total sales by summing up price-times-quantity computations.

     ```sql
     SELECT SUM(unitSalePrice * quantity) AS totalsales
     FROM orderlines;
     ```

   - Grouping can be done using the `GROUP BY` clause, and other common aggregate functions include `MIN`, `MAX`, `AVG`, and `COUNT`.

     ```sql
     SELECT custID, orderDate, SUM(unitSalePrice * quantity) AS total
     FROM orderlines
     GROUP BY custID, orderDate;
     ```

3. **Other Functions:**
   - Various other functions in SQL deal with formatting, converting data types, manipulating strings, and performing miscellaneous tasks.
   - These functions can be proprietary, differing across database systems.
   - Examples include rounding, truncating, formatting numeric data types, manipulating character data types, handling dates and times, and more.

These functions enhance the capabilities of SQL by allowing dynamic computation and manipulation of data. Always refer to the reference manual for your specific database system for accurate information on function syntax and usage.