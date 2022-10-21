def continue_walking(turtle):
    """
    (turtle) --> bool
    Will determine if the turtle has hit the left wall or if it is ok to continue walking.

    Example:
        at_wall(turtle)
        >> True
    """
    if turtle.get_state()['points'][-1]['x'] == 380:
        return False
    else:
        return True
