# MyEducation
Exercitii invatare Python
### __Exercitiu: Se dau 3 pahare. O bila se afla sub unul din cele 3 pahare. Jucatorul trebuie sa aleaga un pahar. Daca bila este acolo, a castigat, daca nu, a pierdut__

### Din modulul random importam functia shuffle
```
from random import shuffle
```

### Initial avem o lista cu 3 elemente. Doua sunt stringuri goale, iar unul un string cu litera **O**, adica locul unde se afla bila. 

```
mylist = [" ", "O", " "]
```

### Cream o functie care amesteca lista initiala cu ajutorul functiei shuffle

```
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
```

### Cream o functie care sa ne returneze alegerea jucatorului. Pornim de la un string gol. Punem conditia ca jucatorul sa aleaga doar unul din cele 3 numere: 0,1 sau 2.
### Daca alege altceva, va fi intors in bucla pana introduce un numar valid.


```
def player_guess():
    guess = ""
    while guess not in ["0","1","2"]:
        guess = input("Alege unul din numerele: 0, 1 sau 2:  ")
    return int(guess)
```

# Cream o functie care imi verfica alegerea jucatorului

```
def check_guess(mylist, guess):
    if mylist[guess] == "O":
        print("Felicitari! Ai castigat!")
    else:
        print("Raspuns gresit! Poate ai mai mult succes data viitoare! ")
        print(f' Varianta corecta era {mylist.index("O")}')
```

## Interactiunea functiilor:

### Salvam rezultatul functiei shuffle_list intr o variabila numita mixedup_list
mixedup_list = shuffle_list(mylist)

### Salvam rezultatul functiei player_guess() intr o variabila guess_player

guess_player = player_guess()

### Apelam functia check_guess(mixedup_list, guess_player)

