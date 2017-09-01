"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Austin Strozier.
"""
########################################################################
# Done: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
import rosegraphics as rg
window = rg.TurtleWindow


boy = rg.SimpleTurtle('turtle')
bill = rg.SimpleTurtle('turtle')
bill.speed = 20
boy.speed = 10
boy.pen = rg.Pen('midnight blue', 3)
bill.pen = rg.Pen('midnight blue', 3)
size = 288

for d in range(10):
    boy.draw_square(size)
    bill.draw_square(size)
    bill.pen_up
    boy. pen_up
    bill.right(45)
    bill.forward(12)
    bill.left(45)
    boy.left(45)
    boy.forward(50)
    boy.right(45)
    bill.pen_down
    boy.pen_down
    size = size-10
