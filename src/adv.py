from room import Room
from player import Player
from items import Items

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons",
                    [],), 

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north, east and west.""",[],),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[],),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",[],),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",[],),

    'library': Room("Library", """Look out for the ghost and things that lurk behind 
books. West to the foyer, East to the kitchen, North to the transporter room""",[],),

    'kitchen': Room("Kitchen", """You are in the kitchen. Grab as many weapons as you 
can, you're gonna need them! East to the foyer, South to the Transport Room.""", [],),

    'transport': Room("Transport Room", """You've made it!!! This room will 
transport you directly to the Treasure Room! Unless you want to go north back into the 
kitchen.""", [],),

    'garden': Room("Beautiful Garden", """Lovely plants, animals and smells. Be Careful 
though...the plants and animals can get angry and change into monsters! North to the 
Narrow Passage.""", [],),

    'secret_chamber': Room("Secret Chamber Room", """WOW!! Look at all the treasure! I guess 
previous adventurers Never found this place! Collect ALL that you can carry! You've won!""", [],)
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']

room['foyer'].n_to = room['overlook']
room['overlook'].s_to = room['foyer']

room['foyer'].w_to = room['library']
room['library'].e_to = room['foyer']

room['library'].w_to = room['kitchen']
room['kitchen'].e_to = room['library']

room['transport'].n_to = room['kitchen']
room['kitchen'].s_to = room['transport']

room['transport'].e_to = room['treasure']
room['transport'].s_to = room['treasure']
room['transport'].w_to = room['treasure']

room['foyer'].e_to = room['narrow']
room['narrow'].w_to = room['foyer']

room['narrow'].s_to = room['garden']
room['garden'].n_to = room['narrow']

room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room['treasure'].e_to = room['secret_chamber']
room['secret_chamber'].w_to = room['treasure']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player(room['outside'], 'Tiffany', )

def set_direction(player, direction):
    place = direction + '_to'
    if hasattr(player.location, place):
        player.location = getattr(player.location, place)
    else:
        print("\n === You can't go that way!! === ")

# Write a loop that:
#
while True:
    print(f"\nHere is your current player: {player1}\n")
    direction = input("\nWhich direction would you like to go? \nNorth, South, East or West: (n, s, e, w) or 'q' to quit:  ").strip().lower().split()

    choices = ['n', 's', 'e', 'w']

    if direction[0] in choices:
        set_direction(player1, direction[0])
    elif direction[0] == 'q':
        break
    else:
        print(f'Sorry, that direction is not allowed.')


    

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.