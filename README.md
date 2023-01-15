# python-skeleton
## Standard set of files to start small to medium python project

Idea is to have python skeleton with all the files needed to start a small to medium python project. 
This is a work in progress and I will keep adding more files as I go along.

## Usage

Simply clone this repo and start working on your project:
```git
git clone https://github.com/dvesic/python-skeleton
```

## Environment

This is done along with https://github.com/dvesic/perfect-python-4-windows - please review this repo for more details.

(specifically, *bin/* files are described there)

## Files

- *config.ini* - configuration file; set specific parameters in [App] section and add code to retrieve them in
*config.py* file. Set at least *description* parameter.
- *main.py* - main file; this is where you start your project; set __author__ and __version__ variables 

## Logging

Basic logging is done over *file_logging.py* file. It logs *info* and *error* messages to *logs/* folder.

You can change actual locations of log files in *config.ini* file, [Logs] section. You can also turn off logging there
as well, or over command line 