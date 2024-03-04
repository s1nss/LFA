class Grammar:
    def __init__ (self):
        self.VN = {'S', 'A', 'C', 'D'}
        self.VT = {'a', 'b'}
        self.P = {
            'S': ['aA'],
            'A': ['bS', 'dD'],
            'C': ['a', 'bA'],
            'D': ['bC', 'aD'],
        }