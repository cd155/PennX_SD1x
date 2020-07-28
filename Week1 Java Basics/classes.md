Classes video 1.6
What is a class?
Short answer: a collection of information

Example
Model a parking lot with spaces for cars
Java does not have a car datatype
Java does not have a Parking Lot datatype
Classes allow you to create your own datatype.
To model a problem in the objected programming world, the nouns in the problem will typically be converted into classes

Creating a Car class (instance variables)
* instance variables are basically the properties of an "instance" of the class in question
* what properties does a car have?
* Example - make, model, year of manufacture, is it new or used?, miles, owner.
* "A 2014 second hand Audi A4"

Note: Python don't explicitly distinguish datatype, in order to focus have right data type for each property, you can add error exceptions. 

Doing something with a car (add new function call sell)
* Sell the car
* The nouns in a problem get turned into classes
* The verbs in a problem get turned into methods
* Methods are similar to functions that you might have seen in other languages.

A method with a return Statement (add new function to calulcation whether this car was manufactured older than ten years)
* We want to know whether the car is older thant 10

Classes video 1.7
what is constructor, "this" keyward (equavlent to self in python), using in built classes

A constructor is code to creat an object.
The syntax for a constructor is:
Class_Name(parameters):
    ...code...

In Java or mosf of C famliy language, the ClassName has to be the same as the class that the constructor occurs in, but Python you can add init method to creating a class.

The parameters are a comma-separated list of variable declarations (whatever you want give to this class, transport to the instance)

The this (self) keyword
* this refers to the current instance of the class, the object in question
* it is generally used for two purposes
    1. disambiguate between an instance variable and a local variable, especially in constructors
    2. when the entire current object has to be passed to a method

Classes video 1.8
writing methods other than a constructor, scope, return statement

A method has the syntax:
def method-name(parameters):
    method-variables

* a method may have local(method) variables
* formal parameters are a kind of local variable
    def add(m, n):
        sum = m + n
        return sum
* m, n, and sum are local variables
    1. the scope of m, n, and sum is the method
    2. these variables car only be used in the method, nowhere else
    3. the names can be re-used elsewhere, for other variables

Declarations in a method
* the scope of formal parameters is the entire method
* the scope of a variable in a block starts where you define it and extends to the end of the block
    if x > y:
        larger = x
    else:
        larger = y
    return larger

In Java: Returning a result from a method
* if a method is to return a result, it must specify the type of the result: boolean isAdult( ...
* you must use a return statement to exit the method with a result of the correct type: return age >= magicAge;

In contrast, Python doesn't require the type of reults, and you can return almost anything from a function

In Python, it is possible to compose a function without a return statement. Functions like this are called void, and they return None, Python's special object for "nothing". Here's an example of a void function:
    def sayhello(who):
        print("What a lovely day.")

Program structure
* a program consists of one or more classes
* Typically, each class is in a separate .Java file

class Someclass:
    # instance variables
    # one or more constructors
    # methods
    # optionally a main method

null(in Java)
* if you declare a variable to have a given obejct type, 
for example: Car myCar;
* if you have not yet assigned a value to it,
for example myCar = new Car();
* then the value of variable is null
* null is a legal value, but there isn't much you can do with it
    1. it's an error to refer to its fields, because it has none
    2. it's an error to send a message to it, because it has no methods
    3. the error you will see is NullPointerException

In Pyhton, there is no such thing as "variable declaration" or "variable initialization". 
Python variables do not need explicit declaration to reserve memory space. The declaration happens automatically when you assign a value to a variable. The equal sign (=) is used to assign values to variables.
We can set default values in the init function