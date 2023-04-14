from guibit import Bit
import random

# Available colors:=====================================================
# red
# green
# blue
# Available functions: =================================================
# front_clear() - checks to see if the space in front of you is clear
# left_clear()  - checks to see if the space to the left of you is clear
# right_clear() - checks to see if the space to the right of you is clear
# left()  - turn to the left
# right() - turn to the right
# erase() - clear the current square
# paint() - paint the current square("red")
# get_color() - get the color of the current square
# is_blue()  - return True if the current square is blue
# is_green() - return True if the current square is green
# is_red()   - return True if the current square is red
# is_empty() - return True if the current square is empty

@Bit.maze_runner(10, 10, 25)
def maze_run(bit):
    while not bit.is_red():
        is_front_clear = False
        is_left_clear = False
        is_right_clear = False
        if bit.front_clear() == True:
            is_front_clear = True
        if bit.left_clear() == True:
            is_left_clear = True
        if bit.right_clear() == True:
            is_right_clear = True
            
        # Now we know all our open options from our current position
        # Randomly select a path and follow it.
        
        # All paths are open
        if is_front_clear and is_right_clear and is_left_clear:
            # This gives me a random decimal between 0 and 1.  I multiply 
            # 3 and add 1 to get random number between 1 and 3.
            decision = (random.random() * 3) + 1
            # This will round to nearest integer
            decision = int(decision)
            
            if decision == 1:
                bit.move()
            if decision == 2:
                bit.right()
                bit.move()
            if decision == 3:
                bit.left()
                bit.move()
        
        # Front and left are open
        if is_front_clear and is_left_clear and not is_right_clear:
            decision = int((random.random() * 2) + 1)
            
            if decision == 1:
                bit.move()
            if decision == 2:
                bit.left()
                bit.move()
                
        # Front and right are open
        if is_front_clear and is_right_clear and not is_left_clear:
            decision = int((random.random() * 2) + 1)
            
            if decision == 1:
                bit.move()
            if decision == 2:
                bit.right()
                bit.move()
                
        # Left and right are open
        if is_left_clear and is_right_clear and not is_front_clear:
            decision = int((random.random() * 2) + 1)
            
            if decision == 1:
                bit.left()
                bit.move()
            if decision == 2:
                bit.right()
                bit.move()
                
        # Only left is open
        if is_left_clear and not is_right_clear and not is_front_clear:
            bit.left()
            bit.move()
            
        # Only right is open
        if is_right_clear and not is_left_clear and not is_front_clear:
            bit.right()
            bit.move()
            
        # Only front is open
        if is_front_clear and not is_right_clear and not is_left_clear:
            bit.move()
            
        # All paths blocked.  turn around.
        if not is_left_clear and not is_right_clear and not is_front_clear:
            bit.left()
            bit.left()
        
    print("You Survived!")
    
    
if __name__ == '__main__':
    maze_run(Bit.new_bit)