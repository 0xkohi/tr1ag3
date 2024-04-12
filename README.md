# Tr1ag3
Data sorting tool for forensic memory analysis

Based on volatility commands, Tr1ag3 is a python tool that helps you to retrieve information at the beginning of a forensic memory analysis.
It requires a memory dump file as an input. 
It creates text files as outputs named after the volatility command in a folder named "tr1ag3-output".

# Requirements

volatility2 or volatility3 installed and working as a cmdline > ``` $ vol.py -f {dump file} ```

# Usage

```py
$ python tr1ag3.py -h
usage: tr1ag3.py [-h] -v VERSION -f FILE

options:
  -h, --help            show this help message and exit
  -v VERSION, --version VERSION
                        the version of volatility
  -f FILE, --file FILE  the file to analyse


$ python tr1ag3.py -v 3 -f dump_img
```

# Ideas of update

- Retrieve the cache files of chrome,firefox,ie 
- create sub folder "suspicious" and use yara rules or something else to identify malicious files/scripts. Put the suspicious files in this same sub folder
- add a requirements.txt file containing all packages necessary (volatility plugins for yara/other browser history) 
- simplify the program
