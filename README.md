# SlackInviter
A script to automate inviting multiple Slack users to multiple channels.

To use:
1) Open the Slack desktop application
2) Add all usernames to `usernames.txt` as a newline-delimited list that you would like to auto-add to channels.
3) Edit `SlackInviter.py' to specify the channel names you would like to auto-add the users to.
4) Run `python SlackInviter.py` to run the script.  Note that for each specified channel the script will *temporarily take over control of your computer* to automate the process of typing in Slack commands to add each user.  After each channel it will prompt you via terminal to continue.  While the script is inviting users you are unable to interrupt the script.