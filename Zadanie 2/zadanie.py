class Piece:
    def __init__(self, color, x, y, type):
        if color == 'b':
            self.color = "black"
        else:
            self.color = "white"
        self.x = x
        self.y = y
        if type == 'p':
            self.type = "Pawn"
        elif type == 'r':
            self.type = "Rook"
        elif type == 'k':
            self.type = "Knight"
        elif type == 'b':
            self.type = "Bishoop"
        elif type == 'q':
            self.type = "Queen"
        elif type == 'W':
            self.type = "King"

    def position(self):
        return [self.x, self.y]

    def row(self):
        return self.x

    def collumn(self):
        return self.y

    def type(self):
        return self.type

    def remove_wrong_moves(self, moves):
        wrong_moves = []
        for i in moves:
            if i[0] < 1 or i[1] < 1 or i[0] > 8 or i[1] > 8:
                wrong_moves.append(i)
        for i in wrong_moves:
            moves.remove(i)

        return moves


class King(Piece):
    def moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                move = [self.x - 1 + i, self.y - 1 + j]
                moves.append(move)
        moves.remove([self.x, self.y])
        moves = Piece.remove_wrong_moves(self, moves)
        return moves


class Pawn(Piece):
    def moves(self):
        moves = []
        if self.color == "black":
            if self.x + 1 == 9:
                pass
            else:
                moves.append([self.x + 1, self.y])
        else:
            if self.x - 1 == 0:
                pass
            else:
                moves.append([self.x - 1, self.y])
        return moves


class Knight(Piece):
    def moves(self):
        moves = []
        a = 2
        b = 1
        for i in range(8):
            moves.append([self.x + a, self.y + b])
            if a*b > 0:
                a = -a
            elif a*b < 0:
                b = -b
            if i == 3:
                a, b = b, a
        moves = Piece.remove_wrong_moves(self, moves)
        return moves


class Rook(Piece):
    def moves(self):
        moves = []
        for j in range(4):
            for i in range(7):
                if j == 0:
                    moves.append([self.x + 1 + i, self.y])
                elif j == 1:
                    moves.append([self.x - 1 - i, self.y])
                elif j == 2:
                    moves.append([self.x, self.y + 1 + i])
                else:
                    moves.append([self.x, self.y - 1 - i])
        moves = Piece.remove_wrong_moves(self, moves)
        return moves


class Bishop(Piece):
    def moves(self):
        moves = []
        for j in range(4):
            for i in range(7):
                if j == 0:
                    moves.append([self.x + 1 + i, self.y + 1 + i])
                elif j == 1:
                    moves.append([self.x - 1 - i, self.y + 1 + i])
                elif j == 2:
                    moves.append([self.x + 1 + i, self.y - 1 - i])
                elif j == 3:
                    moves.append([self.x - 1 - i, self.y - 1 - i])
        moves = Piece.remove_wrong_moves(self, moves)
        return moves


class Queen(Piece):
    def moves(self):
        moves = []
        for j in range(8):
            for i in range(7):
                if j == 0:
                    moves.append([self.x + 1 + i, self.y])
                    #moves.append([self.x + 1 + i, self.y + 1 + i]) do 4 lini
                elif j == 1:
                    moves.append([self.x - 1 - i, self.y])
                    #moves.append([self.x - 1 - i, self.y + 1 + i]) do 5 lini
                elif j == 2:
                    moves.append([self.x, self.y + 1 + i])
                    #moves.append([self.x + 1 + i, self.y - 1 - i]) do 6 lini
                elif j == 3:
                    moves.append([self.x, self.y - 1 - i])
                    #moves.append([self.x - 1 - i, self.y - 1 - i]) do 7 lini
                elif j == 4:
                    moves.append([self.x + 1 + i, self.y + 1 + 1])
                elif j == 5:
                    moves.append([self.x - 1 - i, self.y + 1 + i])
                elif j == 6:
                    moves.append([self.x + 1 + i, self.y - 1 - i])
                else:
                    moves.append([self.x - 1 - i, self.y - 1 - i])
        moves = Piece.remove_wrong_moves(self, moves)
        return moves


def czytaj_plansze(tablica):
    """
    Pozycja w tablicy a figóra:
    0 - pion
    1 - wierza
    2 - skoczek
    3 - gońca
    4 - krolowa
    5 - krol
    """
    biale = [[], [], [], [], [], []]
    czarne = [[], [], [], [], [], []]
    for i in range(len(tablica)):
        for j in range(len(tablica[i])):
            if tablica[i][j] != '--':
                if tablica[i][j][0] == 'w':
                    if tablica[i][j][1] == 'p':
                        biale[0].append(Pawn('w', i+1, j+1, 'p'))
                    elif tablica[i][j][1] == 'r':
                        biale[1].append(Rook('w', i+1, j+1, 'r'))
                    elif tablica[i][j][1] == 'k':
                        biale[2].append(Knight('w', i+1, j+1, 'k'))
                    elif tablica[i][j][1] == 'b':
                        biale[3].append(Bishop('w', i+1, j+1, 'b'))
                    elif tablica[i][j][1] == 'q':
                        biale[4].append(Queen('w', i+1, j+1, 'q'))
                    elif tablica[i][j][1] == 'W':
                        biale[5].append(King('w', i+1, j+1, 'W'))
                elif tablica[i][j][0] == 'b':
                    if tablica[i][j][1] == 'p':
                        czarne[0].append(Pawn('b', i+1, j+1, 'p'))
                    elif tablica[i][j][1] == 'r':
                        czarne[1].append(Rook('b', i+1, j+1, 'r'))
                    elif tablica[i][j][1] == 'k':
                        czarne[2].append(Knight('b', i+1, j+1, 'k'))
                    elif tablica[i][j][1] == 'b':
                        czarne[3].append(Bishop('b', i+1, j+1, 'b'))
                    elif tablica[i][j][1] == 'q':
                        czarne[4].append(Queen('b', i+1, j+1, 'q'))
                    elif tablica[i][j][1] == 'W':
                        czarne[5].append(King('b', i+1, j+1, 'W'))
    return biale, czarne


def zablokowane_ruchy(figurka, move, czarne, biale):
    wrong_moves = []
    if move:
        for i in czarne:
            for j in i:
                for x in move:
                    if x == j.position():
                        wrong_moves.append(x)
        for i in biale:
            for j in i:
                for x in move:
                    if x == j.position():
                        wrong_moves.append(x)
        tym = wrong_moves.copy()
        if figurka.type == 'Rook':
            for i in wrong_moves:
                if i[0] > figurka.x:
                    while i[0] < 8:
                        i[0] += 1
                        tym.append([i[0], i[1]])
                elif i[0] < figurka.x:
                    while i[0] > 1:
                        i[0] -= 1
                        tym.append([i[0], i[1]])
                elif i[1] > figurka.y:
                    while i[1] < 8:
                        i[1] += 1
                        tym.append([i[0], i[1]])
                elif i[1] < figurka.y:
                    while i[1] > 1:
                        i[1] -= 1
                        tym.append([i[0], i[1]])
        elif figurka.type == 'Bishoop':
            for i in wrong_moves:
                if i[0] > figurka.x and i[1] > figurka.y:
                    while i[0] < 8 and i[1] < 8:
                        i[0] += 1
                        i[1] += 1
                        tym.append([i[0],i[1]])
                elif i[0] > figurka.x and i[1] < figurka.y:
                    while i[0] < 8 and i[1] > 1:
                        i[0] += 1
                        i[1] -= 1
                        tym.append([i[0], i[1]])
                elif i[0] < figurka.x and i[1] > figurka.y:
                    while i[0] > 1 and i[1] < 8:
                        i[0] -= 1
                        i[1] += 1
                        tym.append([i[0], i[1]])
                elif i[0] < figurka.x and i[1] < figurka.y:
                    while i[0] > 1 and i[1] > 1:
                        i[0] -= 1
                        i[1] -= 1
                        tym.append([i[0], i[1]])
        elif figurka.type == "Queen":
            licznik = 0
            for i in wrong_moves:
                if i[0] > figurka.x and i[1] > figurka.y:
                    while i[0] < 8 and i[1] < 8:
                        i[0] += 1
                        i[1] += 1
                        tym.append([i[0], i[1]])
                elif i[0] > figurka.x and i[1] < figurka.y:
                    while i[0] < 8 and i[1] > 1:
                        i[0] += 1
                        i[1] -= 1
                        tym.append([i[0], i[1]])
                elif i[0] < figurka.x and i[1] > figurka.y:
                    while i[0] > 1 and i[1] < 8:
                        i[0] -= 1
                        i[1] += 1
                        tym.append([i[0], i[1]])
                elif i[0] < figurka.x and i[1] < figurka.y:
                    while i[0] > 1 and i[1] > 1:
                        i[0] -= 1
                        i[1] -= 1
                        tym.append([i[0], i[1]])
                elif i[0] > figurka.x:
                    while i[0] < 8:
                        i[0] += 1
                        tym.append([i[0], i[1]])
                elif i[0] < figurka.x:
                    while i[0] > 1:
                        i[0] -= 1
                        tym.append([i[0], i[1]])
                elif i[1] > figurka.y:
                    while i[1] < 8:
                        i[1] += 1
                        tym.append([i[0], i[1]])
                elif i[1] < figurka.y:
                    while i[1] > 1:
                        i[1] -= 1
                        tym.append([i[0], i[1]])
                licznik += 1
        for i in tym:
            try:
                move.remove(i)
            except:
                pass
        return move
    return figurka.moves()


def szachowanie(figura, moves):
    seria_ruchow_szach = []
    krol_rzad = biale[5][0].x
    krol_kolumna = biale[5][0].y
    if figura.color == "white":
        krol_rzad = czarne[5][0].x
        krol_kolumna = czarne[5][0].y
    if figura.type == "Pawn" and figura.color == "white":
        for i in moves:
            if i[0] - 1 == krol_rzad and i[1] - 1 == krol_kolumna:
                print("ruch z: ", figura.x, ",", figura.y, "na: ", i[0], ",", i[1], "SZACH!")
                seria_ruchow_szach.append(i)
            elif i[0] - 1 == krol_rzad and i[1] + 1 == krol_kolumna:
                print("ruch z: ", figura.x, ",", figura.y, "na: ", i[0], ",", i[1], "SZACH!")
                seria_ruchow_szach.append(i)
    if figura.type == "Pawn" and figura.color == "black":
        for i in moves:
            if i[0] + 1 == krol_rzad and i[1] - 1 == krol_kolumna:
                print("ruch z: ", figura.x, ",", figura.y, "na: ", i[0], ",", i[1], "SZACH!")
                seria_ruchow_szach.append(i)
            elif i[0] + 1 == krol_rzad and i[1] + 1 == krol_kolumna:
                print("ruch z: ", figura.x, ",", figura.y, "na: ", i[0], ",", i[1], "SZACH!")
                seria_ruchow_szach.append(i)
    if figura.type == "Rook":
        for i in moves:
            if i[0] == krol_rzad:
                print("ruch z: ", figura.x, ",", figura.y, "na: ", i[0], ",", i[1], "SZACH!")
                seria_ruchow_szach.append(i)
            elif i[1] == krol_kolumna:
                print("ruch z: ", figura.x, ",", figura.y, "na: ", i[0], ",", i[1], "SZACH!")
                seria_ruchow_szach.append(i)
    if figura.type == "Knight":
        a = 2
        b = 1
        for i in moves:
            for j in range(8):
                if i[0] + a == krol_rzad and i[1] + b == krol_kolumna:
                    print("ruch z: ", figura.x, ",", figura.y, "na: ", i[0], ",", i[1], "SZACH!")
                    seria_ruchow_szach.append(i)
                if a * b > 0:
                    a = -a
                elif a * b < 0:
                    b = -b
                if j == 3:
                    a, b = b, a
    if figura.type == "Bishoop":
        for i in moves:
            for j in range(4):
                for a in range(7):
                    if j == 0:
                        if i[0] + 1 + a == krol_rzad and i[1] + 1 + a == krol_kolumna:
                            print("ruch z: ", figura.x, ",", figura.y, "na: ", i[0], ",", i[1], "SZACH!")
                            seria_ruchow_szach.append(i)
                    elif j == 1:
                        if i[0] - 1 - a == krol_rzad and i[1] + 1 + a == krol_kolumna:
                            print("ruch z: ", figura.x, ",", figura.y, "na: ", i[0], ",", i[1], "SZACH!")
                            seria_ruchow_szach.append(i)
                    elif j == 2:
                        if i[0] + 1 + a == krol_rzad and i[1] - 1 - a == krol_kolumna:
                            print("ruch z: ", figura.x, ",", figura.y, "na: ", i[0], ",", i[1], "SZACH!")
                            seria_ruchow_szach.append(i)
                    elif j == 3:
                        if i[0] - 1 - a == krol_rzad and i[1] - 1 - a == krol_kolumna:
                            print("ruch z: ", figura.x, ",", figura.y, "na: ", i[0], ",", i[1], "SZACH!")
                            seria_ruchow_szach.append(i)
    if figura.type == "Queen":
        for i in moves:
            for j in range(4):
                for a in range(7):
                    if j == 0:
                        if i[0] + 1 + a == krol_rzad and i[1] + 1 + a == krol_kolumna:
                            print("ruch z: ", figura.x, ",", figura.y, "na: ", i[0], ",", i[1], "SZACH!")
                            seria_ruchow_szach.append(i)
                    elif j == 1:
                        if i[0] - 1 - a == krol_rzad and i[1] + 1 + a == krol_kolumna:
                            print("ruch z: ", figura.x, ",", figura.y, "na: ", i[0], ",", i[1], "SZACH!")
                            seria_ruchow_szach.append(i)
                    elif j == 2:
                        if i[0] + 1 + a == krol_rzad and i[1] - 1 - a == krol_kolumna:
                            print("ruch z: ", figura.x, ",", figura.y, "na: ", i[0], ",", i[1], "SZACH!")
                            seria_ruchow_szach.append(i)
                    elif j == 3:
                        if i[0] - 1 - a == krol_rzad and i[1] - 1 - a == krol_kolumna:
                            print("ruch z: ", figura.x, ",", figura.y, "na: ", i[0], ",", i[1], "SZACH!")
                            seria_ruchow_szach.append(i)
            if i[0] == krol_rzad:
                print("ruch z: ", figura.x, ",", figura.y, "na: ", i[0], ",", i[1], "SZACH!")
                seria_ruchow_szach.append(i)
            elif i[1] == krol_kolumna:
                print("ruch z: ", figura.x, ",", figura.y, "na: ", i[0], ",", i[1], "SZACH!")
                seria_ruchow_szach.append(i)
    return seria_ruchow_szach


def krolowie():
    czarny_krol = zablokowane_ruchy(czarne[5][0], czarne[5][0].moves(), czarne, biale)
    for i in wszystkie_biale:
        for a in i:
            for j in czarny_krol.copy():
                if a == j:
                    czarny_krol.remove(a)
    bialy_krol = zablokowane_ruchy(biale[5][0], biale[5][0].moves(), czarne, biale)
    for i in wszystkie_czarne:
        for a in i:
            for j in bialy_krol.copy():
                if a == j:
                    bialy_krol.remove(a)
    return bialy_krol, czarny_krol


board = [['--', '--', 'bW', '--', '--', '--', '--', '--'],
         ['--', '--', '--', '--', 'wr', '--', '--', '--'],
         ['--', '--', '--', '--', '--', '--', '--', '--'],
         ['--', '--', '--', 'wq', '--', '--', '--', '--'],
         ['--', '--', '--', '--', '--', '--', '--', '--'],
         ['--', 'bp', '--', '--', '--', '--', '--', '--'],
         ['--', '--', '--', '--', '--', '--', '--', 'wp'],
         ['--', '--', '--', '--', 'wW', '--', '--', '--']]
biale, czarne = czytaj_plansze(board)
wszystkie_biale = []
wszystkie_czarne = []
wszystkie_szachujace = []
print("Biale:")
for i in range(len(biale)):
    for j in biale[i]:
        moves = zablokowane_ruchy(j, j.moves(), czarne, biale)
        print(j.type, ":")
        print(moves)
        szach = szachowanie(j, moves)
        print(szach)
        wszystkie_szachujace.append([j.type,szach])
        wszystkie_biale.append(moves)

print("\nCzarne:")
for i in range(len(czarne)):
    for j in czarne[i]:
        moves = zablokowane_ruchy(j, j.moves(), czarne, biale)
        print(j.type, ":")
        print(moves)
        szach = szachowanie(j, moves)
        print(szach)
        wszystkie_czarne.append(moves)

print("Ruchy królów: ", krolowie())

