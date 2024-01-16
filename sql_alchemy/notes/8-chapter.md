Certainly, let's discuss rolling back changes in SQLAlchemy:

1. **Making Changes:**
   - Change the `name` attribute of `ed_user` to 'Edwardo'.
   - Add a new user, `fake_user`, with invalid data.

```python
ed_user.name = 'Edwardo'
fake_user = User(name='fakeuser', fullname='Invalid', nickname='12345')
session.add(fake_user)
```

2. **Flushing and Querying:**
   - Query the session to see the changes before committing.
   - Both the update for 'Edwardo' and the insertion of 'fakeuser' are visible.

```python
session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all()
```

3. **Rolling Back:**
   - Roll back the changes using `session.rollback()`.
   - After rollback, the changes made to `ed_user` are reverted, and `fake_user` is removed from the session.

```python
session.rollback()
```

4. **Checking Reverted Changes:**
   - Querying the session again shows that `ed_user` is back to 'ed', and `fake_user` is not in the session.

```python
ed_user.name
fake_user in session
```

5. **Querying Database after Rollback:**
   - Issuing a new SELECT query shows that the changes were not applied to the database; 'Edwardo' is not present, and 'fakeuser' was not inserted.

```python
session.query(User).filter(User.name.in_(['ed', 'fakeuser'])).all()
```

In summary, rolling back a session reverts any changes made within the current transaction. It's a way to discard modifications and return the session to its previous state. This is useful for handling errors or when changes should not be persisted to the database.