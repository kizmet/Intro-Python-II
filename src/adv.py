from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':
    Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    'foyer':
    Room(
        "Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),
    'overlook':
    Room(
        "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),
    'narrow':
    Room(
        "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),
    'treasure':
    Room(
        "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

moves = ['n', 's', 'e', 'w']
movesto = ['n_to', 's_to', 'e_to', 'w_to']
movesdict = dict(zip(moves, movesto))
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
startingroom = room['outside']
player = Player('bryant', startingroom)
print("Welcome to the game {}. Read carefully:".format(player.name))
player.current_room.legalMoves()
print('To quit the game enter Q')
player.current_room.getName()
player.current_room.getDescription()

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    move = input("Move:")
    if move == 'Q':
        break
    elif move.isdigit():
        print('Enter n, e, s, or w!')
    elif not move in moves:
        print('Enter n, e, s, or w!')
    else:
        movesto = movesdict[move]
        player.playermove(movesto)

print('Goodbye')
