#!/usr/bin/python3
# encoding: utf-8

def parseBlock(s):
  x1, y1, x2, y2 = map(int, s.split())
  return {
    'x1': x1, 'y1': y1,
    'x2': x2, 'y2': y2,
  }


def parseHouse(s):
  x, y = map(int, s.split())
  return { 'x': x, 'y': y }
  

#    -2
# -1     1
#     2

NORTH = -2
EAST  =  1
SOUTH =  2
WEST  = -1

TURN_LEFT  = -1
TURN_RIGHT =  1


def inBlock(x, y, b):
  return b['x1'] < x < b['x2'] and b['y1'] < y < b['y2']
  

class Pathfinder():
  def __init__(self, x, y, dest_x, dest_y, blocks, max_turns, direction, _length = 0, _steps = [], _turns = []):
    for block in blocks:
      if inBlock(x, y, block):
        raise Exception("Can't place CAR to a BLOCK")
    
    if (x < 0) or (y < 0) or (x > dest_x) or (y > dest_x):
      # Negative?
      raise Exception("U r goin 2 far")
      
    self.x, self.y = x, y
    self.dest_x, self.dest_y = dest_x, dest_y
    self.blocks = blocks
    self.max_turns = max_turns
    self.direction = direction
    self.length = _length
    self.steps = _steps
    self.turns = _turns
    
  def step(self):
    if   self.direction == NORTH:
      k, l = -1,  0
    elif self.direction == EAST:
      k, l =  0,  1
    elif self.direction == SOUTH:
      k, l =  1,  0
    elif self.direction == WEST:
      k, l =  0, -1
    return Pathfinder(
      self.x + k, self.y + l,
      self.dest_x, self.dest_y,
      self.blocks,
      self.max_turns, self.direction,
      _length=self.length + 1,
      _steps=self.steps + [(self.x, self.y, self.direction)])
  
  def _turn(self, angle):
    if   (self.direction, angle) in [(EAST, TURN_LEFT), (WEST, TURN_RIGHT)]:
      new_d = NORTH
    elif (self.direction, angle) in [(SOUTH, TURN_LEFT), (NORTH, TURN_RIGHT)]:
      new_d = EAST
    elif (self.direction, angle) in [(WEST, TURN_LEFT), (EAST, TURN_RIGHT)]:
      new_d = SOUTH
    elif (self.direction, angle) in [(NORTH, TURN_LEFT), (SOUTH, TURN_RIGHT)]:
      new_d = WEST
    
    return Pathfinder(
      self.x, self.y,
      self.dest_x, self.dest_y,
      self.blocks,
      self.max_turns - 1, new_d,
      _length=self.length,
      _steps=self.steps,
      _turns=self.turns + [(self.x, self.y, angle)])
  
  def turnStep(self, angle):
    return self._turn(angle).step()
  
  def find(self):
    if self.x == self.dest_x and self.y == self.dest_y:
      return []

    else:
      pathes = []
      
      # trying to go straight 
      try:
        pf = self.step()
        pathes.append(pf.find())
      except:
        pass
      
      # trying to turn left or right
      # TODO: perhaps we should skip this if YAY the path was already found
      if self.max_turns > 0:
        for angle in [TURN_LEFT, TURN_RIGHT]:
          try:
            pf = self.turnStep(angle)
            pathes.append(pf.find())
          except:
            continue
          
      if len(pathes) == 0:
        raise Exception("No wai!")

      return min(pathes, key=lambda s: s.length)


if __name__ == "__main__":
  pf = Pathfinder(0, 0, 5, 5, [], 300, NORTH)
  print(pf.find())
  
##  infile = open("majorhouse.in")
##  outfile = open("majorhouse.out", 'w')
##  
##  n, _ = map(int, infile.readline().split())
##  
##  blocks = []
##  houses = []
##  
##  for _ in range(n):
##    line = infile.readline()
##    blocks.append(parseBlock(line))
##  
##  for line in infile.readlines():
##    houses.append(parseHouse(line))
