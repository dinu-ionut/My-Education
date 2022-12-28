from random import shuffle

mylist = [" ", "O", " "]


def shuffle_list(mylist):
    """
    Se amesteca o lista predefinita
    """
    shuffle(mylist)
    return mylist


def player_guess():
    """
    Alegerea pe care o face jucatorul
    """
    guess = ""
    while guess not in ["0", "1", "2"]:
        # Conditie pentru ca jucatorul sa nu aleaga alt numar
        guess = input("Alege unul din numerele: 0, 1 sau 2:  ")
    return int(guess)


def check_guess(mylist, guess):
    """
    Verifica alegerea jucatorului
    """
    if mylist[guess] == "O":
        print("Felicitari! Ai castigat!")
    else:
        print("Raspuns gresit! Poate ai mai mult succes data viitoare! ")
        print(f' Varianta corecta era {mylist.index("O")}')

# Interactiunea functiilor:

# Lista initiala:
mylist = [" ", "O", " "]

# lista amestecata
mixedup_list = shuffle_list(mylist)

# Alegerea jucatorului

guess_player = player_guess()

check_guess(mixedup_list, guess_player)

