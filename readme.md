# Somali NLP

## Project Description
We want to create tools and utilities for studying/doing cool stuff to the Somali language. Almost *****all**** of the Natural Language Processing libraries out there are focused on European languages. My hope is that in the coming years, with your help, we can find ways of linking this to NLTK and other open source NLP projects. But for now, ****the focus is on****:
* Creating a definitive list of stop words (words like *he, she, they* that google likes to ignore because they don't add that much to the meaning of a search)
* Reasonably accurate stemmers that take a list of words and return morphemes (the smallest syntactic version of word)
* A tokenizer that takes sentences and returns a list of words.
* A tool that takes a word and gives you a list of words it likes be around (colocation).
* Statistical models on everything from spelling errors, to colocation analysis.  
## Getting Started
Not knowing Python shouldn't stop you! Please get involved. If you know what you're doing, please build a feature and submit a pull request for it!
### Prerequisites
* [python 3] (https://wiki.python.org/moin/BeginnersGuide/Download) - code is written in Python
* [pip] (https://pip.pypa.io/en/stable/installing/) - pip goes and fetches python libraries that you can import into your code
* [pipenv](https://pipenv.readthedocs.io/en/latest/) - creates a virtual environment so your code doesn't get ruined by code elsewhere on your computer
* [git] (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) - this is thing used for version controlled, but we'll need it now so you can download this repo into your computer.

if you're still having difficulties, check out [this article](https://docs.python-guide.org/) and follow along.

### Installation

Clone the repo
```
git clone https://github.com/apjama/SOMALI_NLP.git
cd SOMALI_NLP
```  
Make a virtualenv and fire it up
```
pipenv shell
```  
Install all dependencies
```
pipenv install
```

## Contributing
Any one can submit a pull request if it falls into one of the areas described in the project description section.

## Data
The data used in this project comes from a bunch of different places. In each case, we will cite where the data came from so others can also access it.

* [This Corpus by Masaryk University](http://habit-project.eu/wiki/SetOfEthiopianWebCorpora) | Supposedly this has 80 million tokens (individual words). For a cleaned up version, please see the raw folder, under [json_tokens](https://github.com/apjama/SOMALI_NLP/tree/master/raw/json_tokens).

## Author
[AP Jama](https://www.twitter.com/apjama)
