# Bank Account System (Python)

## Overview

This project is a simple simulation of a banking system using Python classes.
It demonstrates object-oriented programming concepts such as classes, methods, and method chaining.

---

## Classes

### 1. BankAccount

Represents a bank account with basic operations:

* `deposit(amount)` → Adds money to the balance
* `withdraw(amount)` → Withdraws money (charges $5 if insufficient funds)
* `display_account_info()` → Displays current balance
* `yield_interest()` → Applies interest if balance is positive

---

### 2. User

Represents a user who owns a bank account:

* `make_deposit(amount)` → Deposits money into account
* `make_withdrawal(amount)` → Withdraws money from account
* `transfer_money(other_user, amount)` → Transfers money to another user
* `display_user_balance()` → Displays user's balance

---

## Example Usage

```python
user_1 = User("mahmoud", "Mahmoud.Shalayel@axsos.academy")

user_1.make_deposit(100)\
      .make_withdrawal(20)\
      .display_user_balance()
```

---

## Features

* Method chaining for cleaner code
* Basic validation for insufficient funds
* Simple money transfer between users

---

## Technologies

* Python 3
* Object-Oriented Programming (OOP)

---

## Output Example

```
User: mahmoud, Balance: $80
```

---

## Notes

* Interest is applied only if balance is greater than 0
* Withdrawal with insufficient funds charges a $5 fee
* Each user has one bank account by default
