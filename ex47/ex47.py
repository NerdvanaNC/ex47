class Room(object):
  def __init__(self, name, desc):
    self.name = name
    self.desc = desc
    self.paths = {}
  
  def go(self, direction):
    return self.paths.get(direction, "Invalid Direction Passed")
    # The second argument in dict.get() is already None
    # by default; idk what purpose this serves?

  def add_paths(self, paths):
    self.paths.update(paths)