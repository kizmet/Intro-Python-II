# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def playermove(self, movesto):
        try:
            newroom = getattr(self.current_room, movesto)
            # newroom = self.current_room.movesto
            print('Now in {}'.format(newroom.name))
            newroom.getDescription()
            self.current_room = newroom
        except AttributeError:
            print("Cant move that way in the room {}".format(
                self.current_room.name))


if __name__ == '__main__':
    bryant = Player('bryant', 'outside')