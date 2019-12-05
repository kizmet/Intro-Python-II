# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def getName(self):
        print('Right now you are in the room: \n{}'.format(self.name))

    def getDescription(self):
        description = textwrap.fill(self.description, width=50)
        print('Hint: \n{}'.format(description))

    def legalMoves(self):
        print(
            "The legal room moves are: \n [n] North  [e] East  [s] South [w] West"
        )

    def move(self, movesto):
        move = movesto
        return move.roomkey()

    def roomkey(self):
        return self.name.lower()


if __name__ == '__main__':
    foyer = Room(
        "Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""")
    foyer.getName()
    foyer.getDescription()
    foyer.roomkey()
