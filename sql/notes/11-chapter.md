

**1. Select (σ) Operator:**
   - Symbolized by σ, it acts like the SQL WHERE clause.
   - Written as σθe, where e is a relational algebra expression.
   - Picks tuples that satisfy a predicate θ.
   - The scheme of the result, σθr, is the same as the original relation r.
   - The result includes all tuples of r that satisfy the predicate θ.

**2. Project (π) Operator:**
   - Symbolized by π, it's similar to the SQL SELECT clause.
   - Written as πXe, where X is a subset of attributes, and e is a relational algebra expression.
   - Picks attributes specified in X from the original relation or expression.
   - The scheme of the result, πXr, is X.
   - If X is a super key of r, the result has the same number of tuples as r; otherwise, duplicates are eliminated, ensuring the result is a set.

**Function Composition:**
   - You can use function composition by applying the project operator to the result of the select operator.
   - For example: πXσθr, where X is the subset of attributes you want, and θ is the predicate for selecting tuples.

**Relational Algebra vs. SQL:**
   - Relational algebra is used to declare what is to be retrieved without specifying how.
   - SQL is declarative and leaves it to the database system to determine how to retrieve the result.
   - SQL is often translated into relational algebra in relational database systems.

**Note:**
   - Uppercase letters are used for relation schemes (R, S, T, U), and lowercase letters for relations (r, s, t, u).
   - σ and π are unary operators, taking a single relation or expression as their operand.