import dfa
from collections import deque


# a class for NFAs
# modify as needed
class NFA:

    # init the NFA
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q  # set of states
        self.Sigma = Sigma  # set of symbols
        self.delta = delta  # non-deterministic transition function
        self.q0 = q0  # initial state
        self.F = F  # final states

    # print the data of the NFA
    def __repr__(self):
        return f"NFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"

    # run the NFA on the word w
    # return if the word is accepted or not
    # modify as needed

    def run(self, w):
        # list of states, start with initial state q0
        # update the list of states by checking transition function, for ex if q0 leads to both q0 and q1, state = {q0, q1}
        # if newState not in states, add to state
        # if finalState in states, return true
        states = []
        states.append(self.q0)
        for char in w:  # for all characters in the word
            reachedStates = []
            for state in states:  # for all states that we are currently in
                # a list of all states we are going to reach in this turn
                for newState in self.delta.get((state, char), []):
                    # loop through dict of returned states, e.g. [1,2]
                    if newState not in reachedStates:
                        # if we arent currently in that state
                        reachedStates.append(newState)
            states = reachedStates

        for state in states:
            # print("State Check:", state)
            if state in self.F:
                return True
        return False

    # def to_DFA(self):
    #     # the transition function changes from (key, index) to (key, list of indicies)
    #     # set of states needs to change to a set of lists of states
    #     # similar to the code for running a DFA right?

    #     # result of the transition function becomes the set of states.
    #     N1 = dfa.DFA(
    #         Q=self.Q,
    #         Sigma=self.Sigma,
    #         delta=self.delta,
    #         q0=self.q0,
    #         F=self.F,
    #     )

    #     #
    #     #

    #     return N1

    def to_DFA(self):
        # Step 1: Initialize DFA components
        q0_dfa = frozenset(
            {self.q0}
        )  # Start state as a set (frozenset for immutability)
        Q_dfa = set()  # DFA states
        delta_dfa = {}  # DFA transition function
        F_dfa = set()  # DFA final states
        queue = deque([q0_dfa])  # Processing queue

        # Step 2: Process states in a BFS manner
        while queue:
            current_dfa_state = queue.popleft()
            Q_dfa.add(current_dfa_state)

            # Check if it's a final state
            if any(state in self.F for state in current_dfa_state):
                F_dfa.add(current_dfa_state)

            # Step 3: Process transitions for this state
            for symbol in self.Sigma:
                next_states = set()
                for state in current_dfa_state:
                    if (state, symbol) in self.delta:
                        next_states.update(self.delta[(state, symbol)])

                next_dfa_state = frozenset(next_states)

                if next_dfa_state:  # Only add non-empty states
                    delta_dfa[(current_dfa_state, symbol)] = next_dfa_state

                    if next_dfa_state not in Q_dfa:
                        queue.append(next_dfa_state)

        # Step 4: Create and return the DFA object
        return dfa.DFA(
            Q=Q_dfa,
            Sigma=self.Sigma,
            delta=delta_dfa,
            q0=q0_dfa,
            F=F_dfa,
        )

    # copied from DFA, need to implement randomness into NFA state?
    # or return if one path has reached a final state.
    # def run(self, w):
    #     state = self.q0
    #     for char in w:
    #         # check all states and keep track in a list of states
    #         state = self.delta[(state, char)]
    #     if state in self.F:
    #         return True
    #     return False
