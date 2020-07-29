# Classes video 1.9
1. representing data collections
2. lists

### Example:
How do you keep track of the rainfall during the year?
```pyhton
jan1 = ...
jan2 = ...
```
This is tendious, we can use array to solve this problem.

An array is an indexed sequence of values of the same data type

Note: in python, we use introduce list which have similar features with array. List have more functions than array, such as append(), extend(). Moreover, list can add different type of data in one list.
### Example 1: Generate an empty list
```pyhton
rainfall = []
```
### Example 2: Generate a list with 356 slots, each of value = None
```pyhton
rainfall = [None] * 365
```
365 consecutive locations in memory are allocated to this array.

It is easy to index into array location.
rainfall[0] is the very first entry in the array. 0 indexing.

### rainfall = |3|2|1|9|10|18|20|5|
rainfall[0] = 3;
rainfall[1] = 2 
### To get last element of list
rainfall[-1] = 5 or rainfall[len(rainfall) - 1] = 5

### Looping through an list
Assume the rainfall list is populated by the rainfall every day in inches.
```python
sum = 0
for inches in rainfall:
    sum += inches
average_rainfall = sum/len(rainfall)
```
### Adding a new element
```python
student_names = []
studnet_names.append["student1"]
studnet_names.append["student2"]
print("list size is " + len(student_names))
```