**Outer Join:**

An **OUTER JOIN** is a type of join that returns not only the rows with matching values in both tables but also the unmatched rows from one or both tables. It ensures that even if there are no matching values in the join condition, the result will still include rows from one or both tables, filled with NULL values for columns without matches.

Here's an example of a **LEFT OUTER JOIN** (also known as a **LEFT JOIN**):

```sql
SELECT cFirstName, cLastName, orderDate
FROM customers c LEFT OUTER JOIN orders o
ON c.custID = o.custID;
```

This query retrieves a list of all customers along with their order dates if they placed orders. If a customer has not placed an order, the order-related columns from the Orders table will be filled with NULL.

In the result, the word "left" refers to the order of the tables in the `FROM` clause, with the left table being the one from which we want all rows. The unmatched rows from the right table (Orders) will contain NULL values in columns that correspond to the join attributes.

Alternatively, you can use a **RIGHT OUTER JOIN** (or **RIGHT JOIN**) to achieve the same result by reversing the order of the tables in the `FROM` clause:

```sql
SELECT cFirstName, cLastName, orderDate
FROM orders o RIGHT OUTER JOIN customers c
ON o.custID = c.custID;
```

The choice between LEFT and RIGHT OUTER JOIN depends on which table's unmatched rows you want to include in the result.

It's important to note that an outer join makes sense when one side of the relationship has a minimum cardinality of zero. Otherwise, it would produce the same result as an inner join. The OUTER JOIN syntax can use either the `USING` or `ON` clause, similar to INNER JOIN. Additionally, there is a FULL OUTER JOIN, which includes unmatched rows from both tables with NULL values for the columns without matches. However, FULL OUTER JOIN is less commonly used in well-designed databases.