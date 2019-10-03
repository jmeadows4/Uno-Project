#BARCODE KEY:
#   ___color___    ___special/not___   ___number/skip/reverse___  ___specific card___

#Colors: Red = 0, Blue = 1, Green = 2, Yellow = 3, Black = 4
#Special/not: special = 1, not_special = 0
#number/skip/reverse: 1-9 for numbers, skip = 0 , reverse = 1, draw2 = 2, draw4 = 3

SKIP = 0
REVERSE = 1
DRAW2 = 2
DRAW4 = 3


#holds lists of every players cards. Ex: index 1 has p1's cards, (red 3, blue skip)
player_cards_list = []

#list of all cards that have been played
cards_read = []

cur_player = 0
num_cards_played = 0
num_players = int(input("Enter the number of players for the game: "))
counter_clockwise = True

#initialized with the first card that get's played later
last_card_played = 0


#decide who the next player will be
def decide_next(code, last_code):
    global cur_player
    cur_player = get_player(code) #see who played the card.
    offset = 1

    #if it's special, and if it is a card that will skip
    if code[1] == 1 and (code[2] == SKIP or code[2] == DRAW2 or code[2] == DRAW4) :
        offset = 2
    elif code[1] == 1 and code[2] == REVERSE:
        counter_clockwise = not counter_clockwise

    if counter_clockwise:
        cur_player = (cur_player + offset) % num_players
    else:
        cur_player = (cur_player - offset) % num_players

    #maybe return the offset so that for the next play, we can check if the player
    #is blooding or not(to see if it's a valid play)
    return offset

def get_player(code):
    i = 0
    for list in player_cards_list:
        for cur_code in list:
            if code == cur_code:
                return i
        i += 1
    print("Big error: code not found in any hand")

#this currently does not check for +2 and +4 stacking
def is_valid(code, last_code, last_offset):
    cur_player = get_player(code)
    last_player = get_player(last_code)

    if counter_clockwise:
        #if the player did not blood
        if (last_player + last_offset) % num_players == cur_player:
            #if they are the same color and not special
            if code[0] == last_code[0] and code[1] == 0:
                return True
            #if they are not special and the same number
            if code[1] == last_code[1] == 0 and code[2] == last_code[2]:
                return True
        else:

    else:
        if (last_player - last_offset) % num_players == cur_player:

        else:


f = open("myfile.txt", "r")
while True:
    #however many codes that have not been processed in the file (will be duplicates)
    for code in f:
        code = code.rstrip('\n')
        #if the current code has not been read yet
        if not code in cards_played:
            if is_valid(code, last_code, last_offset):
                cards_played.append(code)
                last_offset = decide_next(code, last_code)
                last_code = code
