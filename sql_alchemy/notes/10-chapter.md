1. **Equal (`==`) Operator:**
   - Filter users with the name 'ed'.
```python
query.filter(User.name == 'ed')
```

2. **Not Equal (`!=`) Operator:**
   - Filter users not named 'ed'.
```python
query.filter(User.name != 'ed')
```

3. **Like Operator:**
   - Filter users with names containing 'ed'.
```python
query.filter(User.name.like('%ed%'))
```

4. **Case-Insensitive Like Operator (`ilike`):**
   - Case-insensitive version of `like`.
```python
query.filter(User.name.ilike('%ed%'))
```

5. **In Operator:**
   - Filter users with names 'ed', 'wendy', or 'jack'.
   - Use a subquery for more complex conditions.
   - Use `tuple_()` for composite queries (multi-column).
```python
query.filter(User.name.in_(['ed', 'wendy', 'jack']))

# Subquery
query.filter(User.name.in_(
    session.query(User.name).filter(User.name.like('%ed%'))
))

# Composite Query
from sqlalchemy import tuple_
query.filter(
    tuple_(User.name, User.nickname).\
    in_([('ed', 'edsnickname'), ('wendy', 'windy')])
)
```

6. **Not In Operator:**
   - Filter users with names not 'ed', 'wendy', or 'jack'.
```python
query.filter(~User.name.in_(['ed', 'wendy', 'jack']))
```

7. **Is Operator:**
   - Filter users with a `None` name.
```python
query.filter(User.name == None)

# Alternatively
query.filter(User.name.is_(None))
```

8. **Is Not Operator:**
   - Filter users with a non-`None` name.
```python
query.filter(User.name != None)

# Alternatively
query.filter(User.name.isnot(None))
```

9. **AND Operator:**
   - Use `and_()` or chain multiple filter conditions.
```python
from sqlalchemy import and_

# Using and_()
query.filter(and_(User.name == 'ed', User.fullname == 'Ed Jones'))

# Using multiple filter conditions
query.filter(User.name == 'ed', User.fullname == 'Ed Jones')

# Chaining
query.filter(User.name == 'ed').filter(User.fullname == 'Ed Jones')
```

10. **OR Operator:**
    - Use `or_()` for OR conditions.
```python
from sqlalchemy import or_
query.filter(or_(User.name == 'ed', User.name == 'wendy'))
```

11. **Match Operator:**
    - Filter users with names matching 'wendy'.
    - Uses a database-specific MATCH or CONTAINS function.
```python
query.filter(User.name.match('wendy'))
```

These operators provide a powerful set of tools for constructing complex queries with various conditions.