import dfa


def generate_words():
    words = []
    alphabet = ["a", "b"]
    for first in alphabet:
        for second in alphabet:
            for third in alphabet:
                words.append(first + second + third)
    return words


def __main__():

    # all words that end with ab
    A1 = dfa.DFA(
        Q={1, 2, 3},
        Sigma={"a", "b"},
        delta={
            (1, "a"): 2,
            (1, "b"): 1,
            (2, "a"): 2,
            (2, "b"): 3,
            (3, "a"): 1,
            (3, "b"): 1,
        },
        q0=1,
        F={3},
    )

    # all words that contain aba
    A2 = dfa.DFA(
        Q={1, 2, 3, 4},
        Sigma={"a", "b"},
        delta={
            (1, "a"): 2,
            (1, "b"): 1,
            (2, "a"): 1,
            (2, "b"): 3,
            (3, "a"): 4,
            (3, "b"): 1,
            (4, "a"): 4,
            (4, "b"): 4,
        },
        q0=1,
        F={4},
    )

    # odd number of a's and odd number of b's
    A3 = dfa.DFA(
        Q={1, 2, 3, 4},
        Sigma={"a", "b"},
        delta={
            (1, "a"): 2,
            (1, "b"): 3,
            (2, "a"): 1,
            (2, "b"): 4,
            (3, "a"): 4,
            (3, "b"): 1,
            (4, "a"): 3,
            (4, "b"): 2,
        },
        q0=1,
        F={4},
    )

    # even number of a's and odd number of b's
    A4 = dfa.DFA(
        Q={1, 2, 3, 4},
        Sigma={"a", "b"},
        delta={
            (1, "a"): 2,
            (1, "b"): 3,
            (2, "a"): 1,
            (2, "b"): 4,
            (3, "a"): 4,
            (3, "b"): 1,
            (4, "a"): 3,
            (4, "b"): 2,
        },
        q0=1,
        F={3},
    )

    # any three consecutive characters contain at least one a
    A5 = dfa.DFA(
        Q={1, 2, 3, 4, 5, 6, 7},
        Sigma={"a", "b"},
        delta={
            (1, "a"): 2,
            (1, "b"): 5,
            (2, "a"): 3,
            (2, "b"): 3,
            (3, "a"): 4,
            (3, "b"): 4,
            (4, "a"): 2,
            (4, "b"): 5,
            (5, "a"): 3,
            (5, "b"): 6,
            (6, "a"): 4,
            (6, "b"): 7,
            (7, "a"): 7,
            (7, "b"): 7,
        },
        q0=1,
        F={2, 3, 4},
    )

    # all words that contain bbb
    A6 = dfa.DFA(
        Q={1, 2, 3, 4},
        Sigma={"a", "b"},
        delta={
            (1, "a"): 1,
            (1, "b"): 2,
            (2, "a"): 1,
            (2, "b"): 3,
            (3, "a"): 1,
            (3, "b"): 4,
            (4, "a"): 4,
            (4, "b"): 4,
        },
        q0=1,
        F={4},
    )

    # todo: add appropriate test cases for each of A1 to A7
    words = generate_words()
    automata = [A1, A2, A3, A4, A5, A6]

    # test words on automata
    for X in automata:
        print(f"{X.__repr__()}")
        for w in words:
            print(f"{w}: {X.run(w)}")
        print("\n")


__main__()
