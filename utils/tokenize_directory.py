import os, sys
import json

from genericpath import isfile
from os.path import join
from pathlib import Path
from nltk.tokenize.regexp import RegexpTokenizer



def tokenize_large_text_file(file_name, file_location):
    tokens_array = set()
    file = os.path.join(file_location, file_name)
    with open(file,'r') as file:
        for line in file:
            tokenizer = RegexpTokenizer('\s+', gaps=True)
            tokens_array.update(tokenizer.tokenize(line))
    tokens_dict = {str(file_name) + " - {} tokens".format(file_name): list(tokens_array)}
    with open('tokens taken from - {} - .json'.format(str(file_name)), 'w') as f:
        json.dump(tokens_dict, f)


if __name__ == "__main__":
    parent_path = Path(os.getcwd()).parents[0]
    
    try:
        file_location = os.path.join(parent_path, sys.argv[1])
        print({"files found": len(os.listdir(file_location))})
        for file in [f for f in os.listdir(file_location) if isfile(join(file_location, f))]:
            tokenize_large_text_file(file, file_location)
    
    except FileNotFoundError:
        print("Double check file location {} for me chief because I can't find it.".format(file_location))