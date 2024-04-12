import subprocess
import os
import sys
import re
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', help='the version of volatility', required=True)
    parser.add_argument('-f', '--file', help='the file to analyse', required=True)

    return parser.parse_args()

class Triage():
    def __init__(self, ver=3):
        
        if ver == 3:
            self.commands = ["windows.cmdline", "windows.pslist", "windows.netscan", "windows.filescan"]
        else:
            self.commands = ["consoles", "iehistory", "pslist", "netscan", "filescan"]
        self.ver = ver

    def find_profile(self, dump_file):
        # Execute vol.py command to get profile (only for Volatility 2.x)
        command = f"vol.py -f {dump_file} imageinfo"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Extract the profiles
        profile_match = re.search(r"Profile\(s\) : (.+)", result.stdout)
        
        return profile_match if profile_match == None else profile_match.group(1).strip().split(",")[0]
    
    def run_command(self, dump_file, profile, command, output_folder):
        # Determine command format based on Volatility version
        if self.ver == 2:
            command_format = f"vol.py -f {dump_file} --profile={profile} {command} 2>&1"
        else:
            command_format = f"vol -f {dump_file} {command} 2>&1"

        # Execute Volatility command
        output_file = os.path.join(output_folder, f"{command}_output.txt")
        with open(output_file, 'w') as f:
            subprocess.run(command_format, shell=True, stdout=f, stderr=subprocess.PIPE)
        
    def init(self, dump_file):
        output_folder = "tr1ag3-output"

        # Create output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)
        
        profile = None
        if self.ver == 2:
            # Check Volatility version and get profile if needed
            profile = self.find_profile(dump_file, self.ver)
            if profile is not None:
                print(f"Profile found: {profile}")
            else:
                print("Profile not found. Unable to proceed.")
                return
        
        # Run each Volatility command and save output to a text file in the appropriate folder
        for command in self.commands:
            self.run_command(dump_file, profile, command, output_folder)
            print(f"{command} command executed. Results saved to {output_folder}/{command}_output.txt")


def main(major_version, dump_file):
    worker = Triage(major_version)
    worker.init(dump_file)

if __name__ == "__main__":
    opts = get_args()

    sys.exit(main(opts.version, opts.file))
