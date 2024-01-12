In this section, you are introduced to creating an instance of the mapped class (`User` in this case) using SQLAlchemy's Declarative system.

1. **Creating an Instance:**
   - An instance of the `User` class is created with the provided values for the attributes (`name`, `fullname`, `nickname`).

```python
ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
```

2. **Accessing Attributes:**
   - You can access the attributes of the created instance using dot notation.
   - For example, `ed_user.name` gives you the value `'ed'`, and `ed_user.nickname` gives you `'edsnickname'`.

```python
ed_user.name       # Output: 'ed'
ed_user.nickname   # Output: 'edsnickname'
```

3. **Default Value for Unassigned Attribute (`id`):**
   - Although you didn't explicitly assign a value to the `id` attribute, SQLAlchemy's instrumentation system provides a default value of `None` when you access it.

```python
str(ed_user.id)    # Output: 'None'
```

4. **`__init__()` Method:**
   - The `User` class has a default constructor (`__init__()` method) provided by the Declarative system.
   - This constructor automatically accepts keyword arguments that match the columns mapped to the class.

```python
def __init__(self, name, fullname, nickname):
    self.name = name
    self.fullname = fullname
    self.nickname = nickname
```

5. **Custom `__init__()` Method:**
   - You are free to define your own explicit `__init__()` method on the class, which will override the default provided by Declarative.

```python
def __init__(self, name, fullname, nickname, custom_arg):
    self.name = name
    self.fullname = fullname
    self.nickname = nickname
    self.custom_arg = custom_arg
```

This section illustrates the process of creating instances of mapped classes, accessing their attributes, and the default behavior of attribute values, including the option to define a custom constructor (`__init__()` method) if needed.