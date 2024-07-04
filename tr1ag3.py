import subprocess
import os
import sys
import re
import argparse
import threading

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='the file to analyse', required=True)
    return parser.parse_args()

class Triage():
    def __init__(self):
        self.commands = ["windows.cmdline", "windows.pslist", "windows.netscan", "windows.filescan"]
        self.suspicious_commands = ["windows.mbrscan", "windows.mutantscan", "windows.malfind"]

    def run_command(self, dump_file, command, output_folder):
        # Command format for Volatility 3
        command_format = f"vol.py -f {dump_file} {command}"

        # Execute Volatility command
        output_file = os.path.join(output_folder, f"{command}_output.txt")
        with open(output_file, 'w') as f:
            subprocess.run(command_format, shell=True, stdout=f, stderr=subprocess.PIPE)

        print(f"{command} command executed. Results saved to {output_folder}/{command}_output.txt")
        
    def init(self, dump_file):
        output_folder = "tr1ag3-output"
        suspicious_folder = os.path.join(output_folder, "suspicious")

        # Create output and suspicious folders if they don't already exist
        os.makedirs(output_folder, exist_ok=True)
        os.makedirs(suspicious_folder, exist_ok=True)

        threads = list()
        # Run each Volatility3 command and save output to a text file in the appropriate folder
        for command in self.commands:
            x = threading.Thread(target=self.run_command, args=(dump_file, command, output_folder))
            threads.append(x)
            x.start()

        # Run each malware analysis related Volatility3 command and save output to a text file in the suspicious folder
        for command in self.suspicious_commands:
            x = threading.Thread(target=self.run_command, args=(dump_file, command, suspicious_folder))
            threads.append(x)
            x.start()

def main(dump_file):
    worker = Triage()
    worker.init(dump_file)

if __name__ == "__main__":
    opts = get_args()

    sys.exit(main(opts.file))
