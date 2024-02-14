# imports

class InputControls:
  def __init__(self,name):
    self.raw = 0
    self.hwstate = 0
    self.name = name
    self.values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0]

  def __str__(self):
    return f"({self.raw})"
  def setvals(self,reading):
    self.raw = reading
    self.values[1] = int((1 & self.raw) / 1)
    self.values[2] = int((2 & self.raw) / 2)
    self.values[3] = int((4 & self.raw) / 4)
    self.values[4] = int((8 & self.raw) / 8)
    self.values[5] = int((16 & self.raw) / 16)
    self.values[6] = int((32 & self.raw) / 32)
    self.values[7] = int((64 & self.raw) / 64)
    self.values[8] = int((128 & self.raw) / 128)
    self.values[9] = int((256 & self.raw) / 256)
    self.values[10] = int((512 & self.raw) / 512)
    self.values[11] = int((1024 & self.raw) / 1024)
    self.values[12] = int((2048 & self.raw) / 2048)
    self.values[13] = int((4096 & self.raw) / 4096)
    self.values[14] = int((8192 & self.raw) / 8192)
    self.values[15] = int((16384 & self.raw) / 16384)
    self.values[16] = int((32768 & self.raw) / 32768)
  def readhw(self):
    self.hwstate = int(input("reading"))
    self.setvals(self.hwstate)
class OutputControls:
  def __init__(self):
    self.raw = 0
    self.hwstate = 0
    self.name = name
    self.values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0]

  def setvals(self,reading):
    #modify to be outputs
    self.raw = reading
    self.values[1] = int((1 & self.raw) / 1)
    self.values[2] = int((2 & self.raw) / 2)
    self.values[3] = int((4 & self.raw) / 4)
    self.values[4] = int((8 & self.raw) / 8)
    self.values[5] = int((16 & self.raw) / 16)
    self.values[6] = int((32 & self.raw) / 32)
    self.values[7] = int((64 & self.raw) / 64)
    self.values[8] = int((128 & self.raw) / 128)
    self.values[9] = int((256 & self.raw) / 256)
    self.values[10] = int((512 & self.raw) / 512)
    self.values[11] = int((1024 & self.raw) / 1024)
    self.values[12] = int((2048 & self.raw) / 2048)
    self.values[13] = int((4096 & self.raw) / 4096)
    self.values[14] = int((8192 & self.raw) / 8192)
    self.values[15] = int((16384 & self.raw) / 16384)
    self.values[16] = int((32768 & self.raw) / 32768)

  def writehw(self):
    print(self.raw)
class Lever:
  def __init__(self,id):
    self.id = id
    self.currentposition = "off"
    self.lastposition = "off"
    self.changedposition = False
    self.required = []
    self.blocked = []
    self.control = 0
    self.controlmove = False
    self.error = False

  def addrequired(self,requires):
    self.required.append(requires)
  def addblocked(self,blockedby):
    self.blocked.append(blockedby)

  def setposition(self,pos):
    self.currentposition = pos
    if self.currentposition == self.lastposition:
      #didn't move, clear flags and do nothing
      self.error = False
      self.controlmove = False
    else:
      #lever moved
      self.changedposition = True
      self.error = False
      for require in self.required:
        if require.currentposition == "on":
          #required switch on
          #normal operation
          self.a = 1
        else:
          #required switch off
          #error condition
          self.a = 1
      for block in self.blocked:
        if block.currentposition == "off":
          # blocked switch off
          # normal operation
          self.a = 1
        else:
          #blocking switch on
          #error condition
          self.a = 1
      #check error
      if self.error == True:
        #if error do nothing
        self.a = 1
      else:
        #if no error update last position
        self.lastposition = self.currentposition
        self.controlmove = True
class Control:
  def __init__(self,id):
    self.desiredstate = 0
    self.id = id

  def setstate(self,setstate):
    self.desiredstate = setstate
class Frame:
  def __init__(self):
    self.levers = []
    self.controls = []
    #self.inputs
    #self.outputs
    self.errorlever = 0

  def addlever(self,lever):
    self.levers.append(lever)
  def addcontrol(self,control):
    self.controls.append(control)

  def check(self):
    self.inputs.readhw()
    for lever in self.levers:
      if self.errorlever == 0
        a = 1
        #read lever id
        #check input control. self.inputs.values[leverid]
        #try to set lever
        #if no error
          #loop self.controls
            #if control.id = lever.id
              #toggle control
      else:
      a = 1
        #if errorlever == lever.id
        #try to set lever
        #loop self.controls
          #if control.id = lever.id
            #toggle control


#setup

#inputs
i1 = InputControls("dunedin")

#outputs

o1 = OutputControls()

#controls
c1 = Control(1)
c2 = Control(2)
c3 = Control(3)
c4 = Control(4)
c5 = Control(5)
c6 = Control(6)
c7 = Control(7)
c8 = Control(8)

#switches
l1 = Lever(1)
l2 = Lever(2)
l3 = Lever(3)
l4 = Lever(4)

#frames

f1 = Frame()

#interlinking

l1.addrequired(l2)
l1.addblocked(l3)

#add controls to levers
l1.control = 1

#add to frame
f1.inputs = i1
f1.outputs = o1
f1.addlever(l1)
f1.addcontrol(c1)

#loop
while True:
  f1.check()
