# Class video 2.4
- reading an error stacktrace
- common exception you will encounter
    - ArrayIndexOutBoundsException 
        - python: list index out of range
    - StringIndexOutOfBoundsException
    - NullPointerException 
        - python: TypeError (invalid type such as NoneType) or ValueError (correct type, but the value is outside of the accepted domain)

### Debugging with stacktrace
- a sequence of method calls

### Where to begin the debugging process
- read the stacktrace top to bottom
- find the first line of code that you wrote
- exceptions "bubble up". More on this later
- some exception have self explanatory names
    - ArrayIndexOutBoundsException
    - ArithmeticException
- pay attention to any extra information being provided by the stacktrace

### NullPointerException
- one of the most common errors your see
- occurs when you are trying to access a method or instance variable from an object that is null.
- usually caused by
    - forgetting to call a constructor to first create the object
    - if you have a collection of data, then accessing beyond the first or last element of data.

# Class video 2.5
- debugging using the eclipse debugger
    - breakpoints
    - stepping into and over a method
    - the display

In most of cases, we write a simple print state
```python
print("I am here")
```
However, people usually forget to remove debugging the print statement.
### step into
will jump into next step, will go to other block of code
### step return
will return into previous step
### step over
remain in the same block, move to next line