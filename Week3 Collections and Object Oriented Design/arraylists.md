# Class video 3.1
- ArrayList
    - why use them?
- Example: Abstract representation of cards

### ArrayList
- used when the size of the data collection is unknown
- the indexing operations are still quick
- adding an element is quick on average.
    - ArrayList works by dynamically resizing an array behind the scenes.

### Syntax for ArrayList
- Remember to import java.util.*
- ArrayList< object datatype>;
- An arraylist can only be made of objects. Primitive datatypes are not allowed.

### ArrayList of Strings
- Declaration: name
- Initialize the list: []
- Declare and initialize: names = []

### ArrayList methods
names = list[]
- names.append("Ted") - add the element to the end of the list.
- names[i] - get the element at the ith index.
- "Ted" in names - returns a boolean saying whether the names arraylist contains Ted
- names.remove(i) - remove the element at th ith index.

Java wrapper classes for primitives
- Java has classes that "warp around" the primitive datatype.
- Instead of using the primitive datatype int you can replace it with java's Integer class.
- To make an arraylist containing integers(in the mathematical sense)
- ArrayList<Integer> attendance = new ArrayList<Integer>();

### Example - using ArrayList to simulate cards
```python
import random

class Card:
    suit = None
    rank = None

deck = []
suits = ['d', 's', 'c', 'h']
for i in range(13):
    for j in range(4):
        c = Card()
        c.suit = suits[j]
        c.rank = i
        deck.append(c)

random.shuffle(deck)

# pick the 10th card
tenth_card = deck[9]
print(str(tenth_card.rank) + " " + str(tenth_card.suit))
```

# Class video 3.2
- Looping through an ArrayList
    - Enhanced forloop
- Concurrent modification

### Enhanced for loop
- For any collection of data the following systax loops through every element
```python
for item in items:
    # variable name can be used in this loop
    # variable takes each value in the collection one by one
```

### Example: find longest name in a list
- Assume we have an arraylist of strings called names
```python
names = ["a", "aaa", "aa"]
max = 0
longest = ""
for name in names:
    if len(name) > max:
        max = len(name)
        longest = name
print(str(max), longest)
```

### Modifying an array in a loop
- The enhanced forloop is best used for reading elements
- Not suitable for initializing values or modifying existing values
```python
for item in items:
    item = 0
```
The above loop does not make all the values in the collections values to be 0

### Modifying an arraylist
```python
for i in range(len(values)):
    values[i] = 0
```

### ConcurrentModificationException
```python
# Python code
# you can do this in python but not in Java
for card in deck:
    if card.suit == 'c':
        deck.remove(card)
```
```Java
// Java code
// Removing elements while iterating through the list
// at the same time is not allowed in the enhanced forloop
for (Card ca: deck){
    if (ca.suit == 'c')
        deck.remove(ca);
}
```
### Solving the ConcurrentModificationException
```Java
// Java code
ArrayList<Card> clubs = new ArrayList<Card>();
for(int i=0; i<deck.size(); i++>){
    Card ca = deck.get(i);
    if(ca.suit == 'c'){
        clubs.add(ca);
    }
}
deck.removeAll(clubs);
```

# Quiz 3.1
- The goal of the quiz is to test your understanding of the content covered in the lectures. We expect you to be able to solve the quiz questions without having to type any of the code into Eclipse.
```Java
// Java code
ArrayList<String> hosts = new Array<>();
hosts.add("google.com");
hosts.add("mcmaster.ca");
hosts.add("bu.edu");
hosts.add("amazon.com");

for(String host: hosts){
    if(host.endWith("edu")){
        System.out.println(host);
    }else{
        if(host.equals("amazon.com")){
            host.remove(host)
            hosts.add("placeholder")
        }
    }
}
```