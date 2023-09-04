# sort-analyzer
An alogrithm analyzer tool for few famous sort algorithms

## Pre-requesties
* Python 3.6+ (tested on python version: `Python 3.11`)

## Setup
```bash
$ git clone https://github.com/KR-Ravindra/sort-analyzer && cd sort-analyzer
$ python3 -m venv .env
$ source .env/bin/activate
(.env) $ pip3 install -r requirements.txt # Install dependencies from the file 'requirements' in current directory to your local environment
```

## Getting Started
```bash
$ python3 main.py
# Asks for user input of an array and algo_name, else defaults to bubble sort and predefined elements
```
## To Contributors
```bash
(.env) $ pip3 freeze > requirements.txt
$ git add . && git commit -m "My Fancy Commit Message"
$ git push origin mybranchname
```


## Extra Features
- [x] Live Sorting
- [ ] Facility to compare across all available algorithms 

> This is a group assignment for CPSC 535 class for semester Fall 2023 at Cal State University, Fullerton