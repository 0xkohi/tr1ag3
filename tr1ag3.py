import subprocess
import os
import sys
import re

def get_volatility_version():
    # Execute vol.py command to get Volatility version
    result = subprocess.run("vol.py 2>&1", shell=True, capture_output=True, text=True)
    volatility_match = re.search(r"Volatility", result.stdout)

    if volatility_match:
        return 2  # Assuming Volatility 2.x
    else:
        return 3  # Assuming Volatility 3.x

def find_profile(dump_file, major_version):
    if major_version == 2:
        # Execute vol.py command to get profile (only for Volatility 2.x)
        command = f"vol.py -f {dump_file} imageinfo"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Extract the profiles
        profile_match = re.search(r"Profile\(s\) : (.+)", result.stdout)
        
        if profile_match:
            return profile_match.group(1).strip().split(",")[0]  # Get the first profile
        else:
            return None
        
    return None

def run_volatility_command(dump_file, profile, command, output_folder, major_version):
    if major_version is None:
        print("Error: Volatility not found.")
        sys.exit(1)

    # Determine command format based on Volatility version
    if major_version == 2:
        command_format = f"vol.py -f {dump_file} --profile={profile} {command}"
    else:
        command_format = f"vol.py -f {dump_file} {command}"

    # Execute Volatility command
    output_file = os.path.join(output_folder, f"{command}_output.txt")
    with open(output_file, 'w') as f:
        subprocess.run(command_format, shell=True, stdout=f, stderr=subprocess.PIPE)

def main():
    # Check if a dump file is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 tr1ag3.py <dump_file>")
        sys.exit(1)

    dump_file = sys.argv[1]
    output_folder = "tr1ag3-output"

    # Find the Volatility version
    major_version = get_volatility_version()

    # Check Volatility version and get profile if needed
    if major_version is not None:
        profile = find_profile(dump_file, major_version)
        if profile is not None:
            print(f"Profile found: {profile}")

            # Create output folder if it doesn't exist
            os.makedirs(output_folder, exist_ok=True)

            # Define Volatility commands to run
            if major_version == 2:
                volatility_commands = ["consoles", "iehistory", "pslist", "netscan", "filescan"]
            else:
                volatility_commands = ["windows.cmdline", "windows.pslist", "windows.netscan", "windows.filescan"]

            # Run each Volatility command and save output to a text file in the appropriate folder
            for command in volatility_commands:
                run_volatility_command(dump_file, profile, command, output_folder, major_version)
                print(f"{command} command executed. Results saved to {output_folder}/{command}_output.txt")
        else:
            print("Profile not found. Unable to proceed.")
    else:
        print("Error: Volatility not found.")

if __name__ == "__main__":
    main()
