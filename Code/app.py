from datetime import datetime
import csv
import numpy as np
import asciichartpy

from rich import print
from rich import box
from rich.text import Text
from rich.align import Align
from rich.panel import Panel
from rich.layout import Layout 
from rich.table import Table

from rich.live import Live
from rich.prompt import Prompt

from rich.traceback import install
install(show_locals=True)

layout = Layout()

layout.split_column(
    Layout(name = "Header"),
    Layout(name = "Body"),
    Layout(name = "Footer")
)

layout["Body"].split_row(
    Layout(name = "Box1"),
    Layout(name = "Box2")
)

layout["Box1"].split_column(
    Layout(name = "upper_Box1"),
    Layout(name = "upper_Box2")
)

layout["Box2"].split_column(
    Layout(name = "lower_Box1"),
    Layout(name = "lower_Box2")
)

class Header:

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left")
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "📰", "[b]Protein-Packs[/]", datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="bold white")
    
class Footer:

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left")
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "💻", "[b]Stock[/]Mate", "🍞")
        return Panel(grid, style="green on black")
    
layout["Header"].size = 3
layout["Footer"].size = 3
layout["Header"].update(Header())
layout["Footer"].update(Footer())

username = Prompt.ask("Enter your Username")
password = Prompt.ask("Enter your password")
with open('C:\\Users\\hadir\\Documents\\VSC - Projects\\Python\\Protein-Packs\Code\\logIn_Details.txt','r') as file:
                  for line in file:
                        usernames = line.split()[0]
                        passwords = line.split()[1]
                        
if ((username == usernames ) and (password == passwords)):
    print(Panel.fit(f"[b]Welcome back {username}, System is updating ...[/]", title = "Welcome", title_align = "left", border_style = "bold green", box = box.SQUARE))
else:
    print(Panel("Username or Password does not match the database", border_style = "bold red", box = box.SQUARE))
