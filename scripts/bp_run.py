#!/usr/bin/env python3
import sys
import subprocess

DESCRIPTION = """
Default ENTRYPOINT is 'bp_run.py' script.
With no args passed, the script will simply run `bpython` command.
With args passed, the script will try to install ech argument with 'pip3'
before running `bpython` command. It is usefull when you need to have some
libraries installed and available within `bpython`
"""

if len(sys.argv) > 1:
    for help_ in ('-h', 'help', '--help'):
        if help_ in sys.argv:
            print(DESCRIPTION)
            sys.exit(0)
    for lib in sys.argv[1:]:
        subprocess.run(['pip3', 'install', lib], check=False)

subprocess.run(['bpython'])
