## Folder Description

This is folder houses small scripts and function for transforming raw linguistic data in more manageable bits and bobs. Here are a list of function it houses. 


### tokenize_directory  

Run this from the command line in the utils file. Its a script that takes one argument (string) of the folder that houses the text files you want to tokenize. 

```
python tokenize_directory.py folder_directory
```  

It might look something like this:

```
python tokenize_directory.py "raw/raw_text - wikipedia/"
```

Note: the text files should be in the parent directory. If you want to change this behavior, then edit the main function itself. 

### hadrawi - frequency_finder

This script was contributed by [Mohamed Ainab](https://twitter.com/mohamedainab). It can be found in the original repo[here] (https://github.com/codeforsomalia/hadrawi). 