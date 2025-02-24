import dfa


def __main__():

    # todo: instantiate accordingly
    A1 = dfa.DFA(
        Q={1, 2, 3, 4},
        Sigma={"a", "b"},
        delta={
            (1, "a"): 2,
            (1, "b"): 4,
            (2, "a"): 3,
            (2, "b"): 4,
            (3, "a"): 3,
            (3, "b"): 3,
            (4, "a"): 2,
            (4, "b"): 3,
        },
        q0=1,
        F={2, 4},
    )

    # todo: instantiate accordingly
    A0 = A1.refuse()

    # todo: add appropriate test cases for A and A0
    words = {"a", "ab", "aba", "bab", "bb", "aa", "babaaaba"}
    automata = [A0, A1]

    # test words on automata
    for X in automata:
        print(f"{X.__repr__()}")
        for w in words:
            print(f"{w}: {X.run(w)}")
        print("\n")


__main__()
