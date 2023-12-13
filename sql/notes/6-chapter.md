**1. Insert Statement:**
It's like adding new stuff to your table. Imagine your table is a collection of boxes, and you're putting things into each box. Here's how you do it:

```sql
INSERT INTO <table name>
VALUES (<value 1>, ..., <value n>);
```

Each `<value>` is like the item you're putting in a box. Make sure the order and type match the boxes in your table. If it's a word (character), put it in single quotes. If it's a number, no quotes. If it's a date, follow a specific format.

Yes, you need a separate "INSERT" for each item you want to add.

**2. Update Statement:**
Now, let's say you want to change something in a box you already have. It's like saying, "Hey, update this box with a new thing." Here's how:

```sql
UPDATE <table name>
SET <attribute> = <expression>
WHERE <condition>;
```

You're telling the database, "In the 'table,' set the 'attribute' to a new 'expression' where the 'condition' is met."

For example:
```sql
UPDATE Products
SET Price = 20
WHERE Category = 'Electronics';
```

This says, "In the 'Products' table, set the 'Price' to 20 where the 'Category' is 'Electronics'."

You can change one thing or many at once using commas. It's like updating your boxes in bulk.