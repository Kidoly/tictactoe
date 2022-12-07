# Mathéo DELAUNAY
# Alban MARY
lesPositions = {'7': ' ', '8': ' ', '9': ' ',
                '4': ' ', '5': ' ', '6': ' ',
                '1': ' ', '2': ' ', '3': ' '}
def tictactoe():
    nb = 0
    formes = ['0', 'X']
    victoire = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['7', '4', '1'], ['8', '5', '2'], ['9', '6', '3'], ['7', '5', '3'], ['9', '5', '1']]
    print("7|8|9")
    print("4|5|6")
    print("1|2|3")
    player = ['0', 'X']
    player[0] = str(input("Donner le pseudo du premier joueur:"))
    player[1] = str(input("Donner le pseudo du deuxième joueur:"))
    while True:
        for i in (0, 1):
            nb += 1
            position = str(input(f"Joueur {player[i]} saisissez où placer votre signe:"))
            while int(position) > 9 or int(position) < 0 or lesPositions[position] != ' ':
                position = str(input(f'Joueur {player[i]} resaisissez où placer votre signe car cette emplacement est déjà pris:'))
            lesPositions[position] = formes[i]
            print(lesPositions["7"], "|", lesPositions["8"], "|", lesPositions["9"], "           7|8|9")
            print(lesPositions["4"], "|", lesPositions["5"], "|", lesPositions["6"], "           4|5|6")
            print(lesPositions["1"], "|", lesPositions["2"], "|", lesPositions["3"], "           1|2|3")
            for j in range(8):
                if lesPositions[victoire[j][0]] == formes[i] and lesPositions[victoire[j][1]] == formes[i] and lesPositions[victoire[j][2]] == formes[i]:
                    return "Le jouer jouant les", player[i], "a gagné"
                elif nb > 8:
                    return "match nul"
print(tictactoe())
