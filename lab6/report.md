# Laboratory Work Report


## Legend

- [Objectives](#objectives)
- [Implementation](#implementation)
  - [Parsing Basisc](#parsing-basics)
  - [Concept of AST](#concept-of-ast)
  - [Token Type Enumeration](#token-type-enumeration)
- [Lexer Implementation](#lexer-implementation)
  - [Main Function](#main-funnction)
  - [Main Function](#tokens)
  - [Lexer](#lexer)
- [Results](#results)
- [Conclusion](#conclusion)

# Laboratory Work Report

<br><br>
<br><br>
<br><br>

## Objectives:
1. Get familiar with parsing, what it is and how it can be programmed [1].
2. Get familiar with the concept of AST [2].
3. In addition to what has been done in the 3rd lab work do the following:
   1. In case you didn't have a type that denotes the possible types of tokens you need to:
      1. Have a type __*TokenType*__ (like an enum) that can be used in the lexical analysis to categorize the tokens. 
      2. Please use regular expressions to identify the type of the token.
   2. Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
   3. Implement a simple parser program that could extract the syntactic information from the input text.


## Implementation

### Parsing Basics
Parsing involves analyzing text to determine its structure according to a certain grammar. In programming, parsing commonly occurs in language compilers or interpreters, where source code is transformed into a format that can be executed by a computer.

### Concept of AST
An Abstract Syntax Tree (AST) is a hierarchical representation of the syntactic structure of source code. Each node in the tree corresponds to a syntactic construct, such as expressions, statements, or declarations. ASTs are commonly used in compilers and interpreters for analyzing and transforming code.

### Additional Tasks
#### Token Type Enumeration
Define a TokenType enumeration to categorize tokens encountered during lexical analysis. Regular expressions can be used to match token patterns, such as numbers, identifiers, operators, etc.

#### AST Data Structures
Implement data structures for an AST to represent the syntactic structure of the input text. This involves defining classes for different types of nodes in the AST, such as expression nodes, statement nodes, etc.

#### Simple Parser Program
Develop a simple parser program that utilizes the TokenType enumeration and AST data structures to extract syntactic information from input text. The parser should tokenize the input text, parse tokens according to grammar rules, and construct an AST representing the parsed structure.




### LEXER Implementation



#### Main Funnction:
For the Lexer implementation, there is a Python file [Main](main.py) to start the important parts of the lexer.


```python
from lexer import Lexer

while True:
        try:
          text = input("calc > ")
          lexer = Lexer(text)
          tokens = lexer.generate_tokens()
          parser = Parser(tokens)
          tree = parser.parse()
          print(tree)
        except Exception as e:
		    print(e)
```
This Python main function creates an interactive graph processing system. It continuously prompts the user for graph commands, which are then tokenized, parsed, interpreted, and finally, the resulting graph is visualized. If any errors occur during this process, they are printed to the console.


#### Tokens

This code defines an enumeration `TokenType` and a data class `Token` to represent token types and values, facilitating lexical analysis in language processing. It is located inside [tokens.py](tokens.py)

```python
from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
        NUMBER    = 0
        PLUS      = 1
        MINUS     = 2
        MULTIPLY  = 3
        DIVIDE    = 4
        LPAREN    = 5
        RPAREN    = 6

@dataclass
class Token:
        type: TokenType
        value: any = None

        def __repr__(self):
                return self.type.name + (f":{self.value}" if self.value != None else "")


```


#### Lexer
The Lexer class tokenizes input text into tokens like DASH, LEFT, RIGHT, NAME, WEIGHT, and FINAL based on predefined rules. It's a crucial step in language processing. This class is located inn [Lexer](lexer.py)
```python
from tokens import Token, TokenType

WHITESPACE = ' \n\t'
DIGITS = '0123456789'

class Lexer:
        def __init__(self, text):
                self.text = iter(text)
                self.advance()

        def advance(self):
                try:
                        self.current_char = next(self.text)
                except StopIteration:
                        self.current_char = None

        def generate_tokens(self):
                while self.current_char != None:
                        if self.current_char in WHITESPACE:
                                self.advance()
                        elif self.current_char == '.' or self.current_char in DIGITS:
                                yield self.generate_number()
                        elif self.current_char == '+':
                                self.advance()
                                yield Token(TokenType.PLUS)
                        elif self.current_char == '-':
                                self.advance()
                                yield Token(TokenType.MINUS)
                        elif self.current_char == '*':
                                self.advance()
                                yield Token(TokenType.MULTIPLY)
                        elif self.current_char == '/':
                                self.advance()
                                yield Token(TokenType.DIVIDE)
                        elif self.current_char == '(':
                                self.advance()
                                yield Token(TokenType.LPAREN)
                        elif self.current_char == ')':
                                self.advance()
                                yield Token(TokenType.RPAREN)
                        else:
                                raise Exception(f"Illegal character '{self.current_char}'")

        def generate_number(self):
                decimal_point_count = 0
                number_str = self.current_char
                self.advance()

                while self.current_char != None and (self.current_char == '.' or self.current_char in DIGITS):
                        if self.current_char == '.':
                                decimal_point_count += 1
                                if decimal_point_count > 1:
                                        break

                        number_str += self.current_char
                        self.advance()

                if number_str.startswith('.'):
                        number_str = '0' + number_str
                if number_str.endswith('.'):
                        number_str += '0'

                return Token(TokenType.NUMBER, float(number_str))

```

Here is the hearth of this class , generate_tokens method , which categorize input into tokens. Also names and number are categorized in separate methods for readability. 


### Parser Implementation

#### Parser 

For the Parser implementation, there is a Python file [Parser](parser_.py) to start the important parts of the parser.


```python
class Parser:
	def __init__(self, tokens):
		self.tokens = iter(tokens)
		self.advance()

	def raise_error(self):
		raise Exception("Invalid syntax")
	
	def advance(self):
		try:
			self.current_token = next(self.tokens)
		except StopIteration:
			self.current_token = None

	def parse(self):
		if self.current_token == None:
			return None

		result = self.expr()

		if self.current_token != None:
			self.raise_error()

		return result

	def expr(self):
		result = self.term()

		while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
			if self.current_token.type == TokenType.PLUS:
				self.advance()
				result = AddNode(result, self.term())
			elif self.current_token.type == TokenType.MINUS:
				self.advance()
				result = SubtractNode(result, self.term())

		return result

	def term(self):
		result = self.factor()

		while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
			if self.current_token.type == TokenType.MULTIPLY:
				self.advance()
				result = MultiplyNode(result, self.factor())
			elif self.current_token.type == TokenType.DIVIDE:
				self.advance()
				result = DivideNode(result, self.factor())
				
		return result

	def factor(self):
		token = self.current_token

		if token.type == TokenType.LPAREN:
			self.advance()
			result = self.expr()

			if self.current_token.type != TokenType.RPAREN:
				self.raise_error()
			
			self.advance()
			return result

		elif token.type == TokenType.NUMBER:
			self.advance()
			return NumberNode(token.value)

		elif token.type == TokenType.PLUS:
			self.advance()
			return PlusNode(self.factor())
		
		elif token.type == TokenType.MINUS:
			self.advance()
			return MinusNode(self.factor())
		
		self.raise_error()
```


This Python code defines a simple parser for arithmetic expressions. It tokenizes input into numbers and operators, then constructs a syntax tree representing the expression's structure. It recursively parses expressions, terms, and factors, handling addition, subtraction, multiplication, division, and parentheses. Each node in the syntax tree corresponds to an operation or operand in the expression.

### Results 

```text
calc> 3+3
(3.0+3.0)
```


## Conclusion


This laboratory work delved into the fundamentals of lexical analysis, the functioning of a lexer/scanner/tokenizer, and its practical implementation in Python. Understanding lexical analysis is pivotal in breaking down source code into tokens, forming the groundwork for subsequent language processing stages.

The implementation of a Lexer class demonstrated tokenization, recognizing patterns, and handling errors according to predefined rules. The main function showcased an interactive graph processing system, where user-inputted commands were tokenized, parsed, interpreted, and visualized as a graph representation. This integration illustrated the seamless flow from lexical analysis to visualization in language processing.

By comprehending lexical analysis principles and witnessing their application through hands-on implementation, we gained insights into the intricate workings of language processing systems. This laboratory work fostered a deeper understanding of lexer functionality and its role in language interpretation and compilation processes, providing valuable practical experience in language processing concepts.
