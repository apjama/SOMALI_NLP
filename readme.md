# Somali NLP

## Project Description
We want to create tools and utilities for studying/doing cool stuff with the Somali language. Almost *****all**** of the Natural Language Processing libraries out there are focused on European languages. My hope is that in the coming years, with your help, we can find ways of linking this to NLTK and other open source NLP projects. But for now, ****the focus is on****:
* Creating a definitive list of stop words (words like *he, she, they* that google likes to ignore because they don't add that much to the meaning of a search)
* Reasonably accurate stemmers that take a list of words and return morphemes (the smallest syntactic version of word)
* A tokenizer that takes sentences and returns a list of words.
* A tool that takes a word and gives you a list of words it likes be around (colocation).
* Statistical models on everything from spelling errors, to Levenshtein distances (if you're into that sort of thing!)  
## Getting Started
Not knowing Python shouldn't stop you! Please get involved. If you know what you're doing, please build a feature and submit a pull request for it!
### Prerequisites
* [python 3](https://wiki.python.org/moin/BeginnersGuide/Download)
* [pip](https://pip.pypa.io/en/stable/installing/)
* [pipenv](https://pipenv.readthedocs.io/en/latest/)
* [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

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
Any one can submit a pull request if it falls into one of the areas described in the project description. Hit me up on my [Twitter](https://twitter.com/apjama).

## Data
This repo is primary is the codebase for the project. If you’re looking for the data that goes along with it, please check the [Somali NLP Data](https://github.com/apjama/Somali_NLP_data) repo. 



