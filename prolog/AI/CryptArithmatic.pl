sum(N1, N2, N) :-
	sum1(N1, N2, N, 0, 0, [0,1,2,3,4,5,6,7,8,9], _).
% for the problem, carry from left and right are 0
% all digits are available for the problem

sum1([], [], [], C, C, D, D).
% recursive call will exit with empty lists

sum1([D1|N1], [D2|N2], [D|N], Cr, C, Digs1, Digs) :-
	sum1(N1, N2, N, Cr, Cl, Digs1, Digs2),
	digsum(D1, D2, Cl, D, C, Digs2, Digs).
% recursive calls for the remaining list
% digsum handles addition of 2 letters at a time

digsum(D1, D2, C1, D, C, Digs1, Digs) :-
	del_var(D1, Digs1, Digs2),
	del_var(D2, Digs2, Digs3),
	del_var(D, Digs3, Digs),
	S is D1 + D2 + C1,
	D is S mod 10,	% remainder of division
	C is S // 10.	% integer of division
% D1+D2+C1=D+C

del_var(A, L, L) :-
	nonvar(A), !.	% A already instantiated

del_var(A, [A|L], L).

def_var(A, [B|L], [B|L1]) :-
	del_var(A, L, L1).

puzzle1([0,S,E,N,D], [0,M,O,R,E], [M,O,N,E,Y]).
% Examples of problems
