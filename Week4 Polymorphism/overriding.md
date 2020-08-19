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