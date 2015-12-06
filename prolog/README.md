# Author: rohit04saluja
#
#
#
######
### DataStructure.pl ###
- Prolog code snipets implementing a simple list data structure
#
- search predicate lets you check is an item is present in the give n list
# Usage
?- search([1, 2, 3, 4], 3).
#
- search predicate also lets you seach an item at nth position in the given list. 
- search predicate does not allow you to find out the position of an item in the given list. The code snipet is possible, I am just lazy to write it.
# Usage
?- search([1, 2, 3, 4], I, 4).
#
- append predicate lets you concatinate two lists and return an output list or lets you check if the given lists concatinate to form the 3rd.
# Usage
?- append([1, 2], [3, 5], X).
#
- add predicate inserts the given item at the top of the list
# Usage
?- add(1 , [2, 3, 4]).
#
- del predicate lets you delete the given item from the given list if it exists in the list.
# Usage
?- del(3, [1, 2, 3, 5]).
#
- len predicates lets you find the length of the the given list
#
?- len([1, 2, 3, 4], L).
#
#
#
######
### CryptArithmatic.pl ###
- Prolog program to solve a cryptarithimetic problem
- For better understanding the problem google "Cryptarithmetic problem"
- default available digits are 0 to 9
# Usage
?- sum([0,S,E,N,D], [0,M,O,R,E], [M,0,N,E,Y]).
