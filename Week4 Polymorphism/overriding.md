# Class video 4.2
- Method Overriding
 
 ### Extending a class(the "is a " relationship)
 - Use the actual word 'extends'
 - class Square extends Rectangle
 - class Goalkeeper extends Player
 - **You can only extend one class**

 ### Superclass Construction 1
 - The very first thing any constructor does, automatically, is call default constructor for its superclass
 ```Java
 class Foo extends Bar{
     Foo(){// constructor
        super(); // invisible call to superclass constructor
     }
 }
 ```
 - You call replace this with a call to a specific superclass constructor
 - Using the keyword super
 - This must be the very first thing the constructor does
 ```Java
 class Foo extends Bar{
     Foo(){// constructor
        super(name, 5); // explicit call to superclass constructor
     }
 }
 ```

 ### Superclass Construction 2
 - Unless you specify otherwise, every constructor calls the default constructor for its superclass
 ```Java
 class Foo extends Bar{
     Foo(){ // constructor
        super(); // invisible call to superclass constructor
     }
 }
 ```
 - You can use this (...) to call another constructor in the same class:
 ```Java
 class Foo extends Bar{
     Foo(String message){ // constructor
        this(message, 0, 0); // your explicit call to another constructor
     }
 }
 ```

 ### Superclass Construction3
 - You can use super(...) to call a specific superclass constructor
 ```Java
class Foo extends Bar{
    Foo(String message){ // constructor
        super(name, 5); // your explicit call to another constructor
    }
}
 ```
- Since the call to another constructor must be the very first thing you do in the constructor, you can only do one of the above.

### Overriding
```Java
class Animal{
    public static void main(String args[]){
        Animal animal = new Animal();
        Dog dog = new Dog();
        animal.print();
        dog.print();
    }
    void print(){
        System.out.println("Superclass Animal")
    }
}
public class Dog extends Animal{
    void print(){
        System.out.println("Subclass Dog")
    }
}
```
- This is called overriding a method
- Method print in Dog overrides method print in Animal

### How to override a method
- Create a method in a subclass having the same signature as a method in a superclass
- This is, create a method in a subclass having the same name and the same number and types of parameters
- Parameter *names* don't matter, just their types
- Restrictions:
    - The return type must be the same
    - The overriding method cannot be more private than the method it overrides(ignore this bullet point for now)

### Why override a method?
```Java
Dog dog = new dog();
System.out.println(dog);
```
- Prints something like Dog@feda4c00
- The println method calls the toString method, which is defined to Java's top-level Object class
- Hence, every object can be printed(though it might not look pretty)
- Java's method public String toString() can be overridden
If you add a class Dog the following:
```Java
public String toString(){
    return name;
}
```
Then System.out.println(dog); will print the dog's name, which may be something like: Fido

# Class video 4.3
- Common examples of overriding
    - toString method
    - equals method

### The Object class
- In Java, every class inherits from the Object class
- Think of the Object class as the most general class
- Every class that we define is lower in the hierarchy and becomes more and more specific

### toString()
- It is almost always a good idea to override public String toString() to return something "meaningful" about the object
- When debugging, it helps to be able to print objects
- System.out.println(car) is the same with car.toString()
- When you print objects with System.out.print or System.out.println, they automatically call the objects toString() method
- When you concatenate an object with a string, the object's toString() method is automatically called.

### Calling toString() explicitly
- You can call toString() explicitly just like you would do any other method
- Used in cases when you have to pass a string form of an object to another method.
- Can be used in unit testing to check if two objects are the same
- For example you have 2 Person objects. You could decide to use
```Java
assertEquals(person1.toString(), person2.toString())
```
- There are better ways to do this though.

### Equality
- Consider these two assignments:
    - Thing thing1 = new Thing();
    - Thing thing2 = new Thing();
    - Are these two "Things" equal? That's up to the progarmmer.
- But consider:
    - Thing thing3 = new Thing();
    - Thing thing4 = thing3;
    - Are thest two "Things" equal? Yes, because they are the *same* Thing.

### The equals method
- Primitives can always be tested for equality with ==
- For objects, == tests whether the two are the same object
- Two string "abc" and "abc" may or may not be ==!
- Objects can be tested with the method
    - public boolean equals(Object o), **check every components**
- Unless overridden, this method just uses ==
- It is overridden in the class String
- It is not overridden for arrays; == tests if its operands are the same array
#### Morals:
- Never use == to test equality of Strings or arrays or other objects
- Use equals for Strings, java.util.Arrays.equals(a1, a2) for arrays
- If you test your own objects for equality, override equals

### The equals method in unit testing
- assertEquals in a Junit test uses the overriden(hopefully) method of the objects being compared.
- assertArrayEquals - When used on a array of objects the equals method is used for every index
- Consider array1 and array2 as arrays of Object array1[i].equals(array2[i]) needs to be true for every index i