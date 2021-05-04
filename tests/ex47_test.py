## Please run pytest using "python3 -m pytest" ;—;
## Refer: https://docs.pytest.org/en/6.2.x/usage.html#calling-pytest-through-python-m-pytest

from ex47.ex47 import Room

# We're practicing writing tests
# so the actual "module" is very barebones
# but these tests will try to be a bit more
# comprehensive. This will set up the foundations
# for developing "tests first"

def test_Room():
  gold = Room("GoldRoom", """This is the gold room.
  I don't know how to indent these multiline strings.""")
  assert gold.name == "GoldRoom"
  assert gold.paths == {}

def test_room_paths():
  center = Room("Center", "This is the central room.")
  north = Room("North", "This is the north room. You entered from the Center room.")
  south = Room("South", "This is the south room. You entered from the Center room.")

  center.add_paths({"north": north, "south": south})
  assert center.go("north") == north
  assert center.go("south") == south

def test_map():
  start = Room("Start", "You can go west or down a hole.")
  west = Room("Trees", "There's trees here, you can go east.")
  down = Room("Dungeon", "It's dark down here; you can only go back up.")

  start.add_paths({"west": west, "down": down})
  west.add_paths({"east": start})
  down.add_paths({"up": start})

  assert start.go("west") == west
  assert start.go("west").go("east") == start
  assert start.go("down") == down
  assert start.go("down").go("pu") == start