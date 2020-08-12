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