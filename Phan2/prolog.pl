husband(Person, Wife) :- male(Person), female(Wife), married(Person, Wife).
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

sibling(Person1, Person2) :- mother(X, Person1), mother(X, Person2), father(Y, Person1), father(Y, Person2), not(Person1==Person2).
brother(Person, Sibling) :- sibling(Person, Sibling), male(Person).
sister(Person, Sibling) :- sibling(Person, Sibling), female(Person).

aunt(Person, NieceNephew) :- parent(X, NieceNephew), sister(Person, X).
aunt(Person, NieceNephew) :- parent(X, NieceNephew), wife(Person, Y), sibling(X, Y).
uncle(Person, NieceNephew) :- parent(X, NieceNephew), brother(Person, X).
uncle(Person, NieceNephew) :- parent(X, NieceNephew), husband(Person, Y), sibling(X, Y).
niece(Person, AuntUncle) :- female(Person), aunt(AuntUncle, Person).
niece(Person, AuntUncle) :- female(Person), uncle(AuntUncle, Person).
nephew(Person, AuntUncle) :- male(Person), aunt(AuntUncle, Person).
nephew(Person, AuntUncle) :- male(Person), uncle(AuntUncle, Person).

greatgrandparent(GGP, GGC) :- grandparent(GGP, X), parent(X, GGC).
greatgrandfather(GGF, GGC) :- greatgrandparent(GGF, GGC), male(GGF).
greatgrandmother(GGM, GGC) :- greatgrandparent(GGF, GGC), female(GGF).
greatgrandchild(GGC, GGP) :- greatgrandparent(GGP, GGC).
greatgrandson(GGS, GGP) :- greatgrandchild(GGS, GGP), male(GGS).
greatgranddaughter(GGD, GGP) :- greatgrandchild(GGD, GGP), female(GGD).
greataunt(GA, GreatNieceNephew) :- grandparent(X, GreatNieceNephew), sister(GA, X).
greataunt(GA, GreatNieceNephew) :- grandparent(X, GreatNieceNephew), wife(GA, Y), sibling(X, Y).
greatuncle(GU, GreatNieceNephew) :- grandparent(X, GreatNieceNephew), brother(GU, X).
greatuncle(GU, GreatNieceNephew) :- grandparent(X, GreatNieceNephew), husband(GU, Y), sibling(X, Y).
greatniece(GN, GAuntUncle) :- female(GN), greataunt(GAuntUncle, GN).
greatniece(GN, GAuntUncle) :- female(GN), greatuncle(GAuntUncle, GN).
greatnephew(GN, GAuntUncle) :- male(GN), greataunt(GAuntUncle, GN).
greatnephew(GN, GAuntUncle) :- male(GN), greatuncle(GAuntUncle, GN).

stepparent(StepParent, StepChild) :- married(StepParent, X), parent(X, StepChild).
stepmother(StepMother, StepChild) :- stepparent(StepMother, StepChild), female(StepMother).
stepfather(StepFather, StepChild) :- stepparent(StepFather, StepChild), male(StepFather).
stepchild(SC, SP) :- stepparent(SP, SC).
stepson(SS, SP) :- stepchild(SS, SP), male(SS).
stepdaughter(SD, SP) :- stepchild(SD, SP), female(SD).

halfsibling(Person1, Person2) :- child(Person1, X), stepparent(X, Person2).
halfbrother(Person, Sibling) :- halfsibling(Person, Sibling), male(Person).
halfsister(Person, Sibling) :- halfsibling(Person, Sibling), female(Person).

cousin(Person, NieceNephew) :- parent(X, Person), parent(Y, NieceNephew), sibling(X, Y).

siblinginlaw(Person, Sibling) :- sibling(X, Sibling), married(Person, X).
sisterinlaw(Person, Sibling) :- siblinginlaw(Person, Sibling), female(Person).
brotherinlaw(Person, Sibling) :- siblinginlaw(Person, Sibling), male(Person).
parentinlaw(Person, ChildInLaw) :- parent(Person, X), married(X, ChildInLaw).
motherinlaw(Person, ChildInLaw) :- parentinlaw(Person, ChildInLaw), female(Person).
fatherinlaw(Person, ChildInLaw) :- parentinlaw(Person, ChildInLaw), male(Person).
childinlaw(Person, ParentInLaw) :- parentinlaw(ParentInLaw, Person).
soninlaw(Person, ParentInLaw) :- childinlaw(Person, ParentInLaw), male(Person).
daughterinlaw(Person, ParentInLaw) :- childinlaw(Person, ParentInLaw), female(Person).

