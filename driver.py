#BARCODE KEY:
#   ___color___    ___special/not___   ___number/skip/reverse___  ___specific card___

#Colors: Red = 0, Blue = 1, Green = 2, Yellow = 3, Black = 4
#Special/not: special = 1, not_special = 0
#number/skip/reverse: 1-9 for numbers, skip = 0 , reverse = 1, draw2 = 2, draw4 = 3, wild = 4

SKIP = 0
REVERSE = 1
DRAW2 = 2
DRAW4 = 3
WILD = 4
C_WILD = 5


#holds lists of every players cards. Ex: index 1 has p1's cards, (red 3, blue skip)
player_cards_list = []

#list of all cards that have been played
cards_read = []

cur_player = 0
num_cards_played = 0
num_players = int(input("Enter the number of players for the game: "))
counter_clockwise = True

#decide who the next player will be. card validation
def decide_next(code, last_code):
    global cur_player
    cur_player = get_player(code) #see who played the card.
    offset = 1

    #if it's special, and if it is a card that will skip
    if code[1] == 1 and (code[2] == SKIP or code[2] == DRAW2 or code[2] == DRAW4 or code[2] == C_WILD) :
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
                return i    #if going clockwise
        i += 1
    print("Big error: code not found in any hand\n")

#check if a play is valid given the last card played
def is_valid(code, last_code, last_offset):
    cur_player = get_player(code)
    last_player = get_player(last_code)

    offset = 1 if counter_clockwise else -1
    #if the player did not blood
    if (last_player + last_offset) % num_players == cur_player:
        #if they are the same color
        if code[0] == last_code[0]:
            return True
        #if they are the same number/reverse/skip/draw
        if code[2] == last_code[2]:
            return True
        #if it's a wild or a custom wild, any card is playable
        if last_code[0] == 5 and last_code[1] == 1 and (last_code[2] == WILD or last_code[2] == C_WILD):
            return True
    #if the player is stacking a plus 2 or plus 4
    elif (last_player + offset) & num_players == cur_player:
        if last_code[1] == 1 and last_code[2] == DRAW2:
            return True
    #if  the player blooded
    else:
        return code[0] == last_code[0] and code[1] == last_code[1] and code[2] == last_code[2]

f = open("myfile.txt", "r")
#this is the first card that is flipped over to start the game.
last_code = f.readline()
last_code = last_code.strip('\n')
cards_read.append(last_code)
print("very first code = ", last_code,"\n")
#need to figure out how to actually start the game. pick player 0? See if someone can blood?
while True:
    #however many codes that have not been processed in the file (will be duplicates)
    for code in f:
        code = code.rstrip('\n')
        #if the current code has not been read yet
        if not code in cards_read:
            print("checking if code ",code," has been played.\n")
            if is_valid(code, last_code, last_offset):
                print("Thats a valid play! Right on bro.\n")
                cards_read.append(code)
                last_offset = decide_next(code, last_code)
                last_code = code
