from finite_automata import *

nfa = FiniteAutomata(
    states=['0', '1', '2'],
    alphabet=['a', 'b'],
    transitions={ 
        ('0', 'a'): ['0'],
        ('1', 'a'): ['1'],
        ('2', 'a'): ['2'],
        ('0', 'b'): ['0', '1'],
        ('1', 'b'): ['2']
    },
    start_state='0',
    final_states=['2']
)

print("Is our NFA Deterministic:")
print(is_deterministic(nfa))


print("\nNFA to DFA:")
dfa = ndf_to_dfa(nfa)
print(dfa)

reg = to_regular_grammar(nfa)
print("\nNFA to Regular Grammar:")
for state, prods in reg.items():
    for prod in prods:
        print(f"{state} -> {prod}")