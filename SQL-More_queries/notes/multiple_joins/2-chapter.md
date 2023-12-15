In database design, a **superkey** is a set of one or more attributes (columns) that can be used to uniquely identify a tuple (row) in a relation (table). Essentially, a superkey is a set of attributes that, taken together, uniquely identifies a record in a table. It can include one or more columns, and it doesn't necessarily have to be the smallest possible set of attributes that uniquely identifies a tuple.

There are two main types of superkeys:

1. **Candidate Key:** A candidate key is a minimal superkey, meaning it is a superkey for which no proper subset is also a superkey. In other words, it is a set of attributes that uniquely identifies a tuple, and removing any attribute from the set would cause it to lose its uniqueness property.

2. **Primary Key:** A primary key is a candidate key chosen to uniquely identify each tuple in a relation. It is the key that is selected to be the main identifier for a table. By definition, a primary key is both unique and minimal, and it must not contain any null values.

Here's a simple example:

Consider a relation representing students with attributes (columns) such as StudentID, Name, and Email. The combination of StudentID and Email could form a superkey because it uniquely identifies each student. However, removing either attribute from the set would still result in a superkey. In this case, {StudentID, Email} is a candidate key, and if we choose one of them (let's say, StudentID) as the primary key, it becomes the primary key for the relation.

In summary, a superkey is a set of attributes that uniquely identifies a tuple, and a candidate key is a minimal superkey, with the primary key being the chosen candidate key for a relation.