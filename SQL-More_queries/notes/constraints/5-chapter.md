The ENUM constraint in MySQL allows a column to have a value chosen from a predefined list of permitted values. Let's explore the example with the Shops table:

```sql
CREATE TABLE Shops(Id INTEGER, Name VARCHAR(55), Quality ENUM('High', 'Average', 'Low'));
```

This creates the Shops table with columns Id, Name, and Quality. The Quality column is defined as an ENUM, permitting only three specified values: 'High', 'Average', or 'Low'.

```sql
INSERT INTO Shops VALUES(1, 'Boneys', 'High');
INSERT INTO Shops VALUES(2, 'AC River', 'Average');
INSERT INTO Shops VALUES(3, 'AT 34', '**');
```

The first two insertions are successful, as they provide valid values ('High' and 'Average') according to the specified ENUM. However, the third insertion attempts to insert the value '**', which is not among the permitted values. In this case, an empty string is inserted instead.

```sql
SELECT * FROM Shops;
```

The SELECT statement displays the contents of the Shops table:

```
+------+----------+---------+
| Id   | Name     | Quality |
+------+----------+---------+
|    1 | Boneys   | High    |
|    2 | AC River | Average |
|    3 | AT 34    |         |
+------+----------+---------+
```

As seen in the result, the third row has an empty value in the Quality column since the attempted value was not in the ENUM list.

Using ENUM constraints helps restrict the possible values a column can take, ensuring data consistency and integrity.