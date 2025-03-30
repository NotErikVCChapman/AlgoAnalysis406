import nfa


# a class for DFAs
# modify as needed
class DFA:

    # init the DFA
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q  # set of states
        self.Sigma = Sigma  # set of symbols
        self.delta = delta  # transition function
        self.q0 = q0  # initial state
        self.F = F  # final states

    # print the data of the DFA
    def __repr__(self):
        return f"DFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"

    # run the DFA on the word w
    # return if the word is accepted or not
    # modify as needed
    def run(self, w):
        # todo
        # 1. Bring DFA to the initial state
        # 2. While letter in word,
        #       pass symbol to transition function
        # 3. If in final state:
        #       return accepted
        # return failed
        state = self.q0
        for char in w:
            # some combo of delta and char and state
            # state = delta(char)
            state = self.delta[(state, char)]
        if state in self.F:
            return True
        return False

    def refuse(self):
        # Loop through states,
        #   if state is not in F, add to new list N
        #   final states are now the states of N
        N = set()
        for state in self.Q:
            if state not in self.F:
                N.add(state)

        # Create a new DFA that uses N
        newDFA = DFA(Q=self.Q, Sigma=self.Sigma, delta=self.delta, q0=self.q0, F=N)

        return newDFA

    def to_NFA(self):
        N1 = nfa.NFA(
            Q=self.Q,
            Sigma=self.Sigma,
            delta=self.delta,  # transition function wont be a list but shrug
            q0=self.q0,
            F=self.F,
        )

        return N1
