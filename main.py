# THIS V1.7 ADDS ROLLING SCRAMBLED TEXT TO THE CRAWL BEFORE THE GREEN TEXT SCREEN

import enum
import os
# Force the environment to support color before initializing colorama
os.environ['TERM'] = 'xterm-256color'


import random
import string
import sys
import time
import textwrap  # Added for word wrapping
import shutil    # Added for terminal size detection
from colorama import Fore, Style, init

# 'wrap=True' ensures Colorama intercepts the sys.stdout calls 
# 'convert=True' forces it to process the ANSI codes on Mac/Windows
init(autoreset=True)
print(Fore.GREEN + "DIAGNOSTIC: If this is not green, the terminal is blocking ANSI." + Style.RESET_ALL)

ambience = ["tropical glamour ", "luxurious decor ", "nostalgic ambience ",
            "tasteful art ", "retro furnishings ", "exotic fusion ", "velvet textures ",
            "mid-twentieth mix ", "decorative pastiche ", "muted kitsch "]

nostalgia = ["feels warm and inviting, and smells like clove", "reminds you of your childhood",
             "just shows you what money can buy", "vibes like an old Hollywood set",
             "strikes a gentle balance between an art gallery and a dive bar",
             "looks like an airport terminal with disco lighting",
             "just shows you what privilege can hide", "reminds you of a vintage postcard", 
             "strikes a tense balance between an old-fashioned casino and a safehouse",
             "looks like a museum archive with rattan chairs and neon accents", 
             "feels lush and extravagant", "reminds you of a faded hologram", 
             "strikes a sublime balance between an Egyptian temple and a Caribbean speakeasy",
             "strikes a jarring balance between an alien cantina and a smokey jazz joint"]

cocktail = ["Old Fashioned with a twist", "Bourbon, neat",
            "Johnny Walker double", "Bloody Mary with extra Tabasco",
            "Dirty Martini or two", "Sangrita with a tequila chaser",
            "tall Caipirinha", "Vodka on ice", "draft beer and a rum shot",
            "Moscow Mule", "Mojito with extra lime", "Crown and Coke",
            "Side car with a small pour of Ruinart", "Pisco sour",
            "Blue Lagoon", "Veuve Clicquot", "Rusty Nail and Ginger",
            "Sex on the Beach", "Mezcal Negroni"]

intoxicated = ["a little tipsy", "not hammered but getting there", 
               "definitely under the influence", "a little woozy",
               "slightly intoxicated", "a little bit buzzed",
               "slightly altered", "a bit disoriented", 
               "pleasantly toasted", "mildly impaired", "slightly confused",
               "definitely feeling the drinks"]

event = ["The last bloody Aquarian seige of ", "Second Sagitarian War of ",
         "Third Cosmic Battle of ", "Andromedan Action on ",
         "Magentic Magellanic Blockade of ", "Zero Gravity Fornax Devastation of ",
         "Second Virgo Stellar Invasion of ", "Third Nebula Skirmish of ",
         "Cold Fusion Circinus Massacre of ", "Kinetic Cosmic Suppression of ",
         "BoRG-58 Proto Cluster Bombing of ", "Second Pegasus Sector Incursion of ",
         "Dark Matter Draco Annihilation of ", "Hyper-Spatial Phoenix Interdiction of "]

location = ["Capricorn", "Epsilon Draco", "Eridanus Alpha", "Gemini", "Calypso Minor"
            "Orion", "Ursa Major", "Volans", "LEDA 25177", "Vesperia-9",
            "Proxima Centauri B", "Aurelia Seven", "Krill-Vortex", "Kaelis-99", 
            "Zephyrus Prime", "Elysium IV"]

mission = ["broken time machine", "mission from the future",
           "intergallactic assignment", "time-jacked assassination plans",
           "need to travel back to the year 1959", "secret operation",
           "space-time situation", "clandestine time warp",
            "assignment from tomorrow", "cross-dimensional deployment",
            "liquidation protocols", "retro-jump mishap", "quantum-loop crisis", 
            "need to slip back to the year 1959", "classified undertaking", 
            "causal-loop predicament", "multi-galaxy mission", "rewind kerfuffle"]

queasy = ["could be bad", "could get ugly", "could go off the rails",
          "might get awkward", "could turn out to be a mistake", "could get hazardous",
          "could turn out awful", "could make you wish you chose another line of work",
          "could get bloody","could get lethal", "could spiral out of control",
          "might get messy", "could end poorly", "could turn out to be a disaster",
          "could get nasty", "could go sideways fast", "could get sticky",
          "could make you wish you retired last year", "could get hairy"]

tourists = ["sunburned masses", "party seekers", "sun-burned spring breakers",
            "old men Cuban men smoking Habanos and wearing guayaberas",
            "young latinas in string bikinis and flip flops",
            "thirty somethings lost between limbo and Key West",
            "cruise bound retirees en route to the Bahamas", 
            "glittering Illuminati and clubgoers",
            "forty-somethings stuck between bottle service and the flight home",
            "honeymooners stretched between the sheets and the seashore",
            "house DJs spinning beats out of wax and melting in the sun",
            "neon-clad rollerbladers carving geometry across the sidewalk",
            "young models in oversized sunglasses and designer sandals", 
            "young heiresses in crochet cover-ups and platform wedges",
            "fifty-something dads trapped between a second divorce and a sailboat lease",
            "a Canadian Biker club on spring break"]

# TYPEWRITER SIMULATOR OPTION:
# Modified from https://www.101computing.net/python-typing-text-effect/
def typewriter_simulator(message_to_print, color_code=Fore.GREEN):
    for char in message_to_print:
        # Color and character bundled into one single 'write'
        # This mirrors the logic of the radio codes.        
        sys.stdout.write(color_code + char)
        sys.stdout.flush()
        
        time.sleep(0.025)
        if char in [".", ",", "!", "?", "-"]:
            time.sleep(.5)
            
    # Clean up the color at the very end of the line
    sys.stdout.write(Style.RESET_ALL)
    sys.stdout.flush()
    print('')

# 1. Update smart_print to accept an optional color
def smart_print(message_to_print, color=Fore.GREEN):
    columns, _ = shutil.get_terminal_size(fallback=(80, 24))
    wrapped_text = textwrap.fill(
        message_to_print, 
        width=columns - 2, 
        replace_whitespace=False, 
        drop_whitespace=False
    )
    typewriter_simulator(wrapped_text, color)
    
# 2. Update print_pause (Green)
def print_pause(message_to_print, delay=0):
    smart_print(message_to_print, Fore.GREEN)
    time.sleep(delay)

# 3. Update print_gray (Gray)
def print_gray(message_to_print, delay=0):
    # Use Fore.LIGHTBLACK_EX (Colorama's version of Gray)
    smart_print(message_to_print, Fore.LIGHTBLACK_EX)
    time.sleep(delay)

# INPUT: Modified from:
# https://www.101computing.net/python-typing-text-effect/)
def input_query(response, color=Fore.GREEN):
    # 1. This loop prints the menu (A, B, C...) character by character
    for character in response:
        sys.stdout.write(color + character)
        sys.stdout.flush()
        time.sleep(0.05)
    
    # 2. This passes the 'color' code directly INTO the input prompt string.
    # This keeps the "ink" green while the user types their choice.
    # The " " adds a space.
    value = input(color + " ")
    
    # 3. Color reset to white ONLY after the user hits Enter
    sys.stdout.write(Style.RESET_ALL)
    sys.stdout.flush()
    
    return value

# RANDOM COLORS A: DEFINE COLORS
class Color(enum.Enum):
    # Standard format: \033[ + ColorCode + m
    RED = '\033[31m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'

    @classmethod
    def get_color(cls):
        return random.choice([color.value for color in cls])

# RANDOM COLORS B: PRINT RANDOM COLORED TEXT FOR CODE SCAN
def print_rndclr(message, delay=0):
    print(Color.get_color() + message)
    time.sleep(delay)

# BLINKING TEXT GRAY FOR STANDBY ALERT
def print_blink(message_to_print, delay=1):
    n = 0
    while n < 3:
        print('\033[90m' + message_to_print)
        time.sleep(.5)
        clearScreen()
        n = n + 1
        time.sleep(.5)

# PRINT YELLOW TEXT FOR VERIFICATION ALERTS
def print_verification(message_to_print, delay=1):
    print('\033[93m' + message_to_print)

# CLEAR SCREEN: Sourced from-
# https://www.101computing.net/python-typing-text-effect/)
def clearScreen():
    os.system("clear")

# PRINT SCRAMBLED TEXT
def rolling_scramble_fixed(target_text, window_size=16, speed=0.03):
    GRAY = "\033[90m"
    RESET = "\033[0m"
    
    # 1. Get terminal dimensions
    columns, rows = shutil.get_terminal_size(fallback=(80, 24))
    
    # 2. Calculate vertical offset (aiming for the middle)
    vertical_offset = rows // 2
    
    # 3. Wrap and prepare text
    wrapped_lines = textwrap.wrap(target_text, width=columns - 2)
    flat_text = "".join(wrapped_lines)
    
    # 4. Animation Loop
    for frame in range(len(flat_text) + window_size):
        display = []
        for i in range(len(flat_text)):
            if i >= frame: 
                display.append("")
            elif frame - window_size <= i < frame:
                display.append(random.choice(string.ascii_letters + string.digits))
            else: 
                display.append(flat_text[i])
        
        # Re-wrap the scrambled string
        scrambled_string = "".join(display)
        frame_to_print = textwrap.fill(scrambled_string, width=columns - 2)
        
        # Add the vertical padding: 
        # Create a string of empty lines based on the vertical_offset
        padding = "\n" * vertical_offset
        
        # Use \033[H to move cursor to top-left, then add padding
        sys.stdout.write("\033[H" + padding + GRAY + frame_to_print + RESET)
        sys.stdout.flush()
        time.sleep(speed)
        
    print() # Final newline


# INTRO SECTION
def intro():
    time_machine_radio_codes()
    clearScreen()
    print_pause("\nHello.\n", 1)
    print_pause("You are a time traveler for a future Intergalactic "
                "Government.", 1)
    print_pause("\nYou were traveling back in time to January 19, 1959.", 1)
    print_pause("Your mission is to assassinate a notable Cuban "
                "revolutionary.", 1)
    print_pause("But the time machine malfunctioned during the "
                "hyper jump.", 1)
    print_pause("And now you are stranded...", 1)
    print_pause("\nin South Beach-", 1)
    print_pause("\nMiami-", 1)
    print_pause("\n1989.", 2)
    print_pause("\nFortunately, one hotel in this time and place "
                "contains a safe house.", 2)
    print_pause("Since you don’t know which one it is, you'll have to "
                "find it.\n", 2)
    print_pause("You cross Ocean Drive and strike out "
                "for the first hotel in your sightline.", 1)

# HOTEL ENTRANCE
def hotel_bar():
    print_pause("You experience a bit of déjà vu because "
                "the " + random.choice(ambience) + "of the art deco "
                "lobby " + random.choice(nostalgia) + ".", 2)
    print_pause("-So you linger in the hotel bar, take a breather, and "
                "order a " + random.choice(cocktail)+"...", 2)
    print_pause("\nOnce 'refreshed', you return to the lobby and approach "
                "the first front desk clerk you see-\n", 2)

# FRONT DESK CLERK APPROACH
def desk_clerk_approach():
    print_pause("It's possible that you drink too much, but you're still "
                "surprised the cocktail made you feel "
                "you " + random.choice(intoxicated) + ".", 1)
    print_pause("And before you can stop yourself, you immediately "
                "assume the current clerk is also an undercover "
                "intergalactic agent.", 1)
    print_pause("And so you tell them all about "
                "your " + random.choice(mission) + ".", 1)
    print_pause("At first she looks puzzled, but...\n", 1)

# FRONT DESK CLERK: Helpful
def desk_clerk_correct():
    desk_clerk_approach()
    print_pause("Fortunately, your assumption is correct!\n", 1)
    print_pause("However, you also learn that the two of you share "
                "some history on opposing sides of "
                "the " + random.choice(event) + random.choice(location) +
                "!\n", 2)
    print_pause("This " + random.choice(queasy) + "...", 1)

# NEVERTHELESS: the clerk will help
def nevertheless():
    print_pause("\nNevertheless, duty prevails and she agrees to "
                "help you accomplish your present mission.\n", 2)

# FRONT DESK CLERK: Antagonist
def desk_clerk_wrong():
    desk_clerk_approach()
    print_pause("But then she begins to look positively fearful.")
    print_pause("And suddenly you realize-", 2)
    print_pause("This front desk clerk is not an undercover galactic "
                "agent.", 1)
    print_pause("She's just an ordinary person trying to get ahead in "
                "the hospitality trade.\n", 1)
    print_pause("-And she has absolutely no clue what you’re "
                "going on about!\n", 2)
    print_pause("In fact, she thinks you're either high or crazy and that "
                "there's a good chance that you might become violent.\n", 1)
    print_pause("She activates a headset and you hear her whisper "
                "the word 'security'.\n", 1)
    print_pause("'-No, no, don't do that!' you plead. \n", 1)

# HOTEL EXIT: SNOW BIRDS
def snow_birds():
    print_pause("Seconds later you're back outside on the sidewalk, "
                "standing amidst "
                "the teeming crowds of snow birds and "
                + random.choice(tourists) + ".\n", 2)
    print_pause("You cast your gaze the length of Ocean Drive for your next "
                "destination.\n", 1)

# HOTEL_1_TIDES_ITEM 1: Snow Globe
# (Not available until player retrieves briefcase)
def hotel1(items):
    clearScreen()
    print("\n")
    print_pause("You walk along the street and enter the lobby of "
                "The Tides Hotel.\n", 1)
    hotel_bar()
    desk_clerk_correct()
    nevertheless()
    if "briefcase" in items:
        print_pause("So, you show her the briefcase.\n", 2)
        print_pause("She authenticates it and the decryption codes it "
                    "contains.\n", 2)
        if "snowglobe" in items:
            print_pause("And since you already have the snow globe–", 1)
            print_pause("She asks if you've also identified the location "
                        "of the safe house yet?\n", 1)
            print_pause("And if so, she explains that that should be "
                        "your next stop.\n", 1)
            print_pause("And if not, then what are you waiting for?\n", 1)
            print_pause("Then a van filled with several new hotel guests "
                        "arrives at the hotel entrance.\n", 1)
            print_pause("-And so she ushers you out towards the "
                        "back exit, and you oblige.\n", 1)
        else:
            print_pause("Then she gives you what appears to be a very "
                        "delicate looking snow globe.", 2)
            print_pause("\nOf course, the first thing you do is shake it.", 1)
            print_pause("'No, no, -please don't do that!', she says, quickly "
                        "taking it back.", 1)
            print_pause("Then she wraps the snow globe in linen "
                        "and very gingerly places it in the briefcase-", 1)
            print_pause("'-For safe transport,' she explains.\n", 1)
            print_pause("-And then she ushers you back towards the exit.\n", 2)
        items.append("snowglobe")
    else:
        print_pause("She could give you a special snow globe that contains "
                    "space-time transposing comet dust...", 2)
        print_pause("-But she won't hand it over until you return with "
                    "an equally special briefcase.\n", 2)
        print_pause("'Damn', you say. 'Well, ok...'", 1)
        print_pause("-And you tell her you'll be back.\n", 2)

    snow_birds()
    visit_hotel(items)

# HOTEL_2_SHEPLEY_ITEM 2: Briefcase (Must get first, before snow globe)
def hotel2(items):
    clearScreen()
    print("\n")
    print_pause("You walk along the street and enter the lobby of "
                "The Shepley Hotel.\n", 1)
    hotel_bar()
    desk_clerk_correct()
    nevertheless()

    if "briefcase" in items:
        print_pause("She points out that you already have the briefcase with "
                    "the decryption codes.", 1)
        print_pause("And she reminds you that you still need to secure "
                    "a special snow globe.", 1)
        print_pause("Once you secure the snow globe, she tells you, then you "
                    "will be ready to make your way back to the safe "
                    "house.\n", 2)
        if "snowglobe" in items:
            print_pause("Only then, and much to the surprise of the desk "
                        "clerk, do you pull out the snow globe "
                        "and place it on the table between you.", 2)
            print_pause("She picks it up, looks it over for a minute, "
                        "and then returns it to the briefcase.", 2)
            print_pause("Since you now have have everything you need, "
                        "she congratulates you and sends you on your way.", 2)
    else:
        print_pause("Then the hotel clerk gives you a briefcase.", 1)
        print_pause("From the outer markings, you can see that it is a "
                    "vintage brown leather dispatch bag made by house of "
                    "Hermès in Paris, circa 1950.", 2)
        print_pause("Inside is a single sheet of paper with stange "
                    "markings.", 1)
        print_pause("The clerk explains you will need these codes later.", 1)
        print_pause("She then tells you that you'll also need to secure "
                    "a special snow globe.", 1)
        print_pause("And that you should use the briefcase to "
                    "transport the snow globe.\n", 2)
        items.append("briefcase")
    snow_birds()
    visit_hotel(items)

# HOTEL_3_EDISON_SAFEHOUSE
def hotel3(items):
    clearScreen()
    print("\n")
    print_pause("You walk along the street and enter the lobby of "
                "The Edison Hotel.\n", 1)
    hotel_bar()
    desk_clerk_correct()
    nevertheless()
    if "briefcase" in items:
        print_pause("So, you show the clerk the briefcase you retrieved.", 1)
        print_pause("'Good job!', she says. Then she asks if you also have "
                    "the snow globe.", 1)
        print_pause("'You need both the codes and the snow globe,' "
                    "she explains. ", 1)
        print_pause("And then you can use the worm hole to continue "
                    "travelling back in time.\n", 2)
        if "snowglobe" in items:
            print_pause("Only then do you open the briefcase and show "
                        "her the snow globe.\n", 2)
            print_pause("'Whoa!', she says, 'That's awesome!'", 1)
            print_pause("And since you have everything you need, she directs "
                        "you to the hotel’s basement where you can activate "
                        "a worm hole to make a hyper jump.\n", 2)
            ready(items)  # READY OR NOT?
        else:
            print_pause("Since you already have the briefcase, "
                        "she sends you back out to retrieve the "
                        "snow globe.\n", 2)
    else:
        print_pause("She tells you about a worm hole in "
                    "the basement that you can use to complete your "
                    "mission.", 2)
        print_pause("But you'll need to collect two special items from two "
                    "other nearby hotels to activate it.\n", 2)
        print_pause("She tells you that you need a 'Worm Hole Activation "
                    "Agent' and a 'Space-Time De-Cryption Code'.\n", 2)
        print_pause("* The Snow Globe contains a pure strain of "
                    "Andromendan comet dust cleverly disguised "
                    "as snow flakes.", 2)
        print_pause("* And the decryption codes are carried in "
                    "a galactic government issue leather briefcase.\n", 2)
        print_pause("But because both items are re-located every other day, "
                    "she doesn't know which hotel will have which item on "
                    "any given day.\n", 2)
        print_pause("And now you wish you hadn't had that cocktail.\n", 2)
        print_pause("Either way, time is of the essence-", 1)
        print_pause("And you are a highly trained professional- ", 1)
        print_pause("So, you pull yourself together and head "
                    "for the nearest exit.\n", 2)
    snow_birds()
    visit_hotel(items)

# HOTEL_4_CARLYLE: No items
def hotel4(items):
    clearScreen()
    print("\n")
    print_pause("You walk along the street and enter the lobby of "
                "The Carlyle Hotel.\n", 1)
    hotel_bar()
    desk_clerk_wrong()
    print_pause("And now you need to make a quick decision!\n", 1)
    print_pause("Do you want to try to silence her and risk causing a "
                "commotion?\n", 1)
    print_pause("-Or should you turn on your heels and run as "
                "fast as you can before security arrives and "
                "possibly detains you?\n", 2)
    fight_or_flee(items)


# VISIT HOTEL
def visit_hotel(items):
    while True:
        print_pause("\nWhere do you want to go to next? Which hotel do you "
                    "want to visit now?", 1)
        print_pause("\nEnter A, B, C, or D:\n")
        
        # Added .upper() here so 'a' becomes 'A' automatically.
        # This solves the case-sensitivity issue in one line!
        hotel = input_query("A. The Tides\n"
                            "B. The Shepley\n"
                            "C. The Edison\n"
                            "D. The Carlyle\n").upper()
        
        if hotel == 'A':
            hotel1(items)
        elif hotel == 'B':
            hotel2(items)
        elif hotel == 'C':
            hotel3(items)
        elif hotel == 'D':
            hotel4(items)
        else:
            # This only triggers if user types something completely wrong.
            print_pause("\nSorry, I don't understand.")

# FIGHT
def fight():
    print_pause("\n")
    print_pause("NOOOOOOOO!\n")
    print_pause("Before you can even throw a punch two burly security "
                "guards enter the lobby.", 1)
    print_pause("They tase you, and you drop like a ton of bricks.", 1)
    print_pause("You pass out and wake up in jail.", 1)
    print_pause("After months of explaining to mental health professionals "
                "that you are a time traveler-\n")
    print_pause("You become a ward of the state and you are "
                "institutionalized for life.\n", 1)
    print_pause("You never complete your mission, and you fill the rest "
                "of your days collecting snow globes.\n", 2)

# FLEE
def flee():
    print("\n")
    print_pause("Great choice! You turn away from the clerk and "
                "make a successful dash for the exit.\n", 2)

# STAY
def stay():
    print("\n")
    print_pause("And why not? Miami in 1989 is great!\n", 2)
    clearScreen()
    time.sleep(3)
    print_pause("You wake up the next morning on a couch in the lobby of "
                "The Viceroy with a splitting headache.\n", 2)
    print_pause("So, you freshen up in a public washroom-\n", 1)
    print_pause("Then you order a strong coffee and sit poolside "
                "watching the sun rise until the caffeine kicks in.\n", 2)
    print_pause("Afterwards, you grab a donut from the breakfast bar "
                "and exit the hotel to finally finish your mission...\n", 2)
    clearScreen()
    time.sleep(2)

# FIGHT OR FLEE
def fight_or_flee(items):
    while True:
        print_pause("What do you want to do?\n")
        print_pause("Select 'A' to fight, or 'B' to flee:\n")
        f_or_f = input_query("A. FIGHT!\n"
                             "B. FLEE!\n")
        if f_or_f == 'A':
            fight()
            coda()
            play_or_quit()
        elif f_or_f == 'B':
            flee()
            snow_birds()
            visit_hotel(items)
        elif f_or_f == 'a':
            fight()
            coda()
            play_or_quit()
        elif f_or_f == 'b':
            flee()
            snow_birds()
            visit_hotel(items)
        else:
            print("\n")
            print_pause("Sorry, I don't understand.")
            fight_or_flee(items)

# READY TO JUMP?
def ready(items):
    while True:
        print("\n")
        print_pause("ARE YOU FINALLY READY TO MAKE THE JUMP BACK "
                    "TO 1959?\n", 1)
        print("\n")
        print_pause("Select 'A' if you're ready, or 'B' if you want "
                    "to hang out in South Beach a little while longer:\n")
        ready_or_not = input_query("A. TAKE ME BACK TO 1959 SO I CAN COMPLETE "
                                   "MY MISSION!\n"
                                   "B. NO, I WANT TO STAY IN SOUTH BEACH A LITTLE LONGER "
                                   "AND PARTY LIKE IT'S 1989!\n")
        if ready_or_not == 'A':
            hyper_jump()
            coda()
            play_or_quit()
        elif ready_or_not == 'B':
            stay()
            snow_birds()
            visit_hotel(items)
        elif ready_or_not == 'a':
            hyper_jump()
            coda()
            play_or_quit()
        elif ready_or_not == 'b':
            stay()
            snow_birds()
            visit_hotel(items)
        else:
            print("\n")
            print_pause("Sorry, I don't understand.")
            ready(items)


# HYPER JUMP
def hyper_jump():
    print("\n")
    print_pause("AWESOME!\n")
    print_pause("You find the worm hole, enter the codes, "
                "and release the comet dust from the snow globe.", 1)
    print_pause("The worm hole opens and you are immediately whisked "
                "back into the past.", 1)
    clearScreen()
    time.sleep(2)
    print_pause("Five minutes later you arrive twenty years earlier at the "
                "the Hotel Libre in Havana, Cuba, on January 19, 1959. \n")
    print_pause("-Where you seek out your target and complete your "
                "mission.\n", 2)
    print_pause("Unfortunately, afterwards, you're caught, arrested, and "
                "sent to a detention camp, where you live out the rest of your "
                "days. \n", 2)

# CODA
def coda():
    print_pause("However...\n", 2)
    print_pause("Although some 66 years from now, you will die here-", 1)
    print_pause("-at 11:51 pm, on August 30, 2025...\n ", 2)
    print_pause("Not ten minutes after that-", 1)
    print_pause("You will also be born thousands of miles away in "
                "Los Angeles, California.", 1)
    print_pause("\nAnd 29 years after that, in 2054-", 1)
    print_pause("You will be a trained special agent again.", 1)
    print_pause("And once again, you will be offered a unique assignment "
                "by an intergalactic government agency-", 1)
    print_pause("-to travel 100 years back in time to assassinate a notable "
                "political figure and re-shape future history.\n", 1)
    print_pause("-Which means, 100 years from now-\n", 1)
    print_pause("Give or take...\n", 1)
    print_pause("You'll get a second chance.\n", 2)

# PLAY AGAIN
def play():
    print_pause("\n")
    print_pause("Awesome! Returning you to the beginning of your "
                "mission in-\n")
    print_pause("3\n", 1)
    print_pause("2\n", 1)
    print_pause("1\n", 1)
    print_pause("Time Machine engaged!\n")
    print_pause("\n", 2)
    clearScreen()
    print_pause("\n", 2)
    play_game()

# QUIT
def quit_game():
    clearScreen()
    print_pause("Thanks for playing Miami Time Machine!", 2)
    
    # Call the scrolling animation here
    scroll_final_logo()
    
    # Finally, terminate the program
    sys.exit()

# PLAY GAME OR QUIT
def play_or_quit():
    # 1. Get the choice while the story text is still visible
    choice = input_query("Make your choice! Select 'A' to give it another go, "
                         "or 'B' to quit:\n").upper()
    
    # 2. Validation loop (so game doesn't clear/scroll for a typo)
    if choice not in ['A', 'B']:
        print_pause("\nI didn't quite get that. Please select A or B.")
        return play_or_quit()

    # 3. The "Curtain Call" - Clear and Scroll
    clearScreen()
    scroll_final_logo()
    
    # 4. The Dynamic Finish
    if choice == 'A':
        print_gray("STAND BY FOR SPACE-TIME RE-ALIGNMENT...", 2)
        time.sleep(1)
        clearScreen()
        play_game() # Restart the loop
    
    elif choice == 'B':
        print_gray("SESSION TERMINATED. THANK YOU FOR YOUR SERVICE!", 2)
        time.sleep(1)
        sys.exit() # Clean exit

# TIME MACHINE CODES
def time_machine_radio_codes():
    clearScreen()
    time.sleep(2)
    print_blink("\n\nCODE 1 SCANNING:\n")
    print_verification("\n\nCODE 1 VERIFIED: PLEASE SUBMIT NEXT CODE")
    print_rndclr("\n\n2ir3jzso3sfxnoljdycrbjq5reyowxdqj29262ir3jzso3sfdyz \n"
                 "ovj5hp3q1jttnsxlhl4wrnaMiamib9qc2sv784wrqz7yvnsab9q \n"
                 "uw7q2pu5eofo4dc2r9rqfe7Timefk1j4ge9qfe7fhe8fwfk1j4g \n"
                 "oo9d6trotyp8adjgcnfyptn1Machineyym3kgvn5aptn1jcr57y \n"
                 "rm7ey4re83fsqfz(c)2022htyv0htl47e5byvterryogara0hnf \n", 2)
    clearScreen()
    print_blink("\n\nCODE 2 SCANNING:\n")
    print_verification("\n\nCODE 2 VERIFIED: PLEASE SIGN "
                       "INJURY LIABILITY WAIVER")
    print_rndclr("\n\nmlszeqe0ovd9lsjxmwizc5y3p1t7heo4y4mpfjxmwizc5y3p1t7 \n"
                 "w25vkd280di634du4pqc3hg1wqjvs3apdkfefpqc3hg1wqjvs3d \n"
                 "828u6lu3uvq2ep8rjuglniajchjzjqzsqzvlruglniajchjzjqf \n"
                 "payqmoyrl51yd4jcqred0rrajbplidwikebkhed0rrajbplidws \n"
                 "2kt88vmqxij8767iz91pmh1w29kpideiqixnbz91pmh1w29kpih \n", 2)
    clearScreen()
    print_blink("\n\nCODE 3 SCANNING:\n")
    print_verification("\n\nCODE 3 VERIFIED: HYPER JUMP AUTHORIZED")
    print_rndclr("\n\n03puwhf2e1f4d1oajbx1z4tc8dd7un62wk7dn7c0oc8fdd7un62w \n"
                 "511zywe8hqfl1aaz6axla462rikc70jegohrlaxla462rikc70ur \n"
                 "sjil23rhw5bc95isb9yvwexda68vur7ebmzegb9yvwexda68vuwj \n"
                 "3czoysbyltlxqq3tgkg8nlbx1zvwgu7xkcngp8nlbx1zvwgu7xkd \n"
                 "xsm2e3ap75cjskqrc3jifyhgr990taw6hdfh03jifyhgr99tafsz \n", 2)
    clearScreen()
    print_blink("\n\n\n\n\n\n\n\n\n\n\n\nSTANDBY\n", 2)
    clearScreen()
    # ... inside time_machine_radio_codes ...
    print_gray("\n\n\n01101000 01101101 01101110 01101111 00100000")
    print_gray("\n\n\n01101101 01100010\n")
    
    time.sleep(1) 
    
    # ADD THIS: Wipe the corruption before starting the animation
    # 1. Reset the stage
    clearScreen() 
    
    # 2. Define the text data
    text_to_show = (
        "bjq5reyowxdqj2jq5r9262idqj29262r3jzsj2jq5rj03puwh"
        "f2e1f4d1oaj4tc8dd7un62wk7dn7c0oc8dd7un62wk7dn03p"
        "uwhf2e1f4d1oaj4tc8dd7un62wk7dn7c0oc8dd7un62wk7dn"
    )
    
    # 3. Trigger the animation
    rolling_scramble_fixed(text_to_show)


# PLAY GAME
def play_game():
    while True:
        items = []
        intro()
        visit_hotel(items)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Miami Time Machine Scrolling Logo starts below this line:
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def scroll_final_logo():
    # ASCII Art Logo
    logo_lines = [
      r"   __       __  ______   ______   __       __  ______        ________  ______  __       __  ________        __       __   ______    ______   __    __  ______  __    __  ________ ",
        r"/  \     /  |/      | /      \ /  \     /  |/      |      /        |/      |/  \     /  |/        |      /  \     /  | /      \  /      \ /  |  /  |/      |/  \  /  |/        |",
        r"$$  \   /$$ |$$$$$$/ /$$$$$$  |$$  \   /$$ |$$$$$$/       $$$$$$$$/ $$$$$$/ $$  \   /$$ |$$$$$$$$/       $$  \   /$$ |/$$$$$$  |/$$$$$$  |$$ |  $$ |$$$$$$/ $$  \ $$ |$$$$$$$$/ ",
        r"$$$  \ /$$$ |  $$ |  $$ |__$$ |$$$  \ /$$$ |  $$ |           $$ |     $$ |  $$$  \ /$$$ |$$ |__          $$$  \ /$$$ |$$ |__$$ |$$ |  $$/ $$ |__$$ |  $$ |  $$$  \$$ |$$ |__    ",
        r"$$$$  /$$$$ |  $$ |  $$    $$ |$$$$  /$$$$ |  $$ |           $$ |     $$ |  $$$$  /$$$$ |$$    |         $$$$  /$$$$ |$$    $$ |$$ |      $$    $$ |  $$ |  $$$$  $$ |$$    |   ",
        r"$$ $$ $$/$$ |  $$ |  $$$$$$$$ |$$ $$ $$/$$ |  $$ |           $$ |     $$ |  $$ $$ $$/$$ |$$$$$/          $$ $$ $$/$$ |$$$$$$$$ |$$ |   __ $$$$$$$$ |  $$ |  $$ $$ $$ |$$$$$/    ",
        r"$$ |$$$/ $$ | _$$ |_ $$ |  $$ |$$ |$$$/ $$ | _$$ |_          $$ |    _$$ |_ $$ |$$$/ $$ |$$ |_____       $$ |$$$/ $$ |$$ |  $$ |$$ \__/  |$$ |  $$ | _$$ |_ $$ |$$$$ |$$ |_____ ",
        r"$$ | $/  $$ |/ $$   |$$ |  $$ |$$ | $/  $$ |/ $$   |         $$ |   / $$   |$$ | $/  $$ |$$       |      $$ | $/  $$ |$$ |  $$ |$$    $$/ $$ |  $$ |/ $$   |$$ | $$$ |$$       |",
        r"$$/      $$/ $$$$$$/ $$/   $$/ $$/      $$/ $$$$$$/          $$/    $$$$$$/ $$/      $$/ $$$$$$$$/       $$/      $$/ $$/   $$/  $$$$$$/  $$/   $$/ $$$$$$/ $$/   $$/ $$$$$$$$/ "
                                                                                                             
    ]

    # ANSI Colors
    red = '\033[31m'
    reset = '\033[0m'

    # Get terminal width
    term_width, _ = shutil.get_terminal_size(fallback=(80, 24))
    logo_width = len(logo_lines[0])
    
    # Sequence: Total distance is (terminal width + logo width)
    # Implemented a step of 2 to make it move a bit faster
    for shift in range(term_width, -logo_width, -2):
        # Build the frame
        frame = []
        for line in logo_lines:
            if shift > 0:
                # Logo is still entering from the right
                display_line = " " * shift + line
            else:
                # Logo is partially or fully off to the left
                display_line = line[abs(shift):]
            
            # Trim to ensure it doesn't wrap accidentally if the window is small
            # And apply the red color to each line individually
            frame.append(red + display_line[:term_width])
        
        # Draw frame
        # Use sys.stdout.write to reduce flickering compared to clearScreen()
        output = "\033[H" + "\n".join(frame) # \033[H moves cursor to top-left
        sys.stdout.write(output)
        sys.stdout.flush()
        time.sleep(0.05)

    print("\n" * 5)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Miami Time Machine Game program starts below this line:
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++å

if __name__ == "__main__":
    play_game()

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# MIAMI TIME MACHINE: (V1.6) (C) 2022, (V1.7) 2026 Terry O'Gara
# All rights reserved.
# V1.0 originally created for the Udacity Intro to Programming course.
# ADVENTURE GAME ASSIGNMENT: Submitted by 09/02/22
# Note: ipnd-reference-sheet-elevator-code.pdf oft used
# as a reference for this game framework.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
