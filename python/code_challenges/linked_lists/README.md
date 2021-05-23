# Singly Linked List

Code Challenge 5 - Creating a singly linked list

## Challenge

Create, and test functions that allow for a link list to be instantiated, added to, searched through, and return a collection / string that represents all items in the list

## Approach & Efficiency

Used Test Driven Development to make sure that a linked list could be created, and properly point to the beginning/head of the list. I then added and tested each feature function to see if they worked properly.

Time - O(1)

Space - O(n)

## API

- Can create an empty linked list upon initiation
- Can create a new node in the linked list, and properly identify head as first node
- Can check to see if certain values are included in linked list
- Can get every value in a linked list, add it to a collection, and return that collection
- Can return all values in a linked list in a formatted string, and also return a string if the list is empty

### Checklist

#### Features

- [x] Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
- [x] Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.
- [x] Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
- [x] Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
- [x] Define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"

#### Tests

- [x] Can successfully instantiate an empty linked list
- [x] Can properly insert into the linked list
- [x] The head property will properly point to the first node in the linked list
- [x] Can properly insert multiple nodes into the linked list
- [x] Will return true when finding a value within the linked list that exists
- [x] Will return false when searching for a value in the linked list that does not exist
- [x] Can properly return a collection of all the values that exist in the linked list
