% Facts about the family
parent(john, alice).     % John is the parent of Alice
parent(john, bob).       % John is the parent of Bob
parent(alice, charlie).  % Alice is the parent of Charlie
parent(bob, david).      % Bob is the parent of David
parent(charlie, emma).   % Charlie is the parent of Emma
parent(david, grace).    % David is the parent of Grace
parent(emma, harry).     %emma is the parent of Harry
parent(grace, olivia).   %Grace is the parent of Olivia

% Rules for relationships
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).

siblings(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

aunt_or_uncle(X, Y) :- siblings(X, Z), parent(Z, Y).

cousin(X, Y) :- parent(Z, X), aunt_or_uncle(Z, Y).


% Define genders for people
male(john).
male(bob).
male(charlie).
male(david).
male(harry).


female(alice).
female(grace).  % Add Grace as a female
female(emma).   % Emma is a female
female(olivia).


 ?- mother(M, charlie).
M = alice.

24 ?- siblings(A, B).
A = alice,
B = bob .

25 ?- grandparent(G, harry).
G = charlie .

26 ?- cousin(C, harry).
false.

27 ?- father(F, charlie).
false.

28 ?- mother(M, emma).
false.

29 ?- siblings(S, olivia).
false.

30 ?- grandparent(GP, olivia).
GP = david .

31 ?- grandparent(GP, emma).

31 ?- grandparent(GP, emma).
GP = alice .

32 ?- father(F, grace).
F = david.

33 ?- mother(M, olivia).
M = grace.

34 ?- aunt_or_uncle(AU, harry).
false.

35 ?- aunt_or_uncle(AU, grace).
false.

36 ?- aunt_or_uncle(AU, emma).
false.

37 ?- cousin(C, grace).
false.

38 ?- cousin(C, david).
C = charlie .

39 ?- cousin(C, olivia).
false.

40 ?- parent(X, Y), parent(Y, Z).
X = john,
Y = alice,
Z = charlie .

41 ?- siblings(A, B), siblings(A, C), B \= C.
false.

42 ?- siblings(A,B), siblings(A,C), A \=B.
A = alice,
B = C, C = bob .

43 ?- cousin(X, Y), father(F, Y), mother(M, X), F \= M.
X = charlie,
Y = david,
F = bob,
M = alice .

44 ?- cousin(X, Z), father(F, Y), mother(M, X), F \= M.
X = charlie,
Z = david,
F = john,
Y = M, M = alice .

45 ?- parent(X, Y), parent(X, Z), Y \= Z.
X = john,
Y = alice,
Z = bob .

46 ?- grandparent(GP, GC), parent(P, GC), parent(GP, P).

GP = john,
GC = charlie,
P = alice .

47 ?- parent(X, Y), parent(Y, Z), siblings(Z, W).
false.

48 ?- parent(X, W), parent(Y,X), siblings(Z, W).
false.

49 ?- siblings(A, B), parent(B, C), parent(A, D), D \= B, C \= D.
A = alice,
B = bob,
C = david,
D = charlie .

50 ?- parent(X, Y), parent(Z, Y), Z \= X, \+siblings(X, Z).
false.

51 ?- parent(X, Y), parent(W, Y), X \=Z, \+siblings(X, Z).
false.

52 ?- cousin(X, Y), cousin(Y, Z), \+siblings(X, Z).

X = Z, Z = charlie,
Y = david .

53 ?- parent(X, Y), \+siblings(X, Y), \+cousin(X, Y).
X = john,
Y = alice .

