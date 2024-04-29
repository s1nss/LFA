import random

def generate_string_from_regex(regex):
    current_group = ''
    word = ''
    pr_group = ''
    brackets = False
    curly_brace = False

    for char in regex:
        if char == '[':
            brackets = True
            current_group = ''
        elif char == ']':
            brackets = False
            word = word + random.choice(current_group)
            pr_group = current_group
            current_group = ''
        elif char == '*':
            pr_elem = regex[regex.index(char) - 1]
            word += pr_elem * random.randint(0, 5)
        elif char == '+':
            pr_elem = regex[regex.index(char) - 1]
            word += pr_elem * random.randint(1, 5)
        elif char == '{':
            curly_brace = True
            number = int(regex[regex.index(char) + 1 : regex.index('}')])
            word += random.choice(pr_group) * number
        elif char == '}':
            curly_brace = False
        elif char.isalnum() and not brackets and not curly_brace:
            word += char
        else:
            current_group += char

    return word

# def show_processing_sequence(regex_pattern):
#     sequence = []
#     current_group = ''
#     brackets = False
#     for char in regex_pattern:
#         if char == '[':
#             brackets = True
#             current_group = ''
#         elif char == ']':
#             brackets = False
#             sequence.append(f"Match one element from '{current_group}' list")
#             current_group = ''
#         elif char == '*':
#             sequence.append("Match zero or more occurrences of the preceding element")
#         elif char == '+':
#             sequence.append("Match one or more occurrences of the preceding element")
#         elif char == '{':
#             sequence.append("Specify a range of occurrences")
#         elif char == '}':
#             sequence.append("End of range specification")
#         elif char == '(':
#             sequence.append("Start of a group")
#         elif char == ')':
#             sequence.append("End of a group")
#         elif char.isalnum() and not brackets:
#             sequence.append(f"Match '{char}'")
#         else:
#             current_group += char
#     return sequence

regex_1 = r'[ST][UV]W*Y+24'
generated_str = generate_string_from_regex(regex_1)
print("Generated string matching the regex:", generated_str)

# sequence = show_processing_sequence(regex_1)
# for step, explanation in enumerate(sequence, start=1):
#     print(f"Step {step}: {explanation}")
# print()

regex_2 = r'L[MN]OOOP*Q[23]'
generated_str = generate_string_from_regex(regex_2)
print("Generated string matching the regex:", generated_str)

# sequence = show_processing_sequence(regex_2)
# for step, explanation in enumerate(sequence, start=1):
#     print(f"Step {step}: {explanation}")
# print()

regex_3 = r'R*S[TUV]W[XYZ]{2}'
generated_str = generate_string_from_regex(regex_3)
print("Generated string matching the regex:", generated_str)

# sequence = show_processing_sequence(regex_3)
# for step, explanation in enumerate(sequence, start=1):
#     print(f"Step {step}: {explanation}")
# print()
