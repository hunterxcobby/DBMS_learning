In SQL, we can compute values for a table by expressing the computation in the SELECT clause. This creates a new column in the output table, similar to a named attribute. Let's take an example where we want to find the subtotal for each line in the `OrderLines` table based on the UML class diagram.

```sql
SELECT custID, orderDate, UPC, unitSalePrice * quantity
FROM orderlines;
```

This query calculates the subtotal for each line by multiplying the unit sale price with the quantity. The result shows the computed subtotal for each line, including all three `OrderLines` primary key attributes.

```plaintext
Order line subtotals
5678    2003-07-14    51820 33622    11.95
9012    2003-07-14    51820 33622    23.90
9012    2003-07-14    11373 24793    21.25
5678    2003-07-18    81809 73555    18.00
5678    2003-07-20    51820 33622    23.90
5678    2003-07-20    81809 73555    9.00
5678    2003-07-20    81810 63591    24.75
```

Computation is not limited to column names; it can also involve constants. For example, `unitSalePrice * 1.06` could be used to find the sale price plus sales tax.

To improve readability, we can create an alias for the computed column using the AS keyword.

```sql
SELECT custID, orderDate, UPC, 
  unitSalePrice * quantity AS subtotal
FROM orderlines;
```

This query provides a more meaningful heading for the computed column, making it clearer to understand.

```plaintext
Order line subtotals
5678    2003-07-14    51820 33622    11.95
9012    2003-07-14    51820 33622    23.90
9012    2003-07-14    11373 24793    21.25
5678    2003-07-18    81809 73555    18.00
5678    2003-07-20    51820 33622    23.90
5678    2003-07-20    81809 73555    9.00
5678    2003-07-20    81810 63591    24.75
```

This way, we can perform computations on the data within a table and present the results in a clear and meaningful manner.