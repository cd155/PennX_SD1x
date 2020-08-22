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
- Interfaces

### What is an Interface?
- "An interface is a group of related methods with empty bodies" - from the offical Java documentation
- Most common way of specifying that a class follows a certain design

### The implements keyword
- Like signing a contract
- Agreeing to write certain methods

### Interfaces
- An interface declares(describes) methods but does not supply bodies from them
```Java
interface KeyListener{
    public void keyPressed(KeyEvent e);
    public void keyReleased(KeyEvent e);
    public void keyTyped(KeyEvent e);
}
```
- All the methods are implicitly public and abstract
    - You can add these qualifiers if you like, but why bother?
- You cannot instantiate an interface
    - An interface is like a very abstract class - none of its methods are defined
- An interface may also contain constants(final variables)

### When to write an interface
- You will frequently use the supplied Java interfaces
- Sometimes you will want to design your own
- You would write an interface if you want classes of various types to all have a certain set of capabilities
- For example, if you want to be able to create grocery items, you might define an interface as
```Java
public interface Item{
    salePrice();
}
```

### implements != extends
- You extend a class, but you implement an interface
- A class an only extend(subclass) one other class, but it can implement as many interfaces as you like
```Java
class MyListener implements Keylistener, ActionListener{...}
```
### implements == signing a binding contract
- When you say a class implements an interface, you are promising to define all the methods that were declared in the interface
### Example
```Java
class MyKeyListener implements KeyListener{
    public void keyPressed(KeyEvent e){...};
    public void keyReleased(KeyEvent e){...};
    public void keyTyped(KeyEvent e){...};
}
```
- The "..." indicates actual code that you must supply
- Now you can create a new MyKeyListener

### Do we have to write all the methods?
- It is possible for a class to define some but not all of the methods defined in an interface:
```Java
abstract  class MyKeyListener implements KeyListenner{
    public void keyTyped(KeyEvent e){...};
}
```
- Since this class does not supply all the methods it has promised, it must be an abstract class
- You must label it as such with keyword abstract
- You can even extend an interface(to add method):
```Java
interface FunkyKeyListener extends KeyListener{....}
```

### Why interfaces?
- Reason 1: A class can only extend one other class, but it cam implement multiple interfaces
    - This lets the class fill multiple "roles"
    - In writing user interfaces it is common to have a class be able to handle different user interactions.
    - Example:
    ```Java
    class MyApplet extends Applet
        implements ActionListener, KeyListener{...}
    ```
- Reason 2: You can write methods that work for more than one kind of class

### Methods for more than one class
- You can write methods work with more than one class
```Java
interface RuleSet{
    boolean isLegal(Move m, Board b);
    void makeMove(Move m);
}
```
```Java
class CheckersRules implements RuleSet{
    public boolean isLegal(Move m, Board b){...}
    public void makeMove(Move m){...}
}
class ChessRules implements RuleSet{...} // another implementation

RuleSet rulesOfThisGame = new Chessrules();
if(ruleOfThisGame.isLegal(m, b)){
    rulesOfThisGame.makeMove(m);
}
```
- This statement is legal becasue whatever kind of RuleSet object rulesOfThisGame is, it must have isLegal and makeMove methods

### instanceof
- instanceof is a keyword that tells you whether a variable "is a" member of class or interface
- For example, if
```Java
class Dog extends Animal implements Pet{...}
Animal fido = new Dog();
```
then the following are all true:
```Java
fido instanceof Dog
fido instanceof Animal
fido instanceof Pet
```
- instanceof is seldom used
    - When you find yourself wanting to use instanceof, think about whether the method you are writing should be moved to the individual subclasses

### In Summary
- Developers write interface more often than abstract class