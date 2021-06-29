# Challenge Summary
<!-- Description of the challenge -->
Create a function called quick_sort() that takes in a an unsorted list. This function takes in an element as a pivot and partitions the given array around this  pivot.

## Whiteboard Process
<!-- Embedded whiteboard image -->
[WhiteBoard Img](codechallenge28.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Time Complexity - O(n) because we split the list into two parts and perform the same actions on both parts

Space Complexity - O(LogN) because we're using recursive methods

## Solution
<!-- Show how to run your code, and examples of it in action -->
1. Create a function called quick_sort() that takes in an unsorted list, a left, and a right. The function will split the list in two and sort the values low to high.

2. Create a function called partition that is used by the quick_sort function that chooses a pivot, the last value in the list, and partitions the list around this pivot.

3. Create a function called swap that is used by partition to swap values if the left value is less than the right value.
