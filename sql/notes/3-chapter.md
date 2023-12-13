the "ALTER TABLE" statement. It's like giving your table a makeover. You use it to set rules, like saying, "This column is super important, so it's a primary key," or "This column connects to another table."

For example, let's say you want to make the "CustomerID" column in your "Customers" table a primary key. You'd do it like this:

```sql
ALTER TABLE Customers
ADD CONSTRAINT Customers_pk PRIMARY KEY (CustomerID);
```

Here, you're saying, "Hey, alter the 'Customers' table. Add a rule (constraint) called 'Customers_pk' that says 'CustomerID' is a primary key." Naming conventions are handy; here we use 'tablename_pk' to keep things clear.

This helps the database organize and understand relationships. If you want to set rules during the table creation itself, you can do that with the "CREATE TABLE" statement, but "ALTER TABLE" is like tweaking things afterward.