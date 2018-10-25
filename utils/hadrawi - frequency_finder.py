import sys
import pandas as pd

def tokenize(lines):
    words = {}

    for line in lines:
        items = line.translate(
            {ord(c): "" for c in '\'!@"#$%^&*()[]{};:,./<>?\|`~-=_+'}).lower().strip().split(' ')
        for word in items:
            if word in words:
                words[word] += 1
            else:
                words[word] = 0
    return words

def main():
    file = sys.argv[1]
    words = tokenize(open(file).readlines())
    pd.DataFrame(list(words.items())).to_csv('output.csv', index=True)


if __name__ == '__main__':
    main()
