priority(high) :- severity > 80.
priority(medium) :- severity =< 80, severity > 50.
priority(low) :- severity =< 50.