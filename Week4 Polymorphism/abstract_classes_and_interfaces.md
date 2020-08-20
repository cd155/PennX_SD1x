# Class video 4.4
- Abstract classes

### Abstract methods
- An abstract method is a method without any implementation
    - public abstract void draw(int size);
- Notice that the body of the method is completely missing. It is just the first line and then is terminated with a;

### Abstract class
- Any class containing an abstract method is an abstract class
- You must declare the class with the keyword abstract
    - abstract class MyClass{...}
- An abstract class is incomplete
- It has "missing" method bodies
- You cannot instantiate

### Using an Abstract class
- Extend an abstract class before you can use it
- If the subclass defines all the inherited abstract methods, it is "complete" and can be instantiated.
- If the subclass does not define all the abstract methods then it too must be abstract.
- You can declare a class to be abstract even if it does not have any abstract methods.
    - This prevents the class from being instantiated

### Why have an abstract class
- Suppose you wantted to create a class Shape, with subclasses Oval, Rectangle, Triangle, Hexagon, etc.
- You don't want to allow creation of a "Shape"
    - Only particular shapes make sense, not generic ones
    - If Shape is abstract, you can't create a new Shape
    - You can create a new Oval, a new Rectangle, etc.
- Abstract classes are good for defining a general category containing specific, "concrete" classes.

### Example abstract class
```Java
public abstract class Animal{
    abstract int eat ();
    abstract void breathe();
}
```
- This class cannot be instantiated
- Any non-abstract subclass of Animal must provide the eat() and breathe() methods

### Potential Problem
```Java
class Shape{...}
class Star extends Shape{
    void draw(){...}
}
class Crescent extends Shape{
    void draw(){...}
}
```
- Shape someShape = new Star();
    - this is legal, because a Star is a Shape
- someShape.draw();
    - This is a syntax error, because some Shape might not have a draw() method
    - Remember: A class knows its superclass, but not its subclasses.

### Usage of Abstract methods
- Suppose you are making a GUI, and you want to draw a number of different "shapes" (marbles, pegs, frogs, stars, etc.)
    - Each class(Marble, Peg, etc) has a draw method
    - You make these subclasses of a class Shape, so that you can create an ArrayList<Shape> shapes to hold the various things to be drawn
    - You would like to do
        - for(Shape s: shapes) s.draw();
    - This isn't legal
- Every class "knows" its superclass, but a class doesn't "know" its subclass
    - You may know that every subclass of Shape has a draw method, but Java doesn't
- Solution 1: Put a draw method in the Shape class
    - This method will be inherited by all subclass, and will make Java happy
    - But what will it draw?
- Solution 2: Put an abstract draw method in the Shape class
    - This will also be inherited (and make Java happy), but you don't have to define it
    - You do, however, have to make the Shape class abstract
    - This way, Java knows that only "concrete" objects have a draw method

### Solving the problem using abstract method
```Java
abstract class Shape{
    abstract void draw();
}
class Star extends Shape{
    void draw(){...}
}
class Crescent extends Shape{
    void draw(){...}
}
```
- Shape someShape = new Star();
    - This is legal, because a Star is a Shape
    - However, Shape someShape = new Shape(); is no logner legal
- someShape.draw();
    - This is legal, because every actual instance must have a draw() method

# Class video 4.5 