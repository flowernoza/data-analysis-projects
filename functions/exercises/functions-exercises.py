# Part 1 A -- Make a Line
def make_line(size):
   line = ""
   for i in range(size):
      line += "#"
   return line

print(make_line(5))


# Part 1 B -- Make a Square
# create a function using your make_line function to code a square
def make_square(size):
    square = ''
    for i in range(size):
        square += make_line(size)
        if i < size - 1:
            square += '\n'  # Add newline except after the last line
    return square

print(make_square(5))


# Part 1 C -- Make a Rectangle
def make_rectangle(width, height):
   rectangle = ""
   for i in range(height):
      rectangle += make_line(width)
      if i < height - 1:
         rectangle += "\n"
   return rectangle

print(make_rectangle(5, 3))


# Part 2 A -- Make a Stairs
def make_stairs(height):
    stairs = ''
    for i in range(1, height + 1):
        stairs += '#' * i
        if i < height:
            stairs += '\n'  # Add newline except after the last row
    return stairs

print(make_stairs(6))


# Part 2 B -- Make Space-Line 
def make_space_line(space_count, hash_count):
    return ' ' * space_count + '#' * hash_count

print(make_space_line(3, 2))


# Part 2 C -- Make Isosceles Triangle
def make_isosceles(height):
    triangle = ''
    for i in range(height):
        spaces = height - i - 1
        hashes = 2 * i + 1
        triangle += make_space_line(spaces, hashes)
        if i < height - 1:
            triangle += '\n'
    return triangle

print(make_isosceles(5))


# Part 3 -- Make a Diamond

def make_diamond(height):
    diamond = ''
    
    # Top half
    for i in range(height):
        spaces = height - i - 1
        hashes = 2 * i + 1
        diamond += make_space_line(spaces, hashes)
        diamond += '\n'
    
    # Bottom half
    for i in range(height - 2, -1, -1):
        spaces = height - i - 1
        hashes = 2 * i + 1
        diamond += make_space_line(spaces, hashes)
        if i != 0:
            diamond += '\n'
    
    return diamond

print(make_diamond(10))




