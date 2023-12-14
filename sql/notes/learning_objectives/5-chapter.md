
### Creating or Altering a Table (DDL - Data Definition Language):

To **create** a table:

```sql
CREATE TABLE TableName (
    Column1 DataType1,
    Column2 DataType2,
    ...,
    CONSTRAINT ConstraintName PRIMARY KEY (Column1)
);
```

To **alter** a table (add a new column, for example):

```sql
ALTER TABLE TableName
ADD COLUMN NewColumn DataType;
```

### Selecting Data from a Table (DML - Data Manipulation Language):

To **select** data:

```sql
SELECT Column1, Column2
FROM TableName
WHERE SomeCondition;
```

### Inserting Data into a Table:

To **insert** data:

```sql
INSERT INTO TableName (Column1, Column2, ...)
VALUES (Value1, Value2, ...);
```

### Updating Data in a Table:

To **update** data:

```sql
UPDATE TableName
SET Column1 = NewValue1, Column2 = NewValue2
WHERE SomeCondition;
```

### Deleting Data from a Table:

To **delete** data:

```sql
DELETE FROM TableName
WHERE SomeCondition;
```

Remember to replace `TableName`, `Column1`, `Value1`, etc., with your actual table and column names or values. Additionally, ensure that the data types match appropriately.

Analogy: Think of a table as a spreadsheet, where each row is a record and each column is a different attribute. The SQL commands are like specific actions you perform on the spreadsheet, such as adding a new column, selecting certain rows, or updating values in cells.