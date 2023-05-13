import json

from rich import print
from rich import box
from rich.text import Text
from rich.align import Align
from rich.panel import Panel
from rich.layout import Layout 
from rich.table import Table

# Load data from JSON file
with open("meals.json", "r") as f:
    data = json.load(f)

# Print bulking meals
print(Panel.fit("Bulking Meals", border_style = "bold red", box = box.SQUARE))
bulking_meals = data["sections"]["bulk"]["meals"]
for meal in bulking_meals:
    print(Panel.fit(f"{meal['name']}\n{meal['description']}\n"))

# Print cutting meals
print(Panel.fit("Cutting Meals", border_style = "bold blue", box = box.SQUARE))
cutting_meals = data["sections"]["cut"]["meals"]
for meal in cutting_meals:
    print(Panel.fit(f"{meal['name']}\n{meal['description']}\n"))