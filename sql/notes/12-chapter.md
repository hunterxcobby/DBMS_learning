the relational algebra (RA) expressions that match the SQL statements for retrieving customers in a specified zip code (e.g., zip code 90840).

**1. Retrieve All Customers (Equivalent to SQL Initial Query):**
   - RA Expression: `customers`
   - Scheme: Same as the Customers scheme.

**2. Equivalent to SQL Refinement #2 (Filter by Zip Code):**
   - RA Expression: `σcZipCode='90840'customers`
   - Scheme: Same as the Customers scheme.
   - Explanation: This expression uses the σ operator to select tuples from the "customers" relation where the cZipCode attribute equals '90840'.

**3. Equivalent to SQL Refinement #3 (Select Specific Columns):**
   - RA Expression: `πcLastName, cFirstName, cPhone σcZipCode='90840'customers`
   - Scheme: Subset of the Customers scheme, containing only cLastName, cFirstName, and cPhone.
   - Explanation: This expression uses the π operator to project specific attributes from the result set of the previous expression.

**Note:**
   - In relational algebra, the results are sets of tuples, and there's no inherent order specified for tuples. This is unlike SQL with its ORDER BY clause.
   - RA expressions are used to declare what to retrieve without specifying how, leaving it to the system to determine the retrieval strategy.

These RA expressions mirror the SQL statements for retrieving customers in a specified zip code, providing a formalized way to express the same logic.