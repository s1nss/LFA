# Regex String Generator Report

## Introduction
In this lab, we developed a Python script to generate strings based on regular expressions. Regular expressions are powerful tools for pattern matching and string manipulation. The purpose of this script is to provide a practical demonstration of how regular expressions can be used to generate strings that conform to specific patterns.

## Methodology
We implemented a Python function called `generate_string_from_regex(regex)`. This function takes a regular expression pattern as input and generates a string that matches the specified pattern. Below is a breakdown of the key components of the implementation:

1. **Parsing the Regular Expression**: The script iterates over each character in the regular expression pattern. It identifies special characters such as `[`, `]`, `*`, `+`, `{`, and `}` which denote different operations in regular expressions.

2. **Handling Character Classes**: When encountering square brackets `[...]`, the script identifies it as a character class. It randomly selects a character from the specified character class to add to the generated string.

3. **Handling Repetition Operators**: The script supports the `*`, `+`, and `{}` repetition operators. 
   - For `*`, it repeats the preceding character zero or more times.
   - For `+`, it repeats the preceding character one or more times.
   - For `{}`, it specifies a range of occurrences for the preceding character and randomly selects a number within that range.

4. **Generating the String**: As the script processes the regular expression pattern, it accumulates characters and builds the final generated string.

## Example Usage
We provided three example regular expressions (`regex_1`, `regex_2`, and `regex_3`) along with their corresponding generated strings. These examples showcase the flexibility of the script in generating strings that match diverse patterns.

## Conclusion
The Python script presented in this lab demonstrates a practical approach to generating strings based on regular expression patterns. By leveraging the power of regular expressions, developers can automate the generation of strings for various purposes such as testing, data generation, and simulation. This script can serve as a useful tool in software development and testing workflows.
