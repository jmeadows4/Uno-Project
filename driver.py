#BARCODE KEY:
#   ___color___    ___special/not___   ___number/skip/reverse___  ___specific card___

#Colors: Red = 0, Blue = 1, Green = 2, Yellow = 3, Black = 4
#Special/not: special = 1, not_special = 0
#number/skip/reverse: 1-9 for numbers, skip = 10, reverse = 11, 



#holds lists of every players cards. Ex: index 1 has p1's cards, (red 3, blue skip)
player_cards_list = []

#list of all cards that have been played
cards_read = []

cur_person = 0
num_cards_played = 0
num_players = int(input("Enter the number of players for the game: "))
counter_clockwise = True 

#replace 0 with the first card shown?
last_card_played = 0

last_person = num_players-1 if cur_person == 0 else cur_person - 1



#could decide a way to check if the play is valid? We would need this, because if we dont have
#a reset button, there would be no way to reset idiot tax
def decide_next(code, last_code):

    #see who played the card.
    cur_player = get_cur_player(code)
    offset = 1

    if code[1] == 1 and code[2] == SKIP:
        print("skip played.\n")
        offset = 2
    elif code[1] == 1 and code[2] == REVERSE:
        print("reverse played.\n")
        counter_clockwise = not counter_clockwise

    if counter_clockwise:
        cur_player = cur_player + offset % num_players
    else:
        cur_player = cur_player - offset % num_players



def get_cur_player(code):
    i = 0
    for list in player_cards_list:
        for cur_code in list:
            if code == cur_code:
                return i
        i++
    print("Big error: code not found in any hand")


f = open("myfile.txt", "r")
while True:
    #however many codes that have not been processed in the file (will be duplicates)
    for code in f:
        code = code.rstrip('\n')
        #if the current code has not been read yet
        if not code in cards_played:
            cards_played.append(code)
            print("cur person = ", cur_person)
            decide_next(last_code, code)
            last_code = code











#problem: if a wildcard is played, there is no way to know what color is chosen. For now,
#maybe assume that all choices are okay
#def is_validlast_code, cur_code, last_player_cur_player):

#    #if the person is not blooding, they have more options to play
#    if not_blooding(cur_player, last_player):
        #if the last card is not a wild
#        if last_code[0] != 4:









