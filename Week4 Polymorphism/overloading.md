# Class video 4.1
- Overloading
- How to have multiple methods with the same name

### Overloading
- One component of polymorphism
- Polymorphism - "the condition of existing in several forms"
- In this case it is a method existing in several forms in the same class.

### Why is overloading needed?
Assume you are printing to the console. There are two ways of designing the print method
- Method 1 - printInt, printDouble, printString, ....
- Method 2 - just create one method called print. But Java insists that you specify the datatype. So that will not work :(
- Method 3 - create a bunch of methods all of which are called print. Use the argument datatype to distinguish between them.
#### Method 3 wins! **Overloading**

### Rules for overloading
- Signature of method - the name of the method, the datatypes of arguments.
    - includes the number of arguments
    - includes the order in which they occur
```Java
public String subString(String s1, int a, int b){
}

// This is not work
public int subString(String s1, int a, int b){
}
```
- The signature is subString(String, int, int)
- In Java a method signature does not include the return datatype

### Overloading
```Java
class Test{
    public static void main(String args[]){
        myPrint(5);
        myPrint(5.0);
    }
    static void myPrint(int i){
        System.out.println("int i = " + i);
    }
    static void myPrint(double d){
        // same name, different parameters
        System.out.println("double d = " + d);
    }
}
```
- int i = 5; myPrint(i);
- double d = 5.0; myPrint(d);

### Why overload a method?
- So you can use the same names for methods that do essentially the same thing
- Example: println(int), println(double), println(boolean), println(String), etc.
- So you can supply defaults for the parameters:
```Java
int increment(int amount){
    count = count + amount;
    return count;
}
// do not repeat yourself
int increment(){
    return increment(1);
}
```
- Notice that one method can call another of the same name
So you can supply additional information:
```Java
void printResults(){
    System.out.println("total = " + total + ", average = " + average);
}
void printResults(String message){
    System.out.println(message + ": ");
    printResults();
}
```

### DRY (Don't Repeat Yourself)
When you overload a method with another, very similar method, only one of them should do most of the work:
```Java
void debug(){
    System.out.println("first = " + first);
    for(int i=first; i<=last; i++){
        System.out.print(dictionary[i] + " ");
    }
    System.out.println();
}
void debug(String s){
    System.out.println("At checkpoint " + s + ":");
    // call a method, avoid redundance
    debug();
}
```

### Legal assignments
- Widening is legal(going to more general datatype)
- Narrowing is illegal(unless you cast)
- All ints are doubles but all doubles are not ints, so Java gives you an error unless.
```Java
class Test{
    public static void main(String args[]){
        double d;
        int i;
        d = 5;  //legal
        i = 3.5;    //illegal
        i = (int)3.5;   //legal
    }
}
```

### Legal method calls
- Legal because parameter transmission is equivalent to assignment
- myPrint(5) is like saying
    - double d = 5;
    - System.out.println(d);
```Java
class Test{
    public static void main(String args[]){
        myPrint(5);
    }
    static void myPrint(double d){
        System.out.println(d);
    }
}
```

# Illegal method calls
- Illegal because parameter transmission is equivalent to assignment
- myPrint(5.0) is like
    - int i = 5.0;
    - System.out.println(i);
```Java
class Test{
    public static void main(String args[]){
        myPrint(5.0);
    }
    static void myPrint(int i){
        System.out.println(i);
    }
}
```
myPrint(int) in Test cannot be applied to (double)

### Java uses the most specific method
```Java
class Test{
    public static void main(String args[]){
        myPrint(5);
        myPrint(5.0);
    }
    static void myPrint(double d){
        System.out.println("double: " + d);
    }
    static void myPrint(int i){
        System.out.println("int: " + i);
    }
}
```
- int: 5
- double: 5.0

### Multiple constructors 1
You can "overload" constructors as well as methods:
```Java
Counter(){
    count = 0;
}
Counter(int start){
    count = start
}
```

### Multiple constructors 2
- One constructor can "call" another constructor in the same class, but there are special rules.
- You call the other constructor with the keyword this
- The call must be the very first thing the constructor does
```Java
// constructor 1
Point(int x, int y){
    this.x = x;
    this.y = y;
    sum = x + y;
}

// constructor 2
Print(){
    // call constructor 1
    this(0, 0)
}
```