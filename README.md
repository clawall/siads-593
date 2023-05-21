# siads-593
Shared repository for team `04-clawall-rtambyra-bluegene` project on SIADS-593.

This repository contains a subset of available packages on the Coursera repository and is meant to ease the collaboration between the team as well as help track our progress.

## Team members
- César Lawall - clawall
- Wei-Chi Lai - bluegene

## Pre-requisities
- Python 3
- Python virtualenv

### About Virtualenv
Virtualenv is an amazing tool that helps us isolate our environment.  By containing our libraries within its folder structure, we avoid the use of libraries installed on our local OS and can easily share the exact environment amongst the team members.

You can have as many virtual environments as you want but it's a good idea to use a single environment for a specific project.  Each time we add a new library, we need to save it's name (following the pattern`library-name==version`) on a file called `requirements.txt`.  If we ever need to recreate an environment, we can just use the commands specified on the next session to create it.

Please refer to its [documentation](https://docs.python.org/3/library/venv.html) for more instructions and a how-to-use guide.

## Installation
By having Python 3 and Virtualenv installed (please refer to the guides for your operating system within their respective docs) we just need to start our virtual environment and install the libraries contained within our requirements file.

Warning:  The first command on the shell bellow assumes that your Python3 binary is called "python3" and is accessible on the OS path.  Please update this accordingly.

```console
# 1. Creates a new environment with the python executable "python3" on the folder "./.env"
virtualenv -p python3 .env

# 2. Activates the newly created virtual environment
source .env/bin/activate

# 3. Installs the libraries indicated on the "requirements.txt" file
pip install -r requirements.txt

# 4. Starts Jupyter Lab so we can work (it will be opened on a browser)
jupyter lab
```

## Folder structure
- ./ --> Project settings
- ./notebooks/ --> Notebooks for the project
- ./notebooks/assets/ --> General resources, including datasets
