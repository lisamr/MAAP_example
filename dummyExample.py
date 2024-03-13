# code to run dummy example
import os
import constants

def make_statement(love_object: str, hate_object: str):
    string = f"I love {love_object} and I hate {hate_object}."
    return string

def save_statement(string: str, dir=constants.output_dir, filenm='dummy_output.txt'):
    os.makedirs(dir, exist_ok=True)
    file_path = os.path.join(dir, filenm)
    # opens file in file_path in write mode, writes string. 
    # `with` ensures file gets closed when done
    with open(file_path, 'w') as f:
        f.write(string)

def run_example(love_object: str, hate_object: str):
    string = make_statement(love_object, hate_object)
    save_statement(string)
    print(string)

if __name__ == "__main__":
    run_example('my cat Lobster', 'pickles')