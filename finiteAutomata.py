class Finite_Automata:
    def __init__(self, grammar):
        self.alphabet = {}
        self.state = {}
        self.transition = {}
        self.init_state = None
        self.final_state = {}

        self.convert_grammar(grammar)

    def convert_grammar(self, grammar):
        self.alphabet = grammar.VT
        self.state = grammar.VN
        for symb in grammar.P:
            for product in grammar.P[symb]:
                if len(product) == 1:
                    self.transition[(symb, product)] = 'final'
                else:
                    self.transition[(symb, product[0])] = product[1]

        self.init_state = 'S'
        self.final_state = {symb for symb in grammar.P if symb.isupper()}

    def check(self, input_string):
        current_state = self.init_state
        for char in input_string:
            if not (current_state, char) in self.transition:
                return False
            current_state = self.transition[(current_state, char)]

        return True