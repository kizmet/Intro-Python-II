# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def getName(self):
        print("Right now you are in the room: \n{}".format(self.name))

    def getDescription(self):
        description = textwrap.fill(self.description, width=50)
        print("Hint: \n{}".format(description))

    def getItems(self):
        if self.items:
            print("Items in room:")
            for item in self.items:
                print("{}".format(item.name))

    def legalMoves(self):
        print(
            "The legal room moves are: \n[n] North  [e] East  [s] South [w] West\nTo show a room's items enter [ri] \nTo edit your items enter: [items]"
        )

    def move(self, movesto):
        move = movesto
        return move.roomkey()

    def roomkey(self):
        return self.name.lower()


if __name__ == "__main__":
    foyer = Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    )
    foyer.getName()
    foyer.getDescription()
    foyer.roomkey()
