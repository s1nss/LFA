import random
from grammar import Grammar
from finiteAutomata import Finite_Automata


class Main:
    # Static method to generate valid strings from the grammar
    def generate_valid(grammar, nstrings):
        valid = []  # List to store valid strings and their transitions

        # Helper function to recursively generate strings
        def generate_string(remaining, transition):
            if not remaining:  # If there are no more symbols to expand
                return '', transition  # Return empty string and current transitions
            for index, char in enumerate(remaining):  # Find the first non-terminal symbol
                if char.isupper():  # Non-terminal symbols are uppercase
                    current = char
                    break
            else:  # If no non-terminal symbol is found
                return remaining, transition  # Return the remaining string and transitions

            if current in grammar.VT:  # If the current symbol is terminal (should not happen in this context)
                current_str, transition = generate_string(remaining[index + 1:], transition)  # Recurse without the terminal
                return current + current_str, transition  # Append terminal to result
            else:  # If the current symbol is non-terminal
                product = random.choice(grammar.P[current])  # Randomly choose a production
                new_remaining = ''.join(reversed(product)) + remaining[index + 1:]  # Prepare new string to expand
                transition.append((current, product))  # Record the transition
                return generate_string(new_remaining, transition)  # Recurse with new string

        for _ in range(nstrings):  # Generate specified number of strings
            string, transitions = generate_string('S', [('S', 'S')])  # Start with initial state 'S'
            valid.append((string[::-1], transitions))  # Add generated string and transitions to list

        return valid  # Return list of valid strings and their transitions

    # Main method to run the example
    def run():
        grammar = Grammar()  # Create a Grammar instance

        print("Strings generated:")
        valid = Main.generate_valid(grammar, 5)  # Generate 5 valid strings

        for result, transitions in valid:  # Print the generated strings and transitions
            for transition in transitions:
                print(f"-> {transition[1]}", end=' ')
            print(f"-> {result} \n")

        input_strs = ["abac", "baba", "wwwa", "cca", "aaaaac"]  # List of input strings to check
        finite_automata = Finite_Automata(grammar)  # Create Finite_Automata instance with the grammar
        print("\n Checking if the strings can be created")
        for input_str in input_strs:  # Check each input string
            if finite_automata.check(input_str):  # If the string can be created
                print(f" '{input_str}' can be created")
            else:  # If the string cannot be created
                print(f" '{input_str}' cannot be created")


Main.run()  # Execute the main method
