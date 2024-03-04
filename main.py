import random
from grammar import Grammar
from finiteAutomata import Finite_Automata


class Main:
    def generate_valid(grammar, nstrings):
        valid = []

        def generate_string(remaining, transition):
            if not remaining:
                return '', transition
            for index, char in enumerate(remaining):
                if char.isupper():
                    current = char
                    break
            else:
                return remaining, transition

            if current in grammar.VT:
                current_str, transition = generate_string(remaining[index + 1:], transition)
                return current + current_str, transition
            else:
                product = random.choice(grammar.P[current])
                new_remaining = ''.join(reversed(product)) + remaining[index + 1:]
                transition.append((current, product))
                return generate_string(new_remaining, transition)

        for _ in range(nstrings):
            string, transitions = generate_string('S', [('S', 'S')])
            valid.append((string[::-1], transitions))

        return valid

    def run():
        grammar = Grammar()

        print("Strings generated:")
        valid = Main.generate_valid(grammar, 5)

        for result, transitions in valid:
            for transition in transitions:
                print(f"-> {transition[1]}", end=' ')
            print(f"-> {result} \n")

        input_strs = ["abac", "baba", "wwwa", "cca", "aaaaac"]
        finite_automata = Finite_Automata(grammar)
        print("\n Checking if the strings can be created")
        for input_str in input_strs:
            if finite_automata.check(input_str):
                print(f" '{input_str}' can be created")
            else:
                print(f" '{input_str}' cannot be created")


Main.run()