"""
This module contains plotting functions used in Week 2 Lecture 3 of APS106.
"""
# Third party imports
import matplotlib.pylab as plt
from ipywidgets import interact, fixed, IntSlider, FloatText


def plot_end_effector_position(func) -> None:

    """
    This function take a function we developed in class as input and generated an interactive plot.
    :param func:
    :return:
    """

    def plot(len1: float, ang1: float, len2: float, ang2: float, origin_x: float, origin_y: float) -> None:

        """
        Create a 2D plot of a robotic arm with two degrees of freedom given the length and angle of each arm.
        :param float len1:
        :param float ang1:
        :param float len2:
        :param float ang2:
        :param float origin_x:
        :param float origin_y:
        :return: None
        """

        # Call function
        dx1, dy1, dx2, dy2, x, y = func(len1, ang1, len2, ang2)

        # Setup figure
        plt.figure(figsize=(6, 6))

        # Plot lines
        plt.plot([origin_x - 20, origin_x + 20], [0, 0], '-', color=[0.7, 0.7, 0.7])
        plt.plot([0, 0], [origin_y - 20, origin_y + 20], '-', color=[0.7, 0.7, 0.7])
        plt.plot([origin_x, origin_x + dx1], [origin_y, origin_y + dy1], '-', color='#008fd5', lw=4)
        plt.plot([origin_x + dx1, origin_x + x], [origin_y + dy1, origin_y + y], '-', color='#fc4f30', lw=4)

        # Plot markers
        plt.plot(origin_x, origin_y, 'o', color='#e5ae38', ms=10)
        plt.plot(origin_x + dx1, origin_y + dy1, 'o', color='#6d904f', ms=10)
        plt.plot(origin_x + x, origin_y + y, 'o', color='#810f7c', ms=10)

        # Add text box
        plt.text(origin_x + x + 2, origin_y + y + 1,
                 'X = {:.2f}\nY = {:.2f}'.format(origin_x + x, origin_y + y),
                 fontsize=14, verticalalignment='top')

        # Config plot
        plt.xlabel('X', fontsize=20)
        plt.ylabel('Y', fontsize=20)
        plt.xlim([origin_x - 20, origin_x + 20])
        plt.ylim([origin_y - 20, origin_y + 20])
        plt.tick_params(axis='both', which='major', labelsize=14)
        plt.show()

    # Launch interactive widget
    interact(plot,
             origin_x=FloatText(),
             origin_y=FloatText(),
             len1=IntSlider(value=5, min=0, max=10, step=1),
             ang1=IntSlider(value=45, min=-360, max=360, step=10),
             len2=IntSlider(value=5, min=0, max=10, step=1),
             ang2=IntSlider(value=0, min=-360, max=360, step=10),
             func=fixed(func))
