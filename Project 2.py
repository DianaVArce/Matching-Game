"""
Program: CS-115 Project 2 Extra Credit Version
Author: Diana Vanessa Arce-Hernandez
Description: This is a matching game. The user will find 12 pairs of matching cards, that the program will cross out
if it is a match. The game will flash bright colors once all 12 pairs are found. There is one wild card that will not
have a pair - the game randomizes which will have pairs and which will be a wild card at the beginning of each new game,
so it will be different every time.

**Extra Credit Enhancements to game are as follows:
-- A new fantasy/princess set of icons have been added
-- Color scheme for the game has changed: The card background is now red and the outline is grey.
-- The matched X is now black instead of red when pairs are found.
-- The entire board game background has been changed to a darker maroon color in match_graphics to better fit the
theme of this version o
"""
from match_graphics import *


def shuffle_cards():
    '''
    Generates a shuffled deck of cards. When done, cards[i][j] is the name
    of the card in row i and column j. It is a 5x5 grid comprised of 12
    card pairs and one extra card.

    :param: None
    :return: a list of the shuffled cards
    '''

    shuffle(images)
    image = images
    matches = image[0:12]
    no_match = image[12:]

    image_list = []
    image_list.append(no_match[0])
    for i in range(len(matches)):
        image_list.append(matches[i])
        image_list.append(matches[i])
    shuffle(image_list)

    cards = []
    card_array = 0
    for i in range(5):
        row = []
        for j in range(5):
            item = image_list[card_array]
            row.append(item)
            card_array += 1
        cards.append(row)
    return cards


def show_card(win, card_name, i, j):
    '''
    Shows the card at row i and column j in the 5x5 grid in the window.
    the examples in match_graphics

    :param win: the graphics window
    :param card_name: potion of card at [i][j]
    :param i: index of the list at i
    :param j: index of the list at j
    :return: None
    '''

    rec1 = Point(XMARGIN + CARD_WIDTH * j, YMARGIN + CARD_HEIGHT * i)
    rec2 = Point(XMARGIN + CARD_WIDTH * (j + 1), YMARGIN + CARD_HEIGHT * (i + 1))
    rec = Rectangle(rec1, rec2)
    rec.setOutline('grey')
    rec.setWidth(5)
    rec.draw(win)

    c_x = (XMARGIN + CARD_WIDTH * j) + (1 / 2 * CARD_WIDTH)
    c_y = (YMARGIN + CARD_WIDTH * i) + (1 / 2 * CARD_HEIGHT)
    card_name = Image(Point(c_x, c_y), card_name)
    card_name.draw(win)

    return

def hide_card(win, i, j):
    '''
    Takes the window and cards and hides the card at row i and column j.

    :param win: the graphics window
    :param i: index of the list at i
    :param j: index of the list at j
    :return: None
    '''

    rec1 = Point(XMARGIN + CARD_WIDTH * j, YMARGIN + CARD_HEIGHT * i)
    rec2 = Point(YMARGIN + CARD_WIDTH * (j + 1), YMARGIN + CARD_HEIGHT * (i + 1))
    rec = Rectangle(rec1, rec2)
    rec.setOutline('grey')
    rec.setFill('red')
    rec.setWidth(5)
    rec.draw(win)
    return


def mark_card(win, i, j):
    '''
    Takes the window and cards and marks the card at row i and column j
    with a red X.

    :param win: the graphics window
    :param i: index of the list at i
    :param j: index of the list at j
    :return: None
    '''

    f_line1 = Point(XMARGIN + CARD_WIDTH * j, YMARGIN + CARD_HEIGHT * i)
    f_line2 = Point(XMARGIN + CARD_WIDTH * (j + 1), YMARGIN + CARD_HEIGHT * (i + 1))
    line1 = Line(f_line1, f_line2)
    line1.setOutline('black')
    line1.setWidth(5)
    line1.draw(win)

    s_line1 = Point((XMARGIN + CARD_WIDTH * j) + CARD_WIDTH, (YMARGIN + CARD_HEIGHT * i))
    s_line2 = Point((XMARGIN + CARD_WIDTH * (j + 1)) - CARD_WIDTH, (YMARGIN + CARD_HEIGHT * (i + 1)))
    line2 = Line(s_line1, s_line2)
    line2.setOutline('black')
    line2.setWidth(5)
    line2.draw(win)
    return


def get_col(x):
    '''
    Takes the x-coordinate value and returns the column.
    If the x coordinate is outside the board, returns -1.

    :param x: x-coordinate of the user's click
    :return 0-4: the column in which the click took place
    :return -1: If x-coordinate is outside the board
    '''

    if x > XMARGIN and x < BOARD_WIDTH - XMARGIN:

        if XMARGIN + CARD_WIDTH > x > XMARGIN:
            col = 0
            return col
        if XMARGIN + 2*CARD_WIDTH > x > XMARGIN + CARD_WIDTH:
            col = 1
            return col
        if XMARGIN + 3*CARD_WIDTH > x > XMARGIN + 2*CARD_WIDTH:
            col = 2
            return col
        if XMARGIN + 4*CARD_WIDTH > x > XMARGIN + 3*CARD_WIDTH:
            col = 3
            return col
        if XMARGIN + 5*CARD_WIDTH > x > XMARGIN + 4*CARD_WIDTH:
            col = 4
            return col
    else:
        return -1

def get_row(y):
    '''
    Takes the y-coordinate value and returns the row.
    If the y-coordinate is outside the board, returns -1.

    :param y: y-coordinate of the user's click
    :return 0-4: the column in which the click took place
    :return -1: If y-coordinate is outside the board
    '''

    if y > XMARGIN and y < BOARD_HEIGHT - YMARGIN:

        if YMARGIN + CARD_HEIGHT > y > YMARGIN:
            row = 0
            return row
        if YMARGIN + 2*CARD_HEIGHT > y > YMARGIN + CARD_HEIGHT:
            row = 1
            return row
        if YMARGIN + 3*CARD_HEIGHT > y > YMARGIN + 2*CARD_HEIGHT:
            row = 2
            return row
        if YMARGIN + 4*CARD_HEIGHT > y > YMARGIN + 3*CARD_HEIGHT:
            row = 3
            return row
        if YMARGIN + 5*CARD_HEIGHT > y > YMARGIN + 4*CARD_HEIGHT:
            row = 4
            return row
    else:
        return -1

def main():

    try:
        win = create_board()
        card = 1
        cards = shuffle_cards()
        matches_list = []
        game = True

        for i in range(5):
            for j in range(5):
                hide_card(win, i, j)

        while game == True:

            c_point = win.getMouse()
            x_c = int(c_point.getX())
            y_c = int(c_point.getY())

            #initial click for the user
            col = get_col(x_c)
            row = get_row(y_c)
            first_pick = (row, col)
            #ensures that the matches aren't able to click again
            if first_pick in matches_list:
                pass

            #first pick that turns over the first card
            elif card == 1 and col != -1 and row != -1:
                card = card + 1
                show_card(win, cards[row][col], row, col)
                current_pick = (row, col)
                new_row = row
                new_col = col

            #second pick that turns over the second card
            elif card == 2 and col != -1 and row != -1:
                #ensures that the first card picked isn't the same one
                if first_pick == current_pick:
                    continue

                show_card(win, cards[row][col], row, col)
                game_delay(1)

                #checks if the cards are a matches
                if cards[row][col] == cards[new_row][new_col]:
                    mark_card(win, row, col)
                    mark_card(win, new_row, new_col)
                    first_pair = (row, col)
                    second_pair = (new_row, new_col)
                    matches_list.append(first_pair)
                    matches_list.append(second_pair)
                    card = card - 1
                else:
                    hide_card(win, row, col)
                    hide_card(win, new_row, new_col)
                    card = card - 1

            #once all are matched, calls the you won function
            if len(matches_list) == 24:
                    you_won(win)
                    card = False

        win.getMouse()

    except GraphicsError:
        pass

main()