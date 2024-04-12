# Tr1ag3
Data sorting tool for forensic memory analysis

Based on volatility commands, Tr1ag3 is a python tool that helps you to retrieve information at the beginning of a forensic memory analysis.
It requires a memory dump file as an input. 
It creates text files as outputs named after the volatility command in a folder named "tr1ag3-output".

# Requirements

volatility2 or volatility3 installed and working as a cmdline > ``` $ vol.py -f {dump file} ```

# Usage
```sh
$ python tr1ag3.py -h
usage: tr1ag3.py [-h] -v VERSION -f FILE

options:
  -h, --help            show this help message and exit
  -v VERSION, --version VERSION
                        the version of volatility
  -f FILE, --file FILE  the file to analyse
```

### Default usage
```sh
$ python tr1ag3.py -v 3 -f dump_img
```

### Outputs
```sh
$ ls tr1ag3-output/
windows.cmdline_output.txt  windows.filescan_output.txt  windows.netscan_output.txt  windows.pslist_output.txt
```

# Ideas of update

- Retrieve the cache files of chrome,firefox,ie 
- create sub folder "suspicious" and use yara rules or something else to identify malicious files/scripts. Put the suspicious files in this same sub folder
- add a requirements.txt file containing all packages necessary (volatility plugins for yara/other browser history) 
- simplify the program
