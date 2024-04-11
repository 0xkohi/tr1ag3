# For-init
Data sorting tool for forensic analysis

For-init is a python program that helps retrieve the basic information during forensic analysis, it requires a dump file as an input. It creates text files as outputs named after the volatility command in a folder named "result_initial_triage".

# Requirements

volatility2 installed and working as a cmdline > $ volatility -f ...

# Usage

python3 initial_triage.py (memory dump file)

# Ideas of update

- Put the cache files of chrome,firefox,ie in the sub-folder browser 
- look for malicious/suspect strings and write them in a file(ie. might-be-interesting.txt)
- create sub folder "suspicious" and use yara rules or something else to identify malicious files/scripts. Put the suspicious files in this same sub folder
- add a requirements.txt file containing all packages necessary (volatility plugins for yara/other browser history) 
- simplify the program
