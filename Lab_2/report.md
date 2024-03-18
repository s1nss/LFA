# Determinism in Finite Automata. Conversion from NDFA 2 DFA. Chomsky Hierarchy.

---

## Theory:

## Overview
A finite automaton is a model used to depict various processes, functioning similarly to a state machine due to their comparable structures and objectives. The term "finite" underscores that an automaton begins with an initial state and progresses towards one or more designated final states, marking the start and completion of the modeled process.

Within an automaton's framework, it's possible for a single transition to lead to multiple states, introducing a level of non-determinism. In the context of systems theory, determinism refers to the predictability of a system. The presence of unpredictable elements renders a system stochastic or non-deterministic.

Hence, automata are categorized based on their determinism or lack thereof. It's noteworthy that determinism can be achieved through specific algorithms that adjust the automaton's structure, thereby navigating from non-determinism to determinism.

## Objectives:

1. Understand what an automaton is and what it can be used for.
2. Continuing the work in the same repository and the same project, the following need to be added: a. Provide a function in your grammar type/class that could classify the grammar based on Chomsky hierarchy.
   b. For this you can use the variant from the previous lab.
3. According to your variant number (by universal convention it is register ID), get the finite automaton definition and do the following tasks:

   a. Implement conversion of a finite automaton to a regular grammar.
   b. Determine whether your FA is deterministic or non-deterministic.
   c. Implement some functionality that would convert an NDFA to a DFA.
   d. Represent the finite automaton graphically (Optional, and can be considered as a **_bonus point_**):

   - You can use external libraries, tools or APIs to generate the figures/diagrams.
   - Your program needs to gather and send the data about the automaton and the lib/tool/API return the visual representation.

Please consider that all elements of the task 3 can be done manually, writing a detailed report about how you've done the conversion and what changes have you introduced. In case if you'll be able to write a complete program that will take some finite automata and then convert it to the regular grammar - this will be **a good bonus point**.

## Implementation

## Part 1: Grammar Classification

In the code, the `Grammar` class plays the role of a grammar detective, trying to figure out the "personality" of different grammars. Let's break down how it does that:

### 1.1 Chomsky Hierarchy:

1. **Type 0 - Unrestricted Grammars:**

   - These grammars operate without strict limitations, challenging traditional grammar conventions. 
   - They're characterized by production rules that defy standard expectations, such as having longer sequences on the left-hand side or featuring multiple nonterminals in that position.

2. **Type 1 - Context-Sensitive Grammars:**

   - These grammars take into account the surrounding context of a string; a sequence on the left side can be transformed depending on its adjacent elements. The defining trait of these grammars is that the length of the left-hand side is never greater than that of the right-hand side, ensuring every production aligns with the context-sensitive principle.
3. **Type 2 - Context-Free Grammars:**

   - Regarded as the standout group, these grammars apply production rules independently of surrounding context. The hallmark of context-free grammars is that each production rule must have exactly one nonterminal on the left side, allowing for straightforward generation and analysis of structures.
4. **Type 3 - Regular Grammars:**

   - These grammars exhibit a straightforward approach, focusing on linear patterns that can be right-leaning or left-leaning. They are scrutinized for their adherence to either right or left linearity within their production rules, simplifying the parsing and recognition processes.
In the following code I check every use case for each grammar and classify them:

```python
def classify_grammar(self):
        for lhs, rhs_list in self.productions.items():
            for rhs in rhs_list:
                if len(lhs) > len(rhs) or (len(lhs) > 1 and any(char in self.VN for char in lhs)):
                    return "Unrestricted"

                if len(lhs) != 1 or lhs not in self.VN:
                    return "Context Sensitive"

        is_right_linear = any(all(symbole in self.VT for symbole in rhs[:-1]) and rhs[-1] in self.VN for rhs_list in self.productions.values() for rhs in rhs_list)
        is_left_linear = any(rhs[0] in self.VN and all(symbole in self.VT for symbole in rhs[1:]) for rhs_list in self.productions.values() for rhs in rhs_list)

        if is_right_linear and not is_left_linear:
            return "Regular Right Linear"
        elif is_left_linear and not is_right_linear:
            return "Regular Left Linear"

        return "Context Free"
```

## Part 2: Finite Automaton Operations

### 2.1 Conversion to Regular Grammar

#### 2.1.1 The Scoop:

- The `to_regular_grammar` function takes an NFA and transforms its transitions into a more grammatical style.
- Epsilon ('ε') is like the wildcard, representing those moments when there's no specific symbol.

```python
def to_regular_grammar(fa):
    grammar = {}
    for (state, symbole), next_states in fa.transitions.items():
        if state not in grammar:
            grammar[state] = []
        for next_state in next_states:
            grammar[state].append(f"{symbole}{next_state}")
    for final_state in grammar:
        if final_state in grammar:
            grammar[final_state].append("\u03B5")
        else:
            grammar[final_state] = ["\u03B5"]
    return grammar
```

### 2.2 Deterministic Finite Automaton (DFA) Check

#### 2.2.1 In Simple Terms:

- The `is_deterministic` function is like a DFA detective, checking if it's straightforward or a bit of a wildcard.
- If any state has more than one transition for the same symbol, it's a sign that things might get a bit wild.

```python
def is_deterministic(fa):
    for next_states in fa.transitions.values():
        if len(next_states) > 1:
            return False
    return True
```

### 2.3 Conversion of NDFA to DFA

#### 2.3.1 The Unveiling:

- The `ndf_to_dfa` function uses some power (set construction) to turn a less decisive NDFA into a more decisive DFA.
- Each DFA state represents a set of states from the NDFA, making decisions as a team.

```python
def ndf_to_dfa(ndfa):
    dfa_states = {frozenset([ndfa.start_state]): '0'}
    dfa_transitions = {}
    dfa_final_states = []
    unmarked_states = [frozenset([ndfa.start_state])]

    while unmarked_states:
        current_dfa_state = unmarked_states.pop()
        for symbole in ndfa.alphabet:
            next_states = set()
            for ndfa_state in current_dfa_state:
                if (ndfa_state, symbole) in ndfa.transitions:
                    next_states.update(ndfa.transitions[(ndfa_state, symbole)])
            if not next_states:
                continue
            next_states_frozenset = frozenset(next_states)
            if next_states_frozenset not in dfa_states:
                new_state_name = str(len(dfa_states))
                dfa_states[next_states_frozenset] = new_state_name
                unmarked_states.append(next_states_frozenset)
            dfa_transitions[(dfa_states[current_dfa_state], symbole)] = dfa_states[next_states_frozenset]

    for dfa_state, label in dfa_states.items():
        if any(state in ndfa.final_states for state in dfa_state):
            dfa_final_states.append(label)

    return FiniteAutomata(list(dfa_states.values()), ndfa.alphabet, dfa_transitions, '0', dfa_final_states)
```

But mainly the algorithm works in three main steps:

1. **Initialization:** Start with a single state representing the NDFA's starting point and mark it for exploration.

   ```python
   dfa_states = {frozenset([ndfa.start_state]): '0'}
   dfa_transitions = {}
   dfa_final_states = []
   unmarked_states = [frozenset([ndfa.start_state])]
   ```

2. **Explore Transitions:**
   - For each unprocessed state and symbol:
     - Find all possible next states in the NDFA based on transitions.
     - If no transitions exist, move on to the next symbol.
   - If new states are found:
     - Create a new state in the DFA with a unique name.
     - Mark the new state for exploration.
     - Record the transition from the current state and symbol to the new state.

```python
while unmarked_states:
        current_dfa_state = unmarked_states.pop()
        for symbole in ndfa.alphabet:
            next_states = set()
            for ndfa_state in current_dfa_state:
                if (ndfa_state, symbole) in ndfa.transitions:
                    next_states.update(ndfa.transitions[(ndfa_state, symbole)])
            if not next_states:
                continue
            next_states_frozenset = frozenset(next_states)
            if next_states_frozenset not in dfa_states:
                new_state_name = str(len(dfa_states))
                dfa_states[next_states_frozenset] = new_state_name
                unmarked_states.append(next_states_frozenset)
            dfa_transitions[(dfa_states[current_dfa_state], symbole)] = dfa_states[next_states_frozenset]
```

3. **Identify Final States:**
   - Check each DFA state:
     - If it contains any of the NDFA's final states, mark the DFA state as final.

```python
for dfa_state, label in dfa_states.items():
        if any(state in ndfa.final_states for state in dfa_state):
            dfa_final_states.append(label)

    return FiniteAutomaton(list(dfa_states.values()), ndfa.alphabet, dfa_transitions, '0', dfa_final_states)
```

This process ensures a complete exploration of all possible paths in the NDFA and creates an equivalent DFA with deterministic transitions.

## Part 3: Console results



```
Is our NFA Deterministic:
False

NFA to DFA:

States: ['0', '1', '2']
Alphabet: ['a', 'b']

Transitions:
     δ(0, 'a') = ['0']
     δ(0, 'b') = ['1']
     δ(1, 'a') = ['1']
     δ(1, 'b') = ['2']
     δ(2, 'a') = ['2']
     δ(2, 'b') = ['2']
Start State: 0
Final States: ['2']


NFA to Regular Grammar:
0 -> a0
0 -> b0
0 -> b1
0 -> ε
1 -> a1
1 -> b2
1 -> ε
2 -> a2
2 -> ε
```

## 

## Conclusion

During this coding journey, we delved into the classification of grammars and the transformation processes of finite automata. The code offers a tangible glimpse into the syntax and mechanics of grammars and automata, establishing a foundation for grasping more intricate linguistic frameworks and pattern recognition algorithms. This exploration is akin to decoding the secret narratives entwined within symbols and transitions.