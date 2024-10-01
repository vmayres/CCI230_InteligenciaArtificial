male(jose).
male(joao).
male(paulo).
male(carlos).

female(maria).
female(ana).
female(helena).
female(joana).

casal(jose, maria).
casal(paulo, helena).

progenitor(jose, joao).
progenitor(jose, ana).
progenitor(maria, joao).
progenitor(maria, ana).
progenitor(ana, helena).
progenitor(ana, joana).
progenitor(joao, paulo).
progenitor(helena, carlos).
progenitor(paulo, carlos).

% Sibilings
irma(X,Y):-female(X), progenitor(Z,X), progenitor(Z,Y), not(X=Y).
irmao(X,Y):-male(X), progenitor(Z,X), progenitor(Z,Y), not(X=Y).

% pais (mae e pai)
mae(X,Y):-female(X),progenitor(X,Y),not(X=Y).
pai(X,Y):-male(X),progenitor(X,Y),not(X=Y).
%% logica de filhos
filho(X, Y) :- male(X), progenitor(Y, X).
filha(X, Y) :- female(X), progenitor(Y, X).

%avô :- pai do projenitor
avo(X,Y):-pai(X,Z),progenitor(Y,Z),not(X=Y).
avoh(X,Y):-mae(X,Z),progenitor(Y,Z),not(X=Y).
%% logica para neto
neto(X,Y):-avoh(Y,X);avo(Y,X).

%tio :- irmao do seu pai
tio(X,Y):-progenitor(Z,Y),irmao(Z,X),not(X=Y).

%primo :- filho do tio
prime(X,Y):-tio(Z,X),progenitor(Z,Y),not(X=Y).
prima(X,Y):-female(X),prime(X,Y).
primo(X,Y):-male(X),prime(X,Y).

%recursao em prolog
descendente(X, Y) :- filho(X, Y).
descendente(X, Y) :- filha(X, Y).
descendente(X, Y) :- (filho(Z, Y) ; filha(Z, Y)), descendente(X, Z).



