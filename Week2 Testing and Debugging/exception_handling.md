# Class video 2.6
- exception handling
- try. catch. finally

### Errors and exceptions
- an error is a bug in your program. For example, a divide by zero
- an exception is a problem whose cause is outside your program. For example, running out of memory, wrong file name.

### What to do with errors and exceptions
- an error is a bug and therefore should be fixed.
- an exception is a problem that your program may encounter
- the situation in which you encounter the problem might not be the norm but you want to ensure that your program does not completely crash.

### The try statement
- the try statement(also called the try-catch statement) separates normal code from the error handling
```python
try:
    do the "normal" code, ignoring exceptions
except some exception:
    handle the exception
except some other exception:
    handle the excpetion
```

### Exception handling is not optional in Java
- for certain situations, most commonly in file handling, Java insists that you do something about the exceptional situations
- if you do not catch an exception, the code does not even compile
- there are called checked exceptions.

### How Java handles errors behind the scenes
- in Java, an error doesn't necessearily cause your program to crash.
- when an error occurs, Java throws an Error object for you to use
    - you can catch this object to try to recover
    - you can ignore the error (the program will crash)
- When a checked exception occurs, Java throws an exception object for you to use
    - you **cannot ignore** an exception; you must catch it
    - you get a *syntax* error if you forget to take care of any possible exception.

### A few kinds of exceptions
- IOException: a problem doing input/output
    - FileNotFoundException: no such file
    - EOFException: tried to read past the End Of File
- NullPointerException: tried to convert a non-numeric String a number
- OutOfMemoryError: the program has used all available memory
- There are about 200 predefined Exception types

### What to do about Exceptions
- you have two choices:
    - you can "catch" the exception and deal with it
        - For Java's exception, this is usually the better choice
    - you can "pass the buck" and let some other part of the program deal with it
        - this is often better for exceptions that you create and thorw
- Exceptions should be handled by the part of the program that is best equipped to do the right thing about them.
- you can catch exceptions with a try statement
    - when you catch an exception, you can try to repair the problem, or you can just print out information about what happened
- you can "pass the buck" by stating that the method in which the exception occurs "throws" the exception
    - example:
    ```Java
    void openFile(String fileName) throws IOException{
        ... 
    }
    ```
- which of these you do depends on whose *responsibility it is* to do something about the exception
    - if the method "know" what to do, it should do it
    - if it should really be up to the user(the method caller) to decide what to do, then "pass the buck"

### Finally
- after all the catch phrases, you can have an optional finally phrase
```Java
try { ... }
catch (AnExceptionType e){ ... }
catch (AnotherExceptionType e){ ... }
finally { ... }
```
- whatever happens in try and catch, even if it does a return statement, the finally code will be executed
    - if no exception occurs, the finally will be executed after the try code
    - in an exception does occurm the finally will be executed after the appropriate catch code

### Using the exception
- when you say catch(IOException e), e is a *formal parameter* of type IOException
    - a catch phrase is almost like a miniature method
    - e is an instance(object) of class IOException
    - Exception objects have methods you can use
- here's an especially useful method that is defined for every exception type:
    ```Java
    e.printStackTrace();
    ```
    - this prints out what the exception was, and how you got to the statement that caused it

### printStackTrace
- PrintStackTrace() does not print on System.out, but on another stream, System.err
    - Eclipse writes this to the same Console window, but writes it in red
    - From the command line: both System.out and System.err are sent to the terminal window
- printStackTrace(*stream*) prints on the given stream
    - printStackTrace(System.out) prints on System.out, and this output is printed along with the "normal" output

# Class video 2.7
- File I/O
- Reading and writing text files

### Reading Files
- Reading a file is not too different from using the Scanner class.
- So far we have used the Scanner to read from standard input(input taken from the console)

### Reading the contents of a file line bu line
- Open the file
```Java
// Open the file
File textFile = new File("test.txt");
// Define a scanner on the file
Scanner scnr = new Scanner(textFile);
```
- Note that Java will insist that FileNotFoundException gets handled. Use a try catch block. Decide what you want to do in the catch block if the file is not found.

### Reading the contents of a file line by line
```Java
while(scnr.hasNextLine()){
    String line = scnr.nextLine();
    System.out.println(line);
}
```

### Writing to a text file
- FileWrite Write = new FileWriter(filename, append?);
    - if the append argument is set to true the text will be added to the end of the file
    - if the append argument is set to false the file will be overwritten.
- PrintWriter printer = new PrintWriter(writer);
- printer.println(whatever your wanted to write to the file)
- printer.flush() in order to ensure that text is written out to the file. Without the flush method being called, the printing out to the file could be buffered.
```Java
try{
    FileWriter fileWriter = new FileWriter("text.txt", true);
    PrintWriter printer = new PrintWriter(fileWriter);
    printer.printly("some words");
    printer.flush();
}
catch(IOException e){
    e.printStackTrace();
}
``` 