# Laboratory Work Report


## Legend

- [Objectives](#objectives)
- [Implementation](#implementation)
  - [Chomsky Normal Form](#lexical-analysis)
  - [Lexer/Scaner/Tokenizer](#lexerscannertokenizer)
  - [Results](#results)
- [Conclusion](#conclusion)

<br><br>
<br><br>
<br><br>

## Objectives

1. **Learn about Chomsky Normal Form (CNF)**

2. **Get familiar with the approaches of normalizing a grammar.**

3. **Implement a method for normalizing an input grammar by the rules of CNF.**
 

## Implementation

### Chomsky Normal Form:



### Chomsky Converter


#### Epsilon Elimination

```python
 for symbol in self.P:
            for production in list(self.P[symbol]):
                if production == '':
                    self.symbolReplacement(symbol)
                    self.P[symbol].remove('')
```

The epsilonElimination function removes epsilon (empty string) productions from a grammar. For each symbol with an epsilon production, it calls symbolReplacement to handle replacements, then removes the epsilon production from the grammar's production set.

#### Non-Productive Elimination

```python
 for production in list(self.P[symbol]):
                    terminals = False
                    nterminals = False
                    itself = False
                    for p in production:
                        if p == symbol:
                            itself = True
                        elif p in self.VN:
                            nterminals = True
                        elif p in self.VT:
                            terminals = True

                    if itself and not nterminals:
                        dzone = True
                    if (terminals or nterminals) and not itself:
                        dzone = False
                        break
```

The nonproductiveElimination function removes non-productive symbols from a grammar. It iteratively checks productions for non-productive symbols, updating the grammar by eliminating such symbols and their productions until no more non-productive symbols remain.

#### Inaccessible Symbol Elimination

```python
production_w_start = self.remove_key(self.P, 'S')
            for symbol in list(production_w_start):
                production_w_symbol = self.remove_key(self.P, symbol)
                accessible = False

                for symbols in list(production_w_symbol):
                    for production in symbols:
                        if symbol in production:
                            accessible = True
                            break

                    if accessible:
                        break

                if not accessible:
                    self.VN.remove(symbol)
                    del self.P[symbol]
                    counter += 1
```

The inaccessibleElimination function removes inaccessible symbols from a grammar. It iteratively checks for symbols that cannot be reached from the start symbol 'S' and eliminates these symbols and their productions until no inaccessible symbols remain.

#### Renaming Elimination
```python
            for symbol in self.P:
                for production in list(self.P[symbol]):
                    if production in self.VN:
                        self.P[symbol].remove(production)
                        for relation in self.P[production]:
                            self.P[symbol].add(relation)
                            counter += 1
```

The renamingElimination function removes single non-terminal renaming productions. It iteratively replaces productions that directly reference another non-terminal with the productions of the referenced non-terminal, until no more such renaming productions remain.

#### Chomsky Step

```python
        for i, symbol in enumerate(self.VT):
            self.VN.add(f'X{i}')
            self.P[f'X{i}'] = symbol

        for symbol in list(self.P):
            for production in list(self.P[symbol]):
                if len(production) == 2:
                    new_production = ''
                    for char in production:
                        if char in self.VT:
                            newX = f'X{list(self.VT).index(char)}'
                            new_production += newX
                        else:
                            new_production += char
                    self.P[symbol].remove(production)
                    self.P[symbol].add(new_production)
```


The chomskyStep function converts productions in a grammar to Chomsky Normal Form. It first replaces terminal symbols with new non-terminals (e.g., X0, X1, ...). Then, for productions of length 2, it substitutes terminals with their corresponding new non-terminals, ensuring all productions are either two non-terminals or a single terminal.

### Results 

```text

/usr/bin/python3 /Users/nmacrii/Desktop/lab5 Vlad/main.py 

Non-terminals (VN): {'C', 'A', 'B', 'S'}
Terminals (VT): {'d', 'a'}
Productions (P):
S -> dB, A
A -> aBdAB, dS, d
B -> , A, a, dA
C -> Aa

after eliminating epsilon

Non-terminals (VN): {'C', 'A', 'B', 'S'}
Terminals (VT): {'d', 'a'}
Productions (P):
S -> dB, A, d
A -> adAB, d, aBdA, aBdAB, dS, adA
B -> A, a, dA
C -> Aa

after eliminating nonproductive symbols

Non-terminals (VN): {'C', 'A', 'B', 'S'}
Terminals (VT): {'d', 'a'}
Productions (P):
S -> dB, A, d
A -> adAB, d, aBdA, aBdAB, dS, adA
B -> A, a, dA
C -> Aa

after eliminating inaccessible symbols

Non-terminals (VN): {'C', 'A', 'B', 'S'}
Terminals (VT): {'d', 'a'}
Productions (P):
S -> dB, A, d
A -> adAB, d, aBdA, aBdAB, dS, adA
B -> A, a, dA
C -> Aa

after eliminating any renaming

Non-terminals (VN): {'C', 'A', 'B', 'S'}
Terminals (VT): {'d', 'a'}
Productions (P):
S -> adAB, d, aBdA, aBdAB, dS, adA, dB
A -> adAB, d, aBdA, aBdAB, dS, adA
B -> aBdAB, dS, adA, adAB, d, dA, a, aBdA
C -> Aa

 after chomsky transformation

Non-terminals (VN): {'A', 'S', 'B', 'C', 'X0', 'X1'}
Terminals (VT): {'d', 'a'}
Productions (P):
S -> X2X3, d, X0B, aBdA, aBdX3, X2A, X0S
A -> X2X3, d, aBdA, aBdX3, X2A, X0S
B -> X2X3, a, X0S, d, aBdA, aBdX3, X2A, X0A
C -> AX1
X0 -> d
X1 -> a
X2 -> ad
X3 -> AB


Process finished with exit code 0


```


## Conclusion

## Conclusion

In this lab, we explored the Chomsky Normal Form (CNF) and its significance in simplifying context-free grammars. We learned various normalization techniques and applied these concepts to transform an input grammar into CNF. By implementing methods for epsilon elimination, nonproductive elimination, inaccessible elimination, renaming elimination, and final transformation into CNF, we gained practical experience in grammar normalization. This lab enhanced our understanding of formal grammar structures and prepared us for more advanced topics in compiler design and language processing.