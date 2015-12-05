% Sorting a given list
% Stop and return True if head of list matched the item
search([H|T], H) :- !.
% Recursive call to search for searching item in the list
search([H|T], I) :-
	search(T, I).


% Contatinating two given lists
% Append second list to resultant
append([], Y, Z).
% Append the first list turn by turn to the resultant
append([X|Xs], Y, [X|Z]) :-
	append(Xs, Y, Z).

% Add an item to the list
add(I, L, [I|L]).

% Delete and item from list
% Delete item if it is in the head
del(X, [X|Xs], Xs).
% Traverse till the desired item is in the head
del(X, [Y, Xs], [Y, Ys]) :-
	del(X, Xs, Ys).

% Search element at the nth position
% Terminate when item found and is doesnt have more to search
search([H|T], H, 1) :- !.
% Traverse the list till 1 element left to traverse
search([H|T], I, N) :-
	N > 1,
	N0 is N-1,
	search(T, I, N0).
