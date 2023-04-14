# mazeRunner

These are a few methods I built to effectively solve the maze using different techniques.

# Random
This one can be a little frustrating to watch but is effective none the less as the bit navigates the maze
and whenever it is presented with a decision it makes a choice randomly instead of using logic.  It will 
eventually find a path but is not guarenteed to be the best path.

# RandomCompressed
This is the same random method but using a few python techniques to reduce the amount of code used and 
improve human readability by abstracting into functions.

# Wall
This is perhaps the simplest method only requiring 8 lines of code.  It follows the right wall and will 
take the right path whenever it can.  This will lead it to the end in a simply connected maze (meaning 
there are no loops, which ours do not have).  It is a very effective way to solve a maze and is much
faster than random.

# Recursive
This method will recurse through the maze like a tree.  It is called recursive because one function will 
repeat code by calling another instance of itself instead of using a loop.  Each time the bit is faced with
a decision it will fork a branch and start going down one path.  if it ever hits a dead end it can return
false and will return to the point where it had a decision to make and can then follow the other branch.  
It is a little bit hard to wrap your head around but is a very effective way to guarantee every possible
route will be tried if necessary.
