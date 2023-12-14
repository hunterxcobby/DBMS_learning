In MySQL, the NOT NULL constraint ensures that a column cannot contain NULL values, meaning it must always have a value. Think of it like having a mandatory field on a form that must be filled out.

In the example SQL code you provided:

```sql
CREATE TABLE People(Id INTEGER, LastName TEXT NOT NULL, FirstName TEXT NOT NULL, City VARCHAR(55));
```

This creates a table named People with two columns, LastName and FirstName, both of which cannot be NULL.

```sql
INSERT INTO People VALUES(1, 'Hanks', 'Robert', 'New York');
```

This insertion is successful because all columns, including LastName and FirstName, have valid values.

```sql
INSERT INTO People VALUES(1, NULL, 'Marianne', 'Chicago');
```

However, this insertion fails because you're trying to insert a row with a NULL value in the LastName column, which violates the NOT NULL constraint. It's akin to trying to submit a form without filling in a required field.

Remember, NOT NULL ensures that every record has a meaningful value in that column, enhancing data integrity.