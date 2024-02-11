# imports

class InputControls:
  def __init__(self):
    self.raw = 0
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

class Lever:
  def __init__(self):
    self.currentposition = "off"
    self.lastposition = "off"
    self.changedposition = False
    self.required = []
    self.blocked = []
    self.control = 0

  def addrequired(self,requires):
    self.required.append(requires)
  def addblocked(self,blockedby):
    self.blocked.append(blockedby)



p1 = InputControls()

print(p1)

# switch class

# functions
#init
 # clear required-on and required off and blocked and linked signal/point
 
# set linked signal/point
# get linked signal/point
 
#set position
  #read pin
  #check last position
  #set didchange
  #current pos to last pos
   #if set
  # while requires-set
    #check set
    # if set
    # position set
    # else
      # position error
      # while requires-clear
    #check set
    # if set
    # position error
    # else
      # position set
   #while blocked 
     #IF Set
     #position error
    #else
    # position set
    #else (not set)
    # position unset
    
#didchange
    
#set pin    
  # gpio pin  
    
    
#set requires
  #add switch
#set blocked by
  #add switch
#get position
  #return position

#-------- end of class

# class point
# set point position

#------- end of class

# class signal
#set signal position
#----- end of class


# create switches
# create points
# create signals

#assign points to switches
#assign signals to switches
#switch#.set-requires
#switch#.set-blocked




# frame list of switches



#error=0

# while true
#while item in frame
#if error=0    (only do until first error)
#item.setposition()
#if item.didchange.
#then
#item.getpoint().setposition(item.getposition)
#if item.getposition=error 
  #then error =1 

    #while error = 1
    #error= 0
     #while item in frame
     # item.setposition
     # if  item.getposition = error 
      # then error = 1


  