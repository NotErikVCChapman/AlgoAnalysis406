import nfa


# generate words for testing
def generate_words():
    words = []
    alphabet = ["0", "1"]
    for first in alphabet:
        for second in alphabet:
            for third in alphabet:
                words.append(first + second + third)
    return words


def __main__():

    # todo: instantiate accordingly
    A1 = nfa.NFA(
        Q={1, 2},
        Sigma={"0", "1"},
        delta={
            (1, "0"): [1, 2],  # Store values as a list
            (2, "1"): [1],
        },
        q0=1,
        F={2},
    )  # Accepted language should be: 0, 010, 01010, etc

    A2 = nfa.NFA(
        Q={0, 1, 2},
        Sigma={"0", "1"},
        delta={
            (0, "0"): [0, 1],  # Store values as a list
            (0, "1"): [0],
            (1, "1"): [2],
            (2, "0"): [2],
            (2, "1"): [2],
        },
        q0=0,
        F={2},
    )  # accepted language should be (0+1)*01(0+1)*

    A3 = nfa.NFA(
        Q={0, 1, 2},
        Sigma={"0", "1"},
        delta={
            (0, "0"): [0],  # Store values as a list
            (0, "1"): [0, 1],
            (1, "0"): [2],
            (1, "1"): [2],
            (2, "0"): [3],
            (2, "1"): [3],
            (3, "0"): [4],
            (3, "1"): [4],
            (4, "0"): [4],
            (4, "1"): [4],
        },
        q0=0,
        F={0},
    )  # accepted language should be everything

    A4 = nfa.NFA(
        Q={0, 1, 2, 3, 4},
        Sigma={"0", "1"},
        delta={
            (0, "0"): [0, 1],  # Store values as a list
            (0, "1"): [1],
            (1, "1"): [2],
            (2, "0"): [2],
            (2, "1"): [2],
        },
        q0=0,
        F={4},
    )  # accepted language should be (0+1)*01(0+1)*

    # transition function as a dict with a set of states?

    words = generate_words()
    automata = [A1]

    # test words on automata
    # for X in automata:
    #     print(f"{X.__repr__()}")
    #     for w in words:
    #         print(f"{w}: {X.run(w)}")
    #     print("\n")
    print(A3.run("01010"))
    print(A3.run("00000"))
    print(A3.run("00001"))


__main__()
