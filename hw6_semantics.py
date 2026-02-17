import sys
import os
import nltk
from nltk import grammar, parse

def get_inputs():
    grammar_input = sys.argv[1]
    input_sentences = sys.argv[2]
    output_file = sys.argv[3]

    if os.path.exists(output_file):
        os.remove(output_file)
    
    return grammar_input, input_sentences, output_file

def load_grammar(grammar_input):
    abs_path = os.path.abspath(grammar_input)
    grammar_url = f"file://{abs_path}"
    grammar = nltk.data.load(grammar_url)
    parser = parse.FeatureChartParser(grammar)
    return parser

def read_sentences(input_sentences, output_file, parser):
    with open(input_sentences, 'r', encoding='utf8') as file:
        lines = file.readlines()
        with open(output_file, "a") as output:
            for line in lines:
                if line:
                    tokens = line.split()
                    trees =  list(parser.parse(tokens))
                    print(f"{line.strip()}", file=output)
                    if trees:
                        semantic_rep = trees[0].label()['SEM']
                        print(f"{semantic_rep} \n", file=output)

def main():
    grammar_input, input_sentences, output_file = get_inputs()
    parser = load_grammar(grammar_input)
    read_sentences(input_sentences, output_file, parser)

if __name__ == '__main__':
    main()