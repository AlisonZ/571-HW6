import sys
import os

def get_inputs():
    grammar_input = sys.argv[1]
    input_sentences = sys.argv[2]
    output_file = sys.argv[3]

    if os.path.exists(output_file):
        os.remove(output_file)
    
    return grammar_input, input_sentences, output_file

def read_sentences(input_sentences, output_file):
    with open(input_sentences, 'r', encoding='utf8') as file:
        lines = file.readlines()
        with open(output_file, "a") as output:
            for line in lines:
                print(f"XXXX {line}", file=output)

def main():
    grammar_input, input_sentences, output_file = get_inputs()
    read_sentences(input_sentences, output_file)

if __name__ == '__main__':
    main()