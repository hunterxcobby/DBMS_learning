In SQL, the backtick (or backquote) character is used as an identifier delimiter, especially in MySQL and MariaDB, to represent database, table, or column names. It is not part of the SQL standard and is specific to certain database systems.

On the other hand, single quotes (apostrophes) are used to denote string literals in SQL. When you enclose a value in single quotes, it is treated as a literal string rather than an identifier.

Now, let's look at your two queries:

1. **Query with Backticks:**
   ```sql
   SELECT COUNT(DISTINCT(`price`)) FROM `products`;
   ```
   This query counts the distinct values in the `price` column of the `products` table. The backticks indicate that `price` is the name of a column.

2. **Query with Single Quotes:**
   ```sql
   SELECT COUNT(DISTINCT('price')) FROM `products`;
   ```
   This query counts the distinct values in the string literal `'price'`. It does not refer to the column named `price` but rather counts the distinct values of the literal string `'price'`, which is why you get a count of 1.

In summary, the backticks are used for identifiers (like column names), and single quotes are used for string literals. The use of backticks is specific to certain database systems like MySQL and MariaDB. Mixing them up can lead to different interpretations by the database engine.