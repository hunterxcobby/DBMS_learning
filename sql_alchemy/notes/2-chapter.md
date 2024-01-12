
### Declare a Mapping with Declarative:

**1. Import Declarative Base:**
   - Start by importing the `declarative_base` function.

```python
>>> from sqlalchemy.ext.declarative import declarative_base
>>> Base = declarative_base()
```

**2. Define Mapped Class:**
   - Define a class that will be mapped to a database table (e.g., `User` for a 'users' table).
   - Specify the table name and column details.

```python
>>> from sqlalchemy import Column, Integer, String

>>> class User(Base):
...     __tablename__ = 'users'
...
...     id = Column(Integer, primary_key=True)
...     name = Column(String)
...     fullname = Column(String)
...     nickname = Column(String)
...
...     def __repr__(self):
...         return "<User(name='%s', fullname='%s', nickname='%s')>" % (
...             self.name, self.fullname, self.nickname)
```

   - The `__tablename__` attribute specifies the table name.
   - Columns are defined using `Column` with their respective data types.
   - At least one column must be part of the primary key.

**3. Instrumentation:**
   - When the class is constructed, Declarative replaces `Column` objects with special Python accessors (descriptors), a process known as instrumentation.
   - This allows us to interact with the table in a SQL context and persist/load column values from the database.

**4. Optional: Additional Class Attributes/Methods:**
   - The mapped class remains mostly a standard Python class.
   - You can define additional attributes and methods needed by your application.

**5. Represent Data (Optional):**
   - Optionally, include a `__repr__` method for a nicely formatted representation of instances.

**Tip:**
   - The `__repr__` method is optional and used for better representation in examples.

### Important Notes:
   - A minimum requirement is the `__tablename__` attribute and at least one column as part of the primary key.
   - SQLAlchemy does not assume anything about the table; you define names, data types, and constraints.

### Additional Resources:
   - [Mixin and Custom Base Classes](https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/mixins.html)
   - [How do I map a table that has no primary key?](https://docs.sqlalchemy.org/en/13/faq/ormconfiguration.html#how-do-i-map-a-table-that-has-no-primary-key)

