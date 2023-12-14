CREATE DATABASE IF NOT EXISTS library;

USE library;

CREATE TABLE IF NOT EXISTS BookShop (
    BookCode INT PRIMARY KEY,
    Bookname VARCHAR(50),
    AuthorName VARCHAR(50)
);

DESCRIBE BookShop;