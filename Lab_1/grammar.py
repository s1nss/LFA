class Grammar:
    # Constructor method for initializing a grammar
    def __init__ (self):
        self.VN = {'S', 'A', 'C', 'D'}  # Set of non-terminal symbols
        self.VT = {'a', 'b'}  # Set of terminal symbols
        self.P = {  # Production rules
            'S': ['aA'],
            'A': ['bS', 'dD'],
            'C': ['a', 'bA'],
            'D': ['bC', 'aD'],
        }
