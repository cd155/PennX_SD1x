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
class Bank_Account:
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

# Classes video 2.3A
- using unittest
- complete example of Test Driven
- Development
### XP approach to testing
- extreme programming
- if code has no automated test case, it is assumed not to work
- a test framework is used so that automated testing can be done after every small change to the code.
- this may be as often as every 5 or 10 minutes
- if a bug is found after development, a test is created to keep the bug from coming back.
### A simple example
- suppose you have a class Arithmetic with methods multiply(x, y), and is_positive(x)
```python
class TestCase(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(4, Arithmetic(x, y))
        self.assertEqual(-15, Arithmetic(3, -5))

    def test_is_positive(self):
        self.assertTrue(Arithmetic.is_positive(5))
        self.assertFalse(Arithmetic.is_positive(-5))
        self.assertFalse(Arithmetic.is_positive(0))
```
### Example: a counter class
- we'll create a simple counter class
    - the constructor will create a counter and set it to zero
    - the increment method will add 1 to the counter and return the new value
    - the decrement method will subtract 1 from the counter and return the new value
- we write the test methods before we write the code
    - write the method stubs
    - let the IDE take care of generating the test method stubs
```python
class TestCounterCase(unittest.TestCase):
    # start test
    def setUp(self):
        self.counter = Counter()

    # end test
    def tearDown(self):
        self.counter = None

    def test_increment(self):
        self.assertEqual(self.counter.increment(), 1)
        self.assertEqual(self.counter.increment(), 2)

    def test_decrement(self):
        self.assertEqual(self.counter.decrement(), -1)
```
### the actual Counter class
```python
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def decrement(self):
        self.count -= -1
        return self.count
    
    def get_count(self):
        return self.count
```
### Quick verison of the equals method
- you can compare primitives with ==
- Java has a method x.equals(y), for comparing objects (use assertEqual(x, y) in Python)
    - this method works great for springs and few other Java classes
    - for object of classes that you created, you have to define equals
- to define equals for your own objects, define exactly this method. The argument must be of type Object, which isn't what you want, so you must cast it to the correct type(say, Person):
```python
def equals(self, object something):
    p = (Person)something
    return self.name == p.name
```
### Assert Methods
```python
assertEqual(x, y)
assertEqual(x, y, "Message you can print out")
```
expected and actual must be both objects or the same primitive type

for objects, uses your equals methods, if you have defined it properly, as described previously
```python
assertEqual(x, None)
```
Asserts that the object is null(undefined)