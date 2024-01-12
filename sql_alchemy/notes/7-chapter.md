Here's an explanation of adding and updating objects in SQLAlchemy using the provided code:

1. **Adding an Object:**
   - Create a new `User` object, in this case, `ed_user`.
   - Add the object to the session using `session.add(ed_user)`. At this point, the object is in a pending state.
   - The session will issue the necessary SQL statements to persist the object when needed, using a process called a flush.

```python
ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
session.add(ed_user)
```

2. **Querying and Updating:**
   - Query the database to retrieve the user with the name 'ed'.
   - The session automatically flushes any pending changes before executing the query.
   - The returned `our_user` is the same instance as `ed_user`, thanks to SQLAlchemy's identity map.

```python
our_user = session.query(User).filter_by(name='ed').first()
```

3. **Batch Addition:**
   - Add multiple `User` objects using `session.add_all()`.

```python
session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Flintstone', nickname='freddy')])
```

4. **Updating an Object:**
   - Modify an attribute of an object, for example, changing Ed's nickname to 'eddie'.

```python
ed_user.nickname = 'eddie'
```

5. **Checking Changes:**
   - Check the session's `dirty` and `new` attributes to see which objects have been modified and which are pending insertion.

```python
session.dirty  # Modified objects
session.new    # Pending objects
```

6. **Committing Changes:**
   - Issue `session.commit()` to persist all changes to the database.
   - This flushes the remaining changes and commits the transaction.

```python
session.commit()
```

7. **Observing Object States:**
   - Objects in SQLAlchemy have different states (transient, pending, persistent, detached, and deleted).
   - Understanding these states is crucial for managing object lifecycles in the session.

```python
# Example of checking the state of an object
ed_user.id  # Accessing the ID triggers a reload if needed
```

In summary, the process involves creating, adding, querying, and updating objects within a session. The session handles the flushing of changes to the database and manages the lifecycle of objects through different states.