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
        options = [bit.front_clear(), bit.left_clear(), bit.right_clear()]
        mult = 0
        for option in options:
            if option: mult += 1
        
        if mult == 0: turn_around(bit)
        if mult == 1:
            follow_path(bit, options)
        if mult == 2:
            decision = int((random.random() * 2) + 1)
            if not options[0]:
                if decision == 1: path_left(bit)
                else: path_right(bit)
            if not options[1]:
                if decision == 1: bit.move()
                else: path_right(bit)
            if not options[2]:
                if decision == 1: bit.move()
                else: path_left(bit)
        if mult == 3:
            decision = int((random.random() * 3) + 1)
            if decision == 1: bit.move()
            if decision == 2: path_left(bit)
            if decision == 3: path_right(bit)
    
    print("You Survived!")   
        
def turn_around(bit):
    bit.left()
    bit.left()
    
def follow_path(bit, options):
    if options[0]: bit.move()
    if options[1]: path_left(bit)
    if options[2]: path_right(bit)
        
def path_left(bit):
    bit.left()
    bit.move()
    
def path_right(bit):
    bit.right()
    bit.move()
    
    
if __name__ == '__main__':
    maze_run(Bit.new_bit)