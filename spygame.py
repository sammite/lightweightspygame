import random
import os
from dataclasses import dataclass


@dataclass(frozen=True)
class TextColor:
    GREEN: str = "\033[92m"
    RED: str = "\033[91m"
    YELLOW: str = "\033[93m"
    BLUE: str = "\033[94m"
    MAGENTA: str = "\033[95m"
    CYAN: str = "\033[96m"
    WHITE: str = "\033[97m"
    BOLD: str = "\033[1m"
    UNDERLINE: str = "\033[4m"
    RESET: str = "\033[0m"

# Instance to use for dot access
COLOR = TextColor()

def color_print(text, color=COLOR.GREEN):
    print(f"{color}{text}{COLOR.RESET}")

places_dict = {
    "City Places!": [
        "Coffee shop",
        "Library",
        "Train station",
        "Museum",
        "Airport",
        "Farmer's market",
        "Skyscraper rooftop",
        "Street food stall"
    ],
    "Luxury Vacations!": [
        "Private island escape",
        "Luxury yacht cruise",
        "5-star beach resort",
        "Ski chalet in the Alps",
        "Gourmet food and wine tour",
        "Luxury African safari",
        "Overwater bungalow retreat",
        "Designer shopping trip in a world capital",
        "Wellness spa in the Swiss mountains"
    ],
    "Disney Locations!": [
        "Cinderella Castle (Magic Kingdom)",
        "Spaceship Earth (EPCOT)",
        "Galaxy's Edge (Hollywood Studios)",
        "Pandora – The World of Avatar (Animal Kingdom)",
        "Main Street, U.S.A. (Magic Kingdom)",
        "World Showcase – Mexico Pavilion (EPCOT)",
        "Toy Story Land (Hollywood Studios)",
        "Expedition Everest (Animal Kingdom)"
    ],
    "Restaurant Locations!": [
        "McDonald's",
        "Chipotle Mexican Grill",
        "Chick-fil-A",
        "Olive Garden",
        "Buffalo Wild Wings",
        "The Cheesecake Factory",
        "Texas Roadhouse",
        "Outback Steakhouse"
    ],
    "Fantasy Worlds!": [
        "Middle-earth (The Lord of the Rings)",
        "Arendelle (Frozen)",
        "Narnia (The Chronicles of Narnia)",
        "Hogwarts (Harry Potter)",
        "The Shire (The Lord of the Rings)",
        "The Wizarding World (Harry Potter theme parks)",
        "The Land of Oz (The Wizard of Oz)"
    ]


}


def get_random_city_place():


    place = random.choice(list(places_dict.keys()))

    places = places_dict[place]
    return random.choice(places), place


def print_spy_banner():
    banner = '''
 / ___|___   ___ | | / ___| _ __  _   _   / ___| __ _ _ __ ___   ___ 
| |   / _ \ / _ \| | \___ \| '_ \| | | | | |  _ / _` | '_ ` _ \ / _ \\
| |__| (_) | (_) | |  ___) | |_) | |_| | | |_| | (_| | | | | | |  __/
 \____\___/ \___/|_| |____/| .__/ \__, |  \____|\__,_|_| |_| |_|\___|
                           |_|    |___/                              
'''
    COLOR = "\033[96m"  # Cyan
    RESET = "\033[0m"
    print(f"{COLOR}{banner}{RESET}")


rando_place = get_random_city_place()


def spy_game(location, num_players, theme):
    roles = [location] * num_players
    spy_index = random.randint(0, num_players - 1)
    roles[spy_index] = "You are the spy"

    color_print("Pass the device around. Press Enter when you're ready for each player's role.", COLOR.RED)
    for i in range(num_players):
        print_spy_banner()
        color_print(f"\nPlayer {i+1}, press Enter to see your role...", COLOR.BLUE)
        input("> ")
        color_print(roles[i])
        color_print(f"The location theme is {theme}!", COLOR.MAGENTA)
        color_print("Press Enter to hide your role and pass to the next player.", COLOR.BLUE)
        input("> ")
        print("\n" + "-"*40)
        os.system("clear")



os.system("clear")
location, theme = get_random_city_place()
spy_game(location, 4, theme)