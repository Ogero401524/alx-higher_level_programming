def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    tupleone = tuple_a + (0, 0)
    tupletwo = tuple_b + (0, 0)
    new_tuple = tupleone[0] + tupletwo[0], tupleone[1] + tupletwo[1]
    return new_tuple
