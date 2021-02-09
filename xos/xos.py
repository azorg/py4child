#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Крестики нолики 3x3 в терминале
Основано на: https://github.com/g0t0wasd/python/blob/master/games/terminal_games/xos.py
"""

board = list(range(1, 10)) # 1...9

def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", end='')
        for j in range(3):
            print(" ", board[j + i*3], " |", sep='', end='')
        print()
        print("-" * 13)

def take_input(player_token):
    while True:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
        #if player_answer in range(1, 10):
            if (str(board[player_answer - 1]) not in "XO"):
                board[player_answer - 1] = player_token
                break
            else:
                print("Эта клеточка уже занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

def check_win(board):
    win_coord = ((0, 1, 2), \
                 (3, 4, 5), \
                 (6, 7, 8), \
                 (0, 3, 6), \
                 (1, 4, 7), \
                 (2, 5, 8), \
                 (0, 4, 8), \
                 (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
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
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)

if __name__ == '__main__':
    main(board)

