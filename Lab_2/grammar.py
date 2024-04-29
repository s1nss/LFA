class Grammar:

    def __init__(self, VN=None, VT=None, productions=None, start_symbole=None):
        self.VN = VN if VN is not None else {'S', 'B', 'C'}
        self.VT = VT if VT is not None else {'a', 'b', 'c'}
        self.productions = productions if productions is not None else {
            'S': ['aB'],
            'B': ['aC', 'bB'],
            'C': ['bB', 'c', 'aS']
        }
        self.start_symbole = start_symbole if start_symbole is not None else 'S'

    def classify_grammar(self):
        for lhs, rhs_list in self.productions.items():
            for rhs in rhs_list:
                if len(lhs) > len(rhs) or (len(lhs) > 1 and any(char in self.VN for char in lhs)):
                    return "Unrestricted"

                if len(lhs) != 1 or lhs not in self.VN:
                    return "Context Sensitive"

        is_right_linear = any(all(symbole in self.VT for symbole in rhs[:-1]) and rhs[-1] in self.VN for rhs_list in
                              self.productions.values() for rhs in rhs_list)
        is_left_linear = any(rhs[0] in self.VN and all(symbole in self.VT for symbole in rhs[1:]) for rhs_list in
                             self.productions.values() for rhs in rhs_list)

        if is_right_linear and not is_left_linear:
            return "Regular Right Linear"
        elif is_left_linear and not is_right_linear:
            return "Regular Left Linear"

        return "Context Free"
