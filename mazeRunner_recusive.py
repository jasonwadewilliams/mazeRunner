from guibit import Bit

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
        # Add your code here ...
        look_around(bit)
    print("You Survived!")
    
def look_around(bit):
    if bit.front_clear(): 
        if proceed(bit): return True
    if bit.left_clear():
        bit.left()
        if proceed(bit): return True
        bit.right()
    if bit.right_clear():
        bit.right()
        if proceed(bit): return True
        bit.left()
    return False
    
def proceed(bit):
    bit.paint("green")
    bit.move()
    if bit.is_red(): return True
    if look_around(bit): return True
    bit.erase()
    bit.move_back()
    return False
    
if __name__ == '__main__':
    maze_run(Bit.new_bit)