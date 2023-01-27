import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def visualizer(player1, player2, winner):
    """
    (str, str, int) -> None
    This function visualizes the choices from player 1 and 2 and displays the winner.

    Example:
        rpsls_visualizer('Rock', 'Paper', 1)
        rpsls_visualizer('Scissors', 'Rock', 1)
    """

    # Setup figure
    fig = plt.figure(figsize=(20, 6))
    ax1 = plt.subplot2grid((1, 3), (0, 0))
    ax2 = plt.subplot2grid((1, 3), (0, 1))
    ax3 = plt.subplot2grid((1, 3), (0, 2))

    # Player 1
    player1_image = mpimg.imread('images/{}.png'.format(player1.lower()))
    ax1.set_title('Player 1', fontsize=24, y=1.05)
    ax1.imshow(player1_image)
    ax1.axes.xaxis.set_visible(False)
    ax1.axes.yaxis.set_visible(False)
    if winner == -1:
        [x.set_linewidth(10) for x in ax1.spines.values()]
        [x.set_color('green') for x in ax1.spines.values()]
    elif winner == 1:
        [x.set_linewidth(10) for x in ax1.spines.values()]
        [x.set_color('red') for x in ax1.spines.values()]
    else:
        [x.set_linewidth(10) for x in ax1.spines.values()]
        [x.set_color('yellow') for x in ax1.spines.values()]

    # VS
    player1_image = mpimg.imread('images/vs.png')
    ax2.imshow(player1_image)
    ax2.axes.xaxis.set_visible(False)
    ax2.axes.yaxis.set_visible(False)
    ax2.axis('off')

    # Player 2
    player2_image = mpimg.imread('images/{}.png'.format(player2.lower()))
    ax3.set_title('Computer', fontsize=24, y=1.05)
    ax3.imshow(player2_image)
    ax3.axes.xaxis.set_visible(False)
    ax3.axes.yaxis.set_visible(False)
    if winner == 1:
        [x.set_linewidth(10) for x in ax3.spines.values()]
        [x.set_color('green') for x in ax3.spines.values()]
    elif winner == -1:
        [x.set_linewidth(10) for x in ax3.spines.values()]
        [x.set_color('red') for x in ax3.spines.values()]
    else:
        [x.set_linewidth(10) for x in ax3.spines.values()]
        [x.set_color('yellow') for x in ax3.spines.values()]
