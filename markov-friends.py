import markov
import sys


input_path = sys.argv[1]

friends_text = markov.open_and_read_file(input_path)  # open file

#split text on newlines, get rid of empty strings
script_lines = friends_text.split("\n")
script_lines = filter(None, script_lines)


def name_markov(full_text):
    """Takes the full text of the script and parses into list of names
    calls make_chains and returns a dicttionary of names"""

    names = []
    char_dict = {}

    for line in full_text:
        if ":" in line:
            line_list = line.split(":")
            names.append(line_list[0])
            char_dict[line_list[0]] = char_dict.get(line_list[0], [])
            char_dict[line_list[0]].append(line_list[1])

    for char in char_dict.keys():
        char_dict[char] = " ".join(char_dict[char])

    names_text = " ".join(names)
    names_dict = markov.make_chains(names_text, 2)

    return (names_dict, char_dict)


char_data = name_markov(script_lines)
# print script_lines
# print char_data[0]
name_str = markov.make_text(char_data[0])
# print name_str
name_order = name_str.split()
char_dict = char_data[1]


# run make_chains for every character's source text
# then run make_text on every character's chains dictionary

def char_line(char_dict, char_name):
    chains_char = markov.make_chains(char_dict[char_name])
    lines_char = markov.make_text(chains_char)
    index = lines_char.find(".")
    final_string = lines_char[:index+1]
    return final_string

# chains_rachel = markov.make_chains(char_dict['Rachel'], 2)
# lines_rachel = markov.make_text(chains_rachel)
# index = lines_rachel.find(".")

# final_string = lines_rachel[:index+1]
# print final_string

print char_line(char_dict, 'Rachel')
print name_order

for name in name_order:
    print "{}: {}".format(name, char_line(char_dict, name))
