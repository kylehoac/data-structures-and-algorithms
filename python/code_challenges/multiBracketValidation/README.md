# Challenge Summary

Write a function called "multi_bracket_validation(input)" that takes in a string as its only argument, and returns a boolean representing whether or not the brackets in the string are balanced (meaning that if there are brackets in the string, then there must be both an opening and closing bracket present). The three types of brackets include:

1. Round Brackets: ()
2. Square Brackets: []
3. Curly Brackets: {}

## Whiteboard Process

[Whiteboard image](CodeChallenge13.jpg)

## Approach & Efficiency

Time = O(N) - Acceptance of any size string influences time
Space = O(1) - Space is allocated once, and never reassign

## Solution

We iterated through the string, and added all open brackets to a list. If there were no opening brackets, then the function returned false. Every closing bracket found would trigger another function that checked to see if it matched any opening bracket within the list. The function would then return true if every single opening, closing bracket had its other half within the string.

Ex:
> def multi_bracket_validation({([])}) - results in true
> def multi_bracket_validation({[)}) - results in false
