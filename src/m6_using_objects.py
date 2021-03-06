"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Tianlin Wang.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()

def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # Done: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------
    window = rg.RoseWindow(500, 300, 'm6_1')
    center_point1 = rg.Point(300, 100)
    radius = 5
    circle1 = rg.Circle(center_point1, radius)
    circle1.fill_color = 'green'
    circle1.attach_to(window)
    center_point2 = rg.Point(200,200)
    circle2 = rg.Circle(center_point2, radius)
    circle2.fill_color = 'red'
    circle2.attach_to(window)
    window.render()
    window.close_on_mouse_click()

def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # Done: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------
    window = rg.RoseWindow(500, 300, 'm6_2')
    center_point1 = rg.Point(300, 100)
    radius = 5
    circle1 = rg.Circle(center_point1, radius)
    circle1.fill_color = 'green'
    circle1.attach_to(window)
    print('outline thickness',circle1.outline_thickness)
    print('fill color', circle1.fill_color)
    print('center',circle1.center)
    print('center x',center_point1.x)
    print('center y',center_point1.y)
    point3 = rg.Point(100, 150)
    point4 = rg.Point(200, 50)
    rectangle1 = rg.Rectangle(point3, point4)
    center_point2 = rectangle1.get_center()
    rectangle1.attach_to(window)
    print('outline thickness', rectangle1.outline_thickness)
    print('fill color', rectangle1.fill_color)
    print('center', center_point2)
    print('center x', center_point2.x)
    print('center y', center_point2.y)
    window.render()
    window.close_on_mouse_click()
def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # Done: 4. Implement and test this function.
    # -------------------------------------------------------------------------
    window = rg.RoseWindow(500, 300, 'm6_3')
    p1 = rg.Point(100, 150)
    p2 = rg.Point(200, 50)
    p3 = rg.Point(90,220)
    p4 = rg.Point(130,200)
    line1 = rg.Line(p1,p2)
    line2 = rg.Line(p3,p4)
    line2.thickness = 6
    p5 = line1.get_midpoint()
    p6 = line2.get_midpoint()
    line1.attach_to(window)
    line2.attach_to(window)
    window.render()
    window.close_on_mouse_click()
    print('midpoint', p5)
    print('center x', p5.x)
    print('center y', p5.y)
    print('midpoint', p6)
    print('center x', p6.x)
    print('center y', p6.y)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
