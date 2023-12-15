When dealing with a well-designed and linked database, retrieving information from multiple tables is a common and powerful operation. Let's explore an example where we want to retrieve a list of all products purchased by a specific customer in the order entry model:

### Relation Scheme Diagram:
![Sales model relation scheme diagram](image_link)
* [Large image](image_link)
* [Description (text)](image_description_link)

### Relational Algebra (RA) Expression:
```sql
πcLastName, cFirstName, prodName σcFirstName='Alvaro' ∧ cLastName='Monge' (customers ⨝ orders ⨝ orderlines ⨝ products)
```

### Explanation:
- The projection (\(π\)) includes the customer's last name (\(cLastName\)), first name (\(cFirstName\)), and product name (\(prodName\)).
- The selection (\(σ\)) specifies the condition that the customer's first name is 'Alvaro' and last name is 'Monge'.
- The joins (\(⨝\)) link the customers, orders, orderlines, and products tables based on their primary key-foreign key relationships.

### SQL Query Steps:
1. **Retrieve All Linked Data:**
   ```sql
   SELECT *
   FROM customers 
     NATURAL JOIN orders
     NATURAL JOIN orderlines
     NATURAL JOIN products;
   ```
   *Note: Your database system might not support the NATURAL JOIN syntax, and we'll address this when discussing join types. The natural joins work in this example because there are no non-primary key/foreign key attributes with the same name across tables.*

2. **Restrict Rows to One Customer:**
   ```sql
   SELECT *
   FROM customers 
     NATURAL JOIN orders
     NATURAL JOIN orderlines
     NATURAL JOIN products
   WHERE cFirstName = 'Alvaro' AND cLastName = 'Monge';
   ```

3. **Select Desired Columns:**
   ```sql
   SELECT cFirstName, cLastName, prodName
   FROM customers 
     NATURAL JOIN orders
     NATURAL JOIN orderlines
     NATURAL JOIN products
   WHERE cFirstName = 'Alvaro' AND cLastName = 'Monge';
   ```

### Result Set:
```
Products purchased
Alvaro  Monge  Hammer, framing, 20 oz.
Alvaro  Monge  Hammer, framing, 20 oz.
Alvaro  Monge  Screwdriver, Phillips #2, 6 inch
Alvaro  Monge  Screwdriver, Phillips #2, 6 inch
Alvaro  Monge  Pliers, needle-nose, 4 inch
```

This result set provides the list of products purchased by the specific customer 'Alvaro Monge' based on the conditions specified in the query. The step-by-step procedure ensures that the correct data is retrieved and displayed.