# MySQL Workbench Setup

A basic SQL script to verify that MySQL Workbench is installed and working correctly.

## What It Does

The script walks through the core CRUD operations on a simple `students` table:

1. **Create** a test database (`test_db`) and a `students` table
2. **Insert** a sample record
3. **Read** all records with `SELECT`
4. **Update** a field value
5. **Delete** the record and confirm it's gone

## How to Run

1. Open **MySQL Workbench** and connect to your local MySQL server
2. Open `MySQL_Workbench_Setup.txt`
3. Run the script (or paste it into a query tab and execute)

## Schema

```sql
CREATE TABLE students (
    id   INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age  INT
);
```

## Tech

- MySQL 8+
- MySQL Workbench
