# Report for the First Laboritory Work

Course: Formal Languages & Finite Automata

Author: Pruteanu Vlad



## Objectives

1. **Understanding Formal Languages**:

   - Discover what a language is and what it needs to have in order to be considered a formal one.

2. **Project Setup**:

   - Provide the initial setup for the evolving project to be worked on during this semester.
   - Create a GitHub repository for storing and updating the project.
   - Choose a programming language, prioritizing simplicity in problem-solving.
   - Store reports separately to simplify verification of work.

3. **Grammar Implementation**:

   - Implement a type/class for the grammar.
   - Add a function to generate 5 valid strings from the language expressed by the grammar.

4. **Finite Automaton Conversion**:
   - Implement functionality to convert an object of type Grammar to one of type Finite Automaton.
   - Add a method to the Finite Automaton class to check if an input string can be obtained via state transition from it.

## Implementation Description

### Characteristics of Formal Languages

There is a lot we can speak about about the topic of Formal Lanugages. These are some of our symbolistics that we care a lot
while speaking about Formal Languages.

**Alphabet** - is a set of symbols on which this language is built.

**Strings** - is a set of strings of symbols drawn from a finite alphabet.

**Syntax** - are precise rules that tell you the symbols you are allowed to use and how to put them together into legal expressions.

**Semantics** - are precise rules that tell you the meanings of the symbols and legal expressions.

**Formal Grammar** - is defined as a set of production rules for such strings in a formal language.

**Automata Theory** - is a set of strings of symbols drawn from a finite alphabet.

### Project Setup

The initial setup of our project for the semester will be as follows:

#### GitHub Repository

- I created a GitHub repository that will be completed with lab information, this is the repository we will work on.
- Innitialized the repository with the README file that will have a small overview of the work done.

#### Programming Language Selection

- We will use Python because of a vast number of libraries that can be used with simplicity and efficiency to build easy to read code for our project.
- Python is also very easy to use and also is used a lot in the sphere of LFA.
- I'm currently learning python for web dev and using it for our project will evolve my python skills.

#### Report Making

- To make easy reports for every lab done we will have an .md file that will have the Report done in it instead of clustering it all in one file.
- For every laboratory we will use the same structure for our reports.

### Grammars

To implement our grammar I created a file with a class [Grammar](grammar.py).
To actually visualize some of the strings that can be created out of our grammar, I made a new Method in our main file to [Generate Strings](main.py). This method will create any number of strings that we give it out of our grammar.

#### Grammar Class Implementation:

```python
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
```

In this code we have a class named Grammar that has everything we need for our grammar implementation with the variant we have(_Variant 23_)

#### Generate String Method:

```python
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
```

In this code we have our function to take the grammar and a number of strings as input and generate the specified number of final strings that are valid for our grammar through random tries. Each string needs to transit through some transitions that are used to derive a valid string.

### Finite Automata

For our Finite Automata Implementation, we need a class that I named [Finite_Automata](finiteAutomata.py). In this class we created methods to convert grammar to a finite automata and it will check if the input string can be obtained via our transitions.

#### Grammar to Finite Automata

```python
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
```

This will take a grammar object and will convert it to its finite automata. It sets the basics to create finite automata with the grammar object we provided.

### Checking the input string

```python
    ef check(self, input_string):
        current_state = self.init_state
        for char in input_string:
            if not (current_state, char) in self.transition:
                return False
            current_state = self.transition[(current_state, char)]

        return True
```

This method will take some input string and it will check if it can be obtained with our transitions from the finite automata. It will iterate through every character then it will update the current state via the transitions defined. If it will reach the final state it will return True, if the current state was not in the transition it will return False.

### Results

```text
Strings generated:
-> S -> aA -> dD -> aD -> bC -> bA -> bS -> aA -> bS -> aA -> bS -> aA -> dD -> aD -> bC -> a -> adabbbababadaba 

-> S -> aA -> dD -> bC -> a -> adba 

-> S -> aA -> bS -> aA -> dD -> aD -> aD -> aD -> bC -> bA -> bS -> aA -> dD -> aD -> aD -> aD -> bC -> a -> abadaaabbbadaaaba 

-> S -> aA -> dD -> bC -> a -> adba 

-> S -> aA -> bS -> aA -> bS -> aA -> bS -> aA -> dD -> bC -> bA -> dD -> bC -> a -> abababadbbdba 


 Checking if the strings can be created
 'abac' cannot be created
 'baba' cannot be created
 'wwwa' cannot be created
 'cca' cannot be created
 'aaaaac' cannot be created

```

### Conclusion

In this lab we built the basics of Finite Automata.We made our own repository to setup our project for today and the future. We organised the work flow and reports building. We learned how to convert grammar to Finite Automata and how to generate strings. How to check if they can be created or not.