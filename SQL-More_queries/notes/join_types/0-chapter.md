**Inner Join:**

An **INNER JOIN** is a type of join that returns only the rows that have matching values in both tables. It combines rows from two or more tables based on a related column between them. The result includes only the rows where the specified condition is true.

Here are different ways to express INNER JOIN in SQL:

1. **Natural Join:**
   - Automatically picks the join attributes with the same name in both tables (intersection of the schemes).
   - Produces only one copy of those attributes in the result table.
   ```sql
   SELECT cFirstName, cLastName, orderDate
   FROM customers NATURAL JOIN orders;
   ```

2. **INNER JOIN with USING Clause:**
   - Specifies the join attributes in a `USING` clause.
   - Produces only one copy of the join attributes in the result table.
   ```sql
   SELECT cFirstName, cLastName, orderDate
   FROM customers INNER JOIN orders
   USING (custID);
   ```

3. **INNER JOIN with ON Clause:**
   - Specifies the join attributes and the join condition (usually equality) in an `ON` clause.
   - Requires qualifying join attribute names with their table names.
   - Allows joining on attributes with different names in the tables.
   ```sql
   SELECT cFirstName, cLastName, orderDate
   FROM customers INNER JOIN orders
   ON customers.custID = orders.custID;
   ```

4. **INNER JOIN with Table Aliases:**
   - Specifies table aliases for brevity.
   - Qualifies join attribute names with the aliases.
   ```sql
   SELECT cFirstName, cLastName, orderDate
   FROM customers c INNER JOIN orders o
   ON c.custID = o.custID;
   ```

5. **Pre-1992 Syntax:**
   - Uses a comma to list tables and places the join condition in the `WHERE` clause.
   - Not recommended for modern usage.
   ```sql
   SELECT cFirstName, cLastName, orderDate
   FROM customers c, orders o
   WHERE c.custID = o.custID;
   ```

Each of these syntax variations achieves the same result, but the choice may depend on system support, personal preference, or specific requirements. The more explicit forms, like INNER JOIN with ON clause, are often preferred for clarity and to avoid potential pitfalls associated with automatic attribute matching in natural joins.