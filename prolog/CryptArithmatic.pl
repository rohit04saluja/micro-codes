sum(N1, N2, N) :-
	sum1(N1, N2, N, 0, 0, [0,1,2,3,4,5,6,7,8,9], _).
% for the problem, carry from left and right are 0
% all digits are available for the problem

sum1([], [], [], C, C, D, D).
% recursive call will exit with empty lists

sum1([D1|N1], [D2|N2], [D|N], C_in, C_out, DigsA, DigsR):-
	sum1(N1, N2, N, C_in, C, DigsA, Digs),
	digsum(D1, D2, C, D, C_out, Digs, DigsR).
% recursive calls for the remaining list
% digsum handles addition of 2 letters at a time

digsum(D1, D2, C_in, D, C_out, DigsA, DigsR) :-
	del_var(D1, DigsA, Digs1),
	del_var(D2, Digs1, Digs2),
	del_var(D, Digs2, DigsR),
	S is D1 + D2 + C_in,
	D is S mod 10,		% remainder of division
	C_out is S // 10.	% integer of division
% D1+D2+C_in=D+C_out

del_var(A, L, L) :-
	nonvar(A), !.	% A already instantiated

del_var(A, [A|L], L).
% Assign head of the list to variable

del_var(A, [B|L], [B|L1]) :-
	del_var(A, L, L1).
% Strip the head of the list and re-assign
