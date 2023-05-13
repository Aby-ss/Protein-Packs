from datetime import datetime
import csv
import time
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
from rich.progress import track
from rich.progress import Progress

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
    Layout(name = "left_Box1"),
    Layout(name = "left_Box2")
)

layout["Box2"].split_column(
    Layout(name = "right_Box1"),
    Layout(name = "right_Box2", size=27)
)

layout["right_Box1"].split_column(
    Layout(name = "Discount_Panel1", size = 4),
    Layout(name = "Discount_Panel2", size = 4),
    Layout(name = "Discount_Panel3", size = 4)
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
    

def Order_Database():
    orderDB = Table(expand = True)
    orderDB.add_column("Order No.", justify = "center", ratio = 1)
    orderDB.add_column("Location", justify = "center")
    orderDB.add_column("Status", justify = "right")
    orderDB.add_column("Customer name", justify = "right")
    orderDB.add_row("384947273", "8th Street, Manchester", "[b blue]Shipped", "Lucy")
    orderDB.add_row("732487621", "17th Avenue, London", "[b red]Cancelled", "Tom")
    orderDB.add_row("959337388", "1st Lane, Liverpool", "[b green]Processing", "Emily")
    orderDB.add_row("222983753", "15th Road, Glasgow", "[b orange]Pending", "Jake")
    orderDB.add_row("486366593", "21st Boulevard, Edinburgh", "[b greed]Delivered", "Sophie")
    orderDB.add_row("687292983", "12th Avenue, Bristol", "[b red]Cancelled", "Oliver")
    orderDB.add_row("789274839", "9th Street, Newcastle", "[b green]Processing", "Amelia")
    orderDB.add_row("346827284", "20th Road, Sheffield", "[b blue]Shipped", "Harry")
    orderDB.add_row("574839273", "3rd Lane, Leeds", "[b green]Delivered", "Emma")
    orderDB.add_row("273728384", "6th Boulevard, York", "[b orange]Pending", "James")
    orderDB.add_row("943728291", "7th Street, Cardiff", "[b green]Processing", "Grace")
    orderDB.add_row("385728394", "2nd Lane, Southampton", "[b blue]Shipped", "Ryan")
    orderDB.add_row("938472847", "10th Road, Oxford", "[b red]Cancelled", "Ava")
    orderDB.add_row("568379274", "5th Boulevard, Cambridge", "[b green]Delivered", "Ben")
    
    return orderDB

def Discounts_Promotions_1():
    panel1 = Panel("Get 25% off on our Protein Shack bottles", title = "[b]🔔 New Discount Offer", title_align = "left", border_style="bold white", box = box.SQUARE)
    
    return panel1

def Discounts_Promotions_2():
    panel2 = Panel("Experience a new spicy chicken meal deal", title = "[b]🔔 New Discount Offer", title_align = "left", border_style="bold white", box = box.SQUARE)
    
    return panel2

def Discounts_Promotions_3():
    panel3 = Panel("50% off on our latest GYMBRO clothes, Get yours now", title = "[b]🔔 New Discount Offer", title_align = "left", border_style="bold white", box = box.SQUARE)
    
    return panel3

def weight_graph():
    y_values = np.random.uniform(low=0.0, high=10.0, size=50)

    # create chart using asciichartpy module
    chart = asciichartpy.plot(y_values, {"height": 25, "width": 50})
    
    return Panel(chart, title="Weght Analysis", title_align = "left", border_style = "bold white", box = box.SQUARE)

layout["Header"].size = 3
layout["Footer"].size = 3
layout["Header"].update(Header())
layout["Footer"].update(Footer())
layout["left_Box1"].update(Order_Database())
layout["Discount_Panel1"].update(Discounts_Promotions_1())
layout["Discount_Panel2"].update(Discounts_Promotions_2())
layout["Discount_Panel3"].update(Discounts_Promotions_3())
layout["right_Box2"].update(weight_graph())


username = Prompt.ask("Enter your Username")
password = Prompt.ask("Enter your password")
weight_target = Prompt.ask("Enter your target")
with open('C:\\Users\\hadir\\Documents\\VSC - Projects\\Python\\Protein-Packs\Code\\logIn_Details.txt','r') as file:
                  for line in file:
                        usernames = line.split()[0]
                        passwords = line.split()[1]
                        target = line.split()[2]
                        
if ((username == usernames ) and (password == passwords)):
    print(Panel.fit(f"[b]Welcome back {username}, System is updating ...[/]", title = "Welcome", title_align = "left", border_style = "bold green", box = box.SQUARE))
    
    with Progress() as progress:

        task1 = progress.add_task("[red]Downloading...", total=1000)
        task2 = progress.add_task("[green]Processing...", total=1000)
        task3 = progress.add_task("[blue]Uploading...", total=1000)

        while not progress.finished:
            progress.update(task1, advance=6)
            progress.update(task2, advance=4)
            progress.update(task3, advance=5)
            time.sleep(0.02)
    
    print(layout)
    
    if (weight_target == "Bulk"):
        from Meal_planner import Bulk
        Bulk()
else:
    print(Panel("Username or Password does not match the database", border_style = "bold red", box = box.SQUARE))
