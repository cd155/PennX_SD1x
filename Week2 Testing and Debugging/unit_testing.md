# Classes video 2.1
- why is testing important
- different types of testing
- unit testing

### Software Testing
- integral part of development
- if you ship a software with bugs, you will lose money
- the easier a bug is detected, the less time it takes to fix it.
- huge job market for software testers
- in most organizations, a software developer is responsible for writing their own tests as well.

### Types of Testing
- **Black box** - does this method(or collection of methods) with this input lead to this specified output.
- **White box** - you *do* care how the thing being tested actually works. As an example, instead of just checking what the method returns, you are checking that its local variables are all having correct values.
- **Unit testing** - testing software components. For our purposes in this course we will usually call one method one unit.

### Unit testing advantages
- first line of defense. If you have code that fails a unit test, that code is not deployed to the production environment.
- modification of code becomes a less risky process.
- it represents a developers view of the software specifications
- if a bug shows up in code despite the unit tests, a new unit test can be added to ensure that situation is covered.

# Classes video 2.2
- write a unit test
- test driven development(TDD)

### Write the stub of method
```python
class BankAccount:
    def __init__(self, balance = None, account_owner = None):
        self.blance = balance
        self.account_owner = account_owner
```
Assume we want to add a method called deposit that will deposit a certain amount of money into the account.
- First decide on the specs
- parameter - amount to be deposited
- return None - the account balance will change
```python
def deposit(amount):
    # do not write anything here initially
```
The goal is to use the unit test to guide the development.

In cases where some value is being returned
- if it is an object return null
- if it is a primitive datatype just return some random value. 0 for integers for example.