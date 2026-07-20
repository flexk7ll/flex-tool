LICENSE = """ by FLEX TEAM
 Discord Server: https://discord.gg/rees7q7qX4  """
# 
# This is the source code for my dank memer gridner, if you want to create a custom action you can head down to line 42, the bot will run the command then wait the set amount of seconds and type it agein, do whatever you want you can add stuff such as "pls steal..." or "pls buy..."
# 

from colored import fg
import requests
import threading
import time
import random

r = fg(241) # Setup color variables
r2 = fg(255)
b = fg(31)
w = fg(15)

def start():
    token = input(f"\n {r2}[{b}?{r2}] Token: ")
    channel = input(f" {r2}[{b}?{r2}] Channel ID: ")

    def execute_command(command = "", cooldown = 0):
        print(f"{r2}[{b}!{r2} Loaded: '{command}' with cooldown of {cooldown} Seconds")
        while True:
            requests.post(
                f"https://discord.com/api/channels/{channel}/messages",
                data = {'content': command},
                headers = {
                    'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
                    'Authorization' : token
                }
            )
            print(f"{r2}[{b}+{r2}] '{command}' Ran successfully")

            time.sleep(cooldown + random.randint(2, 10))

    commands = { # Command : Cooldown in seconds, remember a comma after each line
        "pls beg" : 45,
        "pls hunt" : 40,
        "pls fish" : 40,
        "pls daily" : 86400
    }

    print()

    for cmd, cooldown in commands.items():
        threading.Thread(target = execute_command, kwargs = {"command" : cmd, "cooldown" : cooldown}).start()
        time.sleep(5)
