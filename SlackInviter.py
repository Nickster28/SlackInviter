import os
from time import sleep

# ORIGINALLY WRITTEN BY ANTON APOSTOLATOS (antonaf@stanford.edu)

# List of channels to add users to (without the '#')
SLACK_CHANNELS = ['channel1', 'channel2', 'channel3']

# Newline-separated list of Slack usernames to invite to the above channels
USERNAMES_FILE = './usernames.txt'

'''
FUNCTION: writeToSlack
----------------------
Parameters:
    command - the command to input into the Slack desktop application

Returns: NA

Sets the Slack process to be frontmost, and then input 1 character at a time
from the given command, followed by ENTER to execute it.
----------------------
'''
def writeToSlack(command):
    first = """
    osascript -e 'tell application "System Events" to tell process "Slack" 
        set frontmost to true 
        delay 0.04
        keystroke "a" using {command down}
        keystroke (ASCII character 127)
        """
    
    keystrokes = """"""

    for ch in command:
        keystrokes += """\n\tdelay 0.04\n\tkeystroke "%s" """ % ch

    keystrokes += """\nkeystroke return"""
    last = """\ndelay 0.04\nend tell' """

    os.system(first + keystrokes + last)
    sleep(0.04)

# Add all usernames to each channel
for channel in SLACK_CHANNELS:
    with open(USERNAMES_FILE) as f:
        for username in f.readlines():
            writeToSlack('/invite @%s %s' % (username, channel))
        raw_input('Press Enter to continue.')
