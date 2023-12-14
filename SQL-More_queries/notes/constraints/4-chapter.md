A FOREIGN KEY in MySQL establishes a referential constraint between two tables, where the foreign key in one table points to the PRIMARY KEY in another. This ensures a connection between related data in different tables. Let's illustrate this with the Authors and Books tables:

```sql
CREATE TABLE Authors(AuthorId INTEGER PRIMARY KEY, Name VARCHAR(70)) type=InnoDB;
```

This creates the Authors table, where AuthorId is the primary key.

```sql
CREATE TABLE Books(BookId INTEGER PRIMARY KEY, Title VARCHAR(50), AuthorId INTEGER, FOREIGN KEY(AuthorId) REFERENCES Authors(AuthorId)) type=InnoDB;
```

Here, the Books table includes a foreign key, AuthorId, which references the primary key (AuthorId) in the Authors table.

Foreign key enforcement means that when inserting a row into the Books table, the AuthorId must exist in the Authors table. In other words, you cannot associate a book with an author that doesn't exist in the Authors table. This constraint helps maintain data integrity and ensures that relationships between tables remain valid.

In practical terms, it prevents scenarios where you might try to insert a book with an AuthorId that does not correspond to any author in the Authors table. This ensures consistency in your database relationships.