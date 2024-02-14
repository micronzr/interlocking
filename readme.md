# Model railroad interlocking
using spdt switches and a raspberry pi pico to Control points and signals to replicate the flavour of mechanical interlocking levers

because it's a model i can't be arsed figuring out a way to lock the levers, as such if the frame goes into an invalid state it will light a fault and stop responding until the fault is fixed by reverting to the previous state, or the levers are all returned to the home position.

switching to another valid state will not resolve the issue, preventing improper signalling and de-railment/crashes

# setup

all awitch and Control elements need to be created, and linked together as either requires or blocked-by

eg, inner signal switch requires point switch, but is blocked by the outer signal switch.

so if a route is configured, you have to signal the trains to stop, then you can change the points and signal the new route

# input

spdt switches represent the levers. these may have to be fed into the pi pico via a shift register to get enough pins. after which the process is.

loop through the switches
check if there's a change to each switch
if there is, check if "requires" is satisfied
check if "blocked by" is clear.
change the state of the switch, and operate the point/signal.. if any.
if there's a problem, flag the error state

# output

likely to be a shift register and a buffer.
after looping through the switches and reading the state and setting the Control elements.
feed the results out to a shift register, and toggle the buffer to read the input, and pulse out to the controls.

hoping to find controls with relays that take seperate on/off left/right momentary inputs

# error state
deny all inputs exept the previous state and home state.
ideally only the previous state would be valid, but humans forget and it's inly a model. so, all switches home is also valid