''' Graphics functions for the Match Game project.

    DO NOT CHANGE THIS FILE. It contains constants and support functions
    for the Match Game. It also demonstrates expectations about how to
    document your functions.

    Functions include:
    - shuffle: permutes the items in a list.
    - you_won: flashes to signal the game is won.
    - create_board: draws the window for the game.
    - game_delay: pauses the game for a fraction of a second
    - random_color: a support function, picks random colors.

    See the specific documentation for each function.

    Author: Mark Gondree
'''

from graphics import *
from random import seed, randint
import time

# Icons made by various authors, Available on http://game-icons.net
images = ['icons/1.gif', 'icons/2.gif', 'icons/3.gif', 'icons/4.gif',
          'icons/5.gif', 'icons/6.gif', 'icons/7.gif', 'icons/8.gif',
          'icons/9.gif', 'icons/10.gif', 'icons/11.gif', 'icons/12.gif',
          'icons/13.gif']

# seed the random number generator for shuffle()
seed()


CARD_HEIGHT = 125   # height of the card (matched the height of each image)
CARD_WIDTH = 125    # width of the card (matches the width of each image)
XMARGIN = 25        # margin on the left and right of the board
YMARGIN = 25        # margin on the top and bottom of the board
BOARD_WIDTH = 2*XMARGIN + 5*CARD_WIDTH   # width of board, per above description
BOARD_HEIGHT = 2*YMARGIN + 5*CARD_HEIGHT # height of board, per above description


def shuffle(L):
    '''
    Permutes items in a list.

    :param L: the list
    :return: None
    '''
    from random import shuffle as permute    
    permute(L)


# noinspection PyUnreachableCode
def you_won(win):
    '''
    Call when the player wins (makes the board pretty).

    :param win: the game window
    :return: None
    '''
    while(True):
        win.setBackground(random_color())
        game_delay(0.2)
    return


def create_board():
    '''
    Generates the game window.

    :param: None
    :return: a graphics window
    '''
    window = GraphWin('Match Game', BOARD_WIDTH, BOARD_HEIGHT)
    window.setBackground('maroon')
    return window


def game_delay(sec):
    '''
    Pauses briefly in the game.

    :param sec: number of seconds
    :return: None
    '''
    time.sleep(float(sec))
    return


def random_color():
    '''
    This is the same function from the lab where we drew a grid of
    colored squared.

    :param: None
    :return: the string for a random color
    '''
    colors = ['blue', 'blue2', 'blue3',
              'green', 'green2', 'green3',
              'orange', 'orange2', 'orange3',
              'red', 'red2', 'red3',
              'purple', 'purple2', 'purple3',
              'yellow', 'yellow2', 'yellow3',
              'gray', 'gray2', 'gray3',
              'pink', 'pink1', 'pink2', 'pink3']
    return colors[randint(0, len(colors)-1)]
#    col = (x - XMARGIN) // CARD_WIDTH
#    row = (y - YMARGIN) // CARD_HEIGHT
