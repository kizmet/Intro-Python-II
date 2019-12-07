from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    def description(self):
        pass

    # Hint: the name should be one word for ease in parsing later.
    def getName(self):
        print("Item: \n{}".format(self.name))

    def getDescription(self):
        description = textwrap.fill(self.description, width=50)
        print("{}: \n{}".format(self.name, description))


class Flashlight(Item):
    name = "Flashlight"
    description = "500, 250, or 125 lumens of light"


class Multitool(Item):
    name = "Multitool"
    description = "Multitool", "9-in-1 multi-tool"


class Saw(Item):
    name = "Saw"
    description = "Compact, lightweight design is easy to pack"


class Knife(Item):
    name = "Knife"
    description = "Comes with 4 interchangeable blades"


class Gloves(Item):
    name = "Gloves"
    description = "Warm and cozy gloves won't harm the gold"


class Shovel(Item):
    name = "Shovel"
    description = "Folding and Mini Shovels for your earth-moving needs."


class Water(Item):
    name = "Water"
    description = "12 oz of cold spring water"


if __name__ == "__main__":
    items = {Flashlight()}
    for item in items:
        print(item.getName())

# * Create a file called `item.py` and add an `Item` class in there.

#   * The item should have `name` and `description` attributes.

#      * Hint: the name should be one word for ease in parsing later.

#   * This will be the _base class_ for specialized item types to be declared
#     later.

# * Add the ability to add items to rooms.

#   * The `Room` class should be extended with a `list` that holds the `Item`s
#     that are currently in that room.

#   * Add functionality to the main loop that prints out all the items that are
#     visible to the player when they are in that room.

# * Add capability to add `Item`s to the player's inventory. The inventory can
#   also be a `list` of items "in" the player, similar to how `Item`s can be in a
#   `Room`.
