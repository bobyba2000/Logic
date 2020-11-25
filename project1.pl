parent(queenElizabethII, princeCharles).
parent(princePhillip, princeCharles).
parent(queenElizabethII, princessAnne).
parent(princePhillip, princessAnne).
parent(queenElizabethII, princeAndrew).
parent(princePhillip, princeAndrew).
parent(queenElizabethII, princeEdward).
parent(princePhillip, princeEdward).

parent(princeCharles, princeWilliam).
parent(princessDiana, princeWilliam).
parent(princeCharles, princeHarry).
parent(princessDiana, princeHarry).

parent(princessAnne, zaraPhillips).
parent(captainMarkPhillips, zaraPhillips).
parent(princessAnne, peterPhillips).
parent(captainMarkPhillips, peterPhillips).

parent(princeAndrew, princessBeatrice).
parent(sarahFerguson, princessBeatrice).
parent(princeAndrew, princessEugenie).
parent(sarahFerguson, princessEugenie).

parent(princeEdward, jamesViscountSevern).
parent(sophieRhys-jones, jamesViscountSevern).
parent(princeEdward, ladyLouiseMountbattenWindsor).
parent(sophieRhys-jones, ladyLouiseMountbattenWindsor).

parent(princeWilliam, princeGeorge).
parent(kateMiddleton, princeGeorge).
parent(princeWilliam, princessCharlotte).
parent(kateMiddleton, princessCharlotte).

parent(peterPhillips, savannahPhillips).
parent(autumnKelly, savannahPhillips).
parent(peterPhillips, islaPhillips).
parent(autumnKelly, islaPhillips).

parent(zaraPhillips, miaGraceTindall).
parent(mikeTindall, miaGraceTindall).

male(princePhillip).
male(princeCharles).
male(captainMarkPhillips).
male(timothyLaurence).
male(princeAndrew).
male(princeEdward).
male(princeWilliam).
male(princeHarry).
male(peterPhillips).
male(mikeTindall).
male(jamesViscountSevern).
male(princeGeorge).

female(queenElizabethII).
female(princessDiana).
female(camilaParkerBowles).
female(princessAnne).
female(sarahFerguson).
female(sophieRhys-jones).
female(kateMiddleton).
female(autumnKelly).
female(zaraPhillips).
female(princessBeatrice).
female(princessEugenie).
female(ladyLouiseMountbattenWindsor).
female(princessCharlotte).
female(savannahPhillips).
female(islaPhillips).
female(miaGraceTindall).

married(queenElizabethII, princePhillip).
married(princePhillip, queenElizabethII).
married(camilaParkerBowles, princeCharles).
married(princeCharles, camilaParkerBowles).
married(princessAnne, timothyLaurence).
married(timothyLaurence, princessAnne).
married(sophieRhys-jones, princeEdward).
married(princeEdward, sophieRhys-jones).
married(princeWilliam, kateMiddleton).
married(kateMiddleton, princeWilliam).
married(autumnKelly, peterPhillips).
married(peterPhillips, autumnKelly).
married(zaraPhillips, mikeTindall).
married(mikeTindall, zaraPhillips).

divorced(princessDiana, princeCharles).
divorced(princeCharles, princessDiana).
divorced(princessAnne, captainMarkPhillips).
divorced(captainMarkPhillips, princessAnne).
divorced(sarahFerguson, princeAndrew).
divorced(princeAndrew, sarahFerguson).

husband(Person, Wife) :- male(Person), female(Wife), married(Wife, Person).
wife(Person, Husband) :- husband(Husband, Person).
father(Parent, Child) :- male(Parent), parent(Parent, Child).
mother(Parent, Child) :- female(Parent), parent(Parent, Child).
child(Child, Parent) :-  parent(Parent, Child).
son(Child, Parent) :- male(Child), child(Child, Parent).
daughter(Child, Parent) :- female(Child), child(Child, Parent).

grandparent(GP, GC) :- parent(GP, X), parent(X, GC).
grandmother(GM, GC) :- grandparent(GM, GC), female(GM).
grandfather(GF, GC) :- grandparent(GF, GC), male(GF).
grandchild(GC, GP) :- grandparent(GP, GC).
grandson(GS, GP) :- grandchild(GS, GP), male(GS).
granddaughter(GD, GP) :- grandchild(GD, GP), female(GD).

sibling(Person1, Person2) :- mother(X, Person1), mother(X, Person2), father(Y, Person1), father(Y, Person2), Person1\==Person2.
brother(Person, Sibling) :- sibling(Person, Sibling), male(Person).
sister(Person, Sibling) :- sibling(Person, Sibling), female(Person).
aunt(Person, NieceNephew) :- parent(X, NieceNephew), (sister(Person, X); (wife(Person, Y), sibling(X, Y))).
uncle(Person, NieceNephew) :- parent(X, NieceNephew), (brother(Person, X); (husband(Person, Y), sibling(X, Y))).
niece(Person, AuntUncle) :- female(Person), (aunt(AuntUncle, Person); uncle(AuntUncle, Person)).
nephew(Person, AuntUncle) :- male(Person), (aunt(AuntUncle, Person); uncle(AuntUncle, Person)).
