To create a database in MySQL, you can use the `CREATE DATABASE` statement. Here's a basic guide on how to do it:

1. **Access MySQL:**
   - Open a command-line interface or a MySQL client that allows you to execute queries.

2. **Log in to MySQL:**
   - Enter your MySQL username and password to log in. For example:
     ```sql
     mysql -u your_username -p
     ```

3. **Create a Database:**
   - Use the following command to create a new database. Replace `your_database` with the desired name for your database.
     ```sql
     CREATE DATABASE your_database;
     ```

4. **Verify Creation:**
   - You can check if the database has been created successfully using the following command:
     ```sql
     SHOW DATABASES;
     ```

   - Your newly created database should be listed in the output.

Here's an example with specific names:

```sql
CREATE DATABASE mydatabase;
```

This creates a database named "mydatabase."

Remember to use semicolons at the end of each SQL statement to indicate the end of the command.

If you encounter any permission issues, ensure that your MySQL user has the necessary privileges to create databases. If not, you might need to log in as a user with administrative privileges (`root` user) or ask your database administrator for assistance.