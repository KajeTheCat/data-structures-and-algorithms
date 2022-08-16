# problem domain

Given a linked-list, find the largest value.
Given a BST, find the largest value
All values 0 or larger, all whole numbers. (No -negatives).

## LL Largest value

define function --> largest value
largest value will take in --> head

set variable --> max to 0
while head is not none
check if max is less than the head
if max is less than the head set max to head
set head to next
after return max

LL max value steps:

1. looks at first item in list checks if value is less than or greater, if less than, sets max to value; if not, ignores current
2. steps to next node and repeats step one.
3. when head becomes none, loop ends and we return the max value.

## efficiency LL

+ space O(1): because the max is a single integer
+ time O(n): due to being on a loop

## BST Largest value

define function find largest
function will take in root node
decalre current starting at root_node
if current is True
check if current is not none
set current to the value to the right
return the current value

BST steps:

1. looks at current node and checks the right
2. if there is a value to right, step to right
3. repeat steps 1 and 2 until there are no more values to the right
4. return final current node.

## efficiency BST

+ space O(1): because the max is a single integer
+ time O(n): due to being on a loop
