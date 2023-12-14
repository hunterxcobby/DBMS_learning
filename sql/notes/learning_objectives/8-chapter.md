### Subqueries:

Subqueries, also known as nested queries, are queries embedded within another query. They are used to retrieve data that will be used in the main query as a condition to further restrict the data to be retrieved. Here's a basic example:

```sql
SELECT FirstName, LastName
FROM Employees
WHERE DepartmentID IN (SELECT DepartmentID FROM Departments WHERE DepartmentName = 'Sales');
```

In this example, the subquery `(SELECT DepartmentID FROM Departments WHERE DepartmentName = 'Sales')` retrieves the DepartmentID for the 'Sales' department, and the main query then retrieves employees from that department.

### MySQL Functions:

MySQL provides a variety of functions that perform operations on data. Here are a few examples:

#### 1. **String Functions:**

- **CONCAT():** Concatenates two or more strings.
  ```sql
  SELECT CONCAT(FirstName, ' ', LastName) AS FullName FROM Employees;
  ```

- **SUBSTRING():** Extracts a portion of a string.
  ```sql
  SELECT SUBSTRING(CompanyName, 1, 5) AS ShortName FROM Customers;
  ```

#### 2. **Numeric Functions:**

- **SUM():** Calculates the sum of values in a numeric column.
  ```sql
  SELECT SUM(OrderAmount) AS TotalSales FROM Orders;
  ```

- **AVG():** Calculates the average value of a numeric column.
  ```sql
  SELECT AVG(Salary) AS AvgSalary FROM Employees;
  ```

#### 3. **Date Functions:**

- **NOW():** Returns the current date and time.
  ```sql
  SELECT NOW() AS CurrentDateTime;
  ```

- **DATE_FORMAT():** Formats a date as specified.
  ```sql
  SELECT DATE_FORMAT(OrderDate, '%Y-%m-%d') AS FormattedDate FROM Orders;
  ```

#### 4. **Aggregate Functions:**

- **COUNT():** Counts the number of rows in a result set.
  ```sql
  SELECT COUNT(*) AS NumberOfOrders FROM Orders;
  ```

- **MAX() and MIN():** Retrieve the maximum or minimum value in a column.
  ```sql
  SELECT MAX(Salary) AS MaxSalary FROM Employees;
  ```

#### 5. **Math Functions:**

- **ROUND():** Rounds a numeric value to a specified number of decimal places.
  ```sql
  SELECT ROUND(AVG(ProductPrice), 2) AS AvgRoundedPrice FROM Products;
  ```

These are just a few examples, and MySQL offers many more functions for various purposes. Understanding the context in which each function is used is essential for effective query building.