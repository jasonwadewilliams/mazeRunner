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
        if bit.right_clear():
            bit.right()
            bit.move()
        elif bit.front_clear():
            bit.move()
        else:
            bit.left()

    print("You Survived!")  
    
if __name__ == '__main__':
    maze_run(Bit.new_bit)
