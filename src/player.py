# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def playermove(self, movesto):
        try:
            newroom = getattr(self.current_room, movesto)
            print("Now in {}".format(newroom.name))
            newroom.getDescription()
            self.current_room = newroom
        except AttributeError:
            print("Cant move that way in the room {}".format(self.current_room.name))

    def additem(self, item):
        exists = item.name in [item.name for item in self.current_room.items]
        if exists:
            self.items.append(item)
            self.getItems()
        else:
            print("Item not in this room!")

    def delitem(self, item):
        exists = item.name in [item.name for item in self.items]
        if exists:
            self.items.remove(item)
            self.getItems()
        else:
            print("You dont have this item!")

    def getItems(self):
        print("My items:")
        if self.items:
            for item in self.items:
                print("{}".format(item.name))

    def __repr__(self):
        return f"{self.name}, {self.current_room.name},{self.items}"


if __name__ == "__main__":
    bryant = Player("bryant", "outside")
