# Random Password Generator
---
This application is a simple password generator written in **Python 3**. It creates a string of 8 -16 characters in length under the typical password requirements of at least 1 of each of the following:
* Uppercase
* Lowercase
* Number
* Symbol

In addition to these, the requirement for the string to contain no substrings that are considered words has also been applied to this application.

## Installation
---
Clone the repository to a directory of your liking. Once downloaded, navigate to the directory and run the following command:

`pip3 install -r requirements.txt`

This uses the Hunspell module to check for words. As such, you may need to configure your environment for this module. All information regarding Hunspell and its requirements can be found in the following [link](https://github.com/blatinier/pyhunspell).

## Usage
---
In the application's directory, run the following:

`python3 run.py`
