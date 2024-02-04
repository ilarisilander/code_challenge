# Word Counter - Code Challenge
A simple CLI application that will take a text file path as argument and then count how many times
the file name appears in the text file.

# Table of contents
<!--ts-->
   * [Table of contents](#table-of-contents)
   * [The Challenge](#the-challenge)
   * [Pre-requisites](#pre-requisites)
   * [Installation](#installation)
   * [How to](#how-to)
<!--te-->

# The Challenge
  ### Instructions
  Write a console program that takes one argument, a path to a file.
  Open that file and count how many times its filename (minus the file extension) occurs in the file's contents.
  Example: If the argument is "myfile.txt" it should count how many times the string "myfile" occurs in it.

  * ##### In the task instructions, there was a lot about C# and F#, but I was recommended to use my strongest programming language

  ### My thoughts about the requirements and instructions
  * #### Input arguments
    * Should it be able to take more than .txt files?
      My assumption and decision is to only use .txt files.
    * The validator should validate for capital letters also
      The argument is set to lower case before it goes to the validator.
    * What should happen if there is no argument when executed?
      This is handled by the arg parser with the "required" option
    * If there is more than one argument?
    * If user adds spaces in file name, then that will throw an exception.
      We don't want spaces in our text file names...

  * #### Word search
    ##### Instructions does not clarify special characters in the file name:
     If file name is foot.txt
     * "foot" - character before and after the actual word. Could be ' and () also.
     * football - word is a part of another word
     * foot. - word has a trailing symbol. Could be ! . , : or any other symbol.
     * .foot - leading symbol, same as above.
     * Foot/FOOT - capital/lower letters and so on...
    
      My assumption is that all hits will be detected.

  * #### Visualization
    ##### The instructions does not specify how to display the word count result
    * I decide to print it out to the user in the terminal in this fashion.
      "The word [fetch name from file object] appeared [x] times"

  * #### Path
    * Should it work with a relative path or only full path?
      I decided that it should take both relative and full path

  * #### Test cases
    * I like to write my unit tests without any file dependencies
    * I also like to write my test cases with as much coverage as possible
    * I try to make the code easy to test. To make it in small chunks of code
  
  * #### Exception handling
    ##### Things that I decided to include in exception handling
    * If the user inserts a path that does not have a file in the base of the path
    * To check that the file has .txt as extension
    * The user could add a path with spaces in the file name

# Pre-requisites
* Python 3.8 or higher
* GIT
* A text file with a name and a .txt prefix.

Download Python [here](https://www.python.org/downloads/)

# Installation
Download the necessary files
```bash
git clone https://github.com/ilarisilander/code_challenge.git
cd code_challenge
```

Install dependencies
```bash
pip install -r requirements.txt
```

# How to
There are some files in /code_challenge/files to use unless you want to create your own files.

### Help in the application
```bash
python WordCounter.py --help
```

### Add a text file path as argument
```bash
python WordCounter.py --file_path c:/path/to/text_file.txt
```

### Run the test cases
Given that you are in the root folder of the project (code_challenge)
* Run with coverage (all tests)
  ```bash
  coverage run -m unittest tests/test*
  ```
* Run with coverage (single test file)
  ```bash
  coverage run -m unittest tests/test_CommandLine.py
  coverage run -m unittest tests/test_Files.py
  ```
* Show the coverage report
  ```bash
  coverage report
  ```
* Run without coverage (all files)
  ```bash
  python -m unittest tests/test*
  ```
