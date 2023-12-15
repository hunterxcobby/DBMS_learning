The `DISTINCT` keyword in SQL is used to eliminate duplicate rows from the result set of a query. Let's explore its application in the context of your example:

### Revised SQL Query with DISTINCT:
```sql
SELECT DISTINCT cFirstName, cLastName, prodName
FROM customers 
  NATURAL JOIN orders
  NATURAL JOIN orderlines
  NATURAL JOIN products
WHERE cFirstName = 'Alvaro' AND cLastName = 'Monge'
ORDER BY prodName;
```

### Explanation:
- The `DISTINCT` keyword is added to the `SELECT` clause to ensure that only unique combinations of `cFirstName`, `cLastName`, and `prodName` are included in the result set.
- The `ORDER BY` clause is used to arrange the result set in alphabetical order based on the product name (`prodName`).

### Result Set:
```
Distinct products
Alvaro	Monge	Hammer, framing, 20 oz.
Alvaro	Monge	Pliers, needle-nose, 4 inch
Alvaro	Monge	Screwdriver, Phillips #2, 6 inch
```

### Explanation of the Need for DISTINCT:
- Without the `DISTINCT` keyword, the result set might contain duplicate rows, as seen in the initial query.
- The reason for duplicates is that the `SELECT` clause eliminated unwanted columns but retained all rows picked by the `WHERE` clause, leading to redundancy.
- Unlike in Relational Algebra, SQL result sets are not implicitly treated as sets, and duplicates may occur.

### Cautionary Note:
- Using `DISTINCT` should be judicious. If the `SELECT` attribute list forms a super key of the result set, the `DISTINCT` keyword is not necessary and should be omitted.
- Relying on `DISTINCT` unnecessarily can be a sloppy approach and may hinder a deeper understanding of the query.
- Removing duplicates can be resource-intensive, especially with large datasets. It's essential to consider the performance impact and use it only when necessary.

In summary, the `DISTINCT` keyword is a useful tool to ensure uniqueness in the result set, but it should be applied thoughtfully based on the characteristics of the query and the desired outcome.