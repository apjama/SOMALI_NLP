# Somali NLP Project READ ME


##Project Description
We want to create tools and utilities for studying/doing cool stuff to the Somali languages. AlMost *all* of the Natural Language Processing libraries  out there are focused on European languages. My hope is that in the coming years, with your help, we can find ways of linking this to NLTK and other open source NLP projects. But for now, the focus is on:
* creating a definitive list of stop words (words like *he, she, they* that google likes to ignore because they don't add that much to the meaning of a search)
* reasonably accurate stemmers that take a list of words and return morphemes (the smallest syntactic version of word)
* A tokenizer that takes sentences and returns a list of words.
* a tool that takes a word and gives you the most likely word that word will have in front of it and behind it.
* statistical models on everything from spelling errors, to colocation analysis.  
##Getting Started

### Prerequisites
* [python 3] - code is written in Python
* [pip] - pip goes and fetches python libraries that you can import into your code
* [pipenv](https://pipenv.readthedocs.io/en/latest/) - creates a virtual environment so your code doesn't get ruined by code elsewhere on your computer

if you're still having difficulties, check out [this article](https://docs.python-guide.org/) and follow along.

### Installation

Clone the Repo
```
git clone https://github.com/apjama/SOMALI_NLP.git
```  
Make a virtualenv
```
pipenv shell
```  
Download all dependencies
```
pipenv install
```

## Contributing
Any one can submit a pull request if it falls into one of the areas described in the project description section.


## Author
[AP Jama](https://www.twitter.com/apjama)
