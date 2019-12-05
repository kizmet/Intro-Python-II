class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        #Hint: the name should be one word for ease in parsing later.


if __name__ == '__main__':
    main()

item = {
    'flashlight':
    Item(
        "Flashlight",
        "50,000 hour LED flashlight system, you’ll be able to depend on a variable torch setting that can produce 500, 250, or 125 lumens of light"
    ),
    'multitool':
    Item("Multitool", "9-in-1 multi-tool"),
    'saw':
    Item("Saw", "Compact, lightweight design is easy to pack"),
    'knife':
    Item("Knife", "Comes with 4 interchangeable blades"),
    'gloves':
    Item("Gloves", "Comes with 4 interchangeable blades"),
    'shovel':
    Item("Shovel", "Folding and Mini Shovels for your earth-moving needs."),
    'water':
    Item("Water", "12 oz of cold spring water"),
    'kit':
    Item("Kit", "Includes food, water, portable stove, first-aid and more"),
    'rope':
    Item("Rope", "20 foot nylon rope"),
    'matches':
    Item("Matches", "Standard issue safety matches"),
    'tissues':
    Item("Tissues", "Having a bad day? Here's some tissues."),
}

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