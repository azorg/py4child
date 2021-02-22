#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Крестики нолики 3x3 в терминале с подсказками компьютера
"""

# Размер игрового поля (клеток)
N = 3
M = 3
NM = N * M

# размер выигрышной линии
K = 3

# отладочная печать
debug = False

# игровое поле
board = ['.'] * NM

def draw_board(state):
    """распечатать игровое поле"""
    if   NM < 10:  digit = 1
    elif NM < 100: digit = 2
    else:          digit = 3
    line = "-" * ((digit + 3) * M + 1)  
    fmt = "%" + str(digit) + "s"
    print(line)
    for i in range(N):
        print("|", end='')
        for j in range(M):
            inx = i * M + j
            sym = state[inx]
            if sym not in "XO": sym = str(inx + 1) 
            print(" ", fmt % sym, " |", sep='', end='')
        print()
        print(line)

def check_win(state):
    """проверить выигрышность состояния (возвращяется 'X', 'O' или '')"""
    for i in range(N):
        for j in range(M):
            sym = state[i * M + j]
            if sym not in "XO": continue
            ans = b1 = b2 = False
            if M - j >= K: # проверка по горизонтали
                ans = b1 = True
                for k in range(1, K):
                    if sym != state[i * M + j + k]:
                        ans = False
                        break
            if ans: return sym
            if N - i >= K: # проверка по вертикали
                ans = b2 = True
                for k in range(1, K):
                    if sym != state[(i + k) * M + j]:
                        ans = False
                        break
            if ans: return sym
            if b1 and b2: # проверка по прямой диоганали
                ans = True
                for k in range(1, K):
                    if sym != state[(i + k) * M + j + k]:
                        ans = False
                        break
            if ans: return sym
            if j + 1 >= K and N - i >= K: # проверка по косой диоганали
                ans = True
                for k in range(1, K):
                    if sym != state[(i + k) * M + j - k]:
                        ans = False
                        break
            if ans: return sym
    return "" # нет выигрышной комбинации

def next_states(state):
    """сделать всевозможные ходы от state, рернуть список"""
    sym = 'X' if state.count('X') == state.count('O') else 'O' # чей ход?
    states = []
    for i in range(len(state)):
        if state[i] == '.': # клетка пуста
            next_state = list(state)
            next_state[i] = sym
            states.append(tuple(next_state))
    return tuple(states)

def build_tree():
    """построить дерево всевозможных исходов игры (без статистики)"""
    if debug: print("build_tree():")
    state = ('.',) * NM # исходное состояние игрового поля
    tree = {} # ключ - состояние поля
              # [0] - кортедж возможных последующих состояний
              # [1] - число выигрышных веток 'X'
              # [2] - число выигрышных веток 'O'
              # [3] - число веток "в ничью"
              # [4] - кто выиграл ('X' или 'O')
    steps = [ set([state]) ] # множество всевозможных состояний для каждого хода
    run = True
    cnt = 1 # счетчик ходов (1 - первый ход)
    while run:
        run = add = False
        for state in steps[cnt - 1]:
            win = check_win(state)
            if not win:
                nxt = next_states(state)
                if nxt:
                    run = True
                    if not add:
                        add = True
                        steps.append(set(nxt))
                    else:
                        for ns in nxt:
                            steps[cnt].add(ns)
                if state.count('X') + state.count('O') == NM:
                    tree[state] = [ nxt, 0, 0, 1, '' ] # ничья
                else:
                    tree[state] = [ nxt, 0, 0, 0, '' ]
            else: # выигрышное состояние
                if win == 'X':
                    tree[state] = [ (), 1, 0, 0, win ] # выиграл 'X'
                else:
                    tree[state] = [ (), 0, 1, 0, win ] # выиграл '0'
        if debug:
            variants = len(steps[cnt]) if len(steps) - 1 >= cnt else 0
            if variants:
                print("  " + ('O' if (cnt & 1) == 0 else 'X') +
                      ": cnt=", cnt, " variants=", variants, sep='')
        cnt += 1
    if debug:
        print("  len(steps)=", len(steps), sep='')
        print("  len(tree)=", len(tree), sep='')
    return steps, tree        

def fill_tree(steps, tree):
    """заполнить статистику выигрышей/проигрышей в дереве"""
    if debug: print("fill_tree():")
    cnt = len(steps) - 2
    while cnt >= 0: # идем в обратном порядке ходов
        for state in steps[cnt]:
            x = o = n = 0
            for nxt in tree[state][0]:
                x += tree[nxt][1]
                o += tree[nxt][2]
                n += tree[nxt][3]
            tree[state][1] += x
            tree[state][2] += o
            tree[state][3] += n
        cnt -= 1
    if debug:
        print("  x_cnt(0)=", tree[tuple(steps[0])[0]][1], sep='')
        print("  o_cnt(0)=", tree[tuple(steps[0])[0]][2], sep='')
        print("  n_cnt(0)=", tree[tuple(steps[0])[0]][3], sep='')

def help(state):
    """компьютерная помощь"""
    sym = 'X' if state.count('X') == state.count('O') else 'O' # чей ход?
    var = {}
    for i in range(NM):
        if state[i] not in "XO":
            nxt = list(state)
            nxt[i] = sym
            x = tree[tuple(nxt)][1]
            o = tree[tuple(nxt)][2]
            n = tree[tuple(nxt)][3]
            # FIXME: magic!!!
            if sym == 'X':
                #d = 100 * (x - 2 * o + 2 * n) // (x + 2 * o + n)
                d = x - o + n
            else:
                #d = 100 * (o - 2 * x + 2 * n) // (2 * x + o + n)
                d = o - x + n
            if debug:
                print(i + 1,
                      ": X=", tree[tuple(nxt)][1],
                       " O=", tree[tuple(nxt)][2],
                       " N=", tree[tuple(nxt)][3],
                       " D=", d, sep='')
            if d in var:
                var[d].append(i + 1)
            else:
                var[d] = [i + 1]
    if var:
        print("Рекомендованные ходы:", sep='', end='')
        keys = list(var.keys())
        keys.sort(reverse=True)
        for d in keys[:1:]:
            for i in var[d]:
                print(" ", i, sep='', end='')
            print()
    else:
        print("  Рекомендаций НЕТ - ошибка в программе")


def take_input(player_token):
    """запрос воода пользователя"""
    while True:
        player_answer = input("Куда поставим " + player_token + " (h-помощь)? ")
        if player_answer == 'h' or \
           player_answer == 'H':
            help(board)
            continue
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if 1 <= player_answer <= NM:
            if (str(board[player_answer - 1]) not in "XO"):
                board[player_answer - 1] = player_token
                break
            else:
                print("Эта клеточка уже занята")
        else:
            print("Некорректный ввод. Введите число от 1 до %i чтобы походить." % NM)


def main(board):
    """функция главного игрового цикла"""
    # посттролит дерево ВСЕХ решений
    global steps, tree
    steps, tree = build_tree()
    fill_tree(steps, tree)
    
    counter = 0
    while True:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        #print("counter =", counter)
        if counter > 4:
            win = check_win(board)
            if win:
                print(win, "выиграл!")
                break
        if counter == NM:
            print("Ничья!")
            break
    draw_board(board)


def unit_tests():
    """функция тестирования функций (DEBUG ONLY!)"""
    global N, M, NM, K
    N = M = K = 3
    NM = N * M
    
    # проверка функци check_win()
    s = ((('X', '.', '.',
           'X', '.', '.',
           'X', '.', '.'), 'X'), # 0
         (('O', '.', '.',
           '.', 'O', '.',
           '.', '.', 'O'), 'O'), # 1
         (('O', '.', '.',
           '.', 'O', '.',
           'X', 'X', 'X'), 'X'), # 2 
         (('O', '.', '.',
           'O', 'O', 'O',
           'X', 'X', 'O'), 'O'), # 3 
         (('.', '.', '.',
           'X', 'O', 'O',
           'O', 'X', 'O'), ''),  # 4 
         (('O', '.', 'X',
           '.', 'X', '.',
           'X', 'O', 'O'), 'X')) # 5
    for i in range(len(s)):
        print()
        draw_board(s[i][0])
        print("check_win(s", i, ")=", check_win(s[i][0]), " [",
                                      check_win(s[i][0]) == s[i][1], "]", sep='')
    
    # проверка функци build_tree()
    steps, tree = build_tree()
    fill_tree(steps, tree)

if __name__ == '__main__':
    #unit_tests()
    main(board)

