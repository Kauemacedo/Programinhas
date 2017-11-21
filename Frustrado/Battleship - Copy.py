from random import randint
import os
import sys
import pygame

pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

ocean = pygame.image.load("ocean.jpg").convert()
oceanradar = pygame.image.load("oceanradar.bmp").convert()
screen.blit(ocean, (0, 0))
pygame.display.update()
screen.blit(oceanradar, (0, 0))
pygame.display.update()
pygame.mouse.set_cursor(*pygame.cursors.broken_x)
button = pygame.image.load("button.jpg")
b = screen.blit(button, (300, 200))

    


print ("Bem vindo a Batalha Naval!")
board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print ((" ").join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ("você tem 12 tentativas!")
for turn in range(12):
  print ("Turno", turn + 1)
  while True:
    try:
      guess_row = int(input("Linha: ")) - 1
      break
    except ValueError:
      print ("Tu é doido? Tem que colocar um número inteiro!")
  while True:
    try:
      guess_col = int(input("Coluna: ")) -1
      break
    except ValueError:
      print ("Tu é doido? Tem que colocar um número inteiro!")
  
  if guess_row == ship_row and guess_col == ship_col:
    print ("Parabéns!! Tu chitou?")
    venceu = input("Aperte enter para encerrar")
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      os.system('cls')
      print ("Tão ruim que nem no oceano tu acertou... o oceano tem o tamanho de 5x5")
    elif board[guess_row][guess_col] == "X":
      os.system('cls')
      print( "Seu peixe desmiolado, atirou no mesmo lugar... perdeu um turno" )
    else:
      os.system('cls')
      print ("Eeeeeeerrrou!")
      board[guess_row][guess_col] = "X"   
    if (turn == 11):
      print ('PERDEU! OLHE ABAIXO QUANTOS TIROS ERRADOS! O BARCO ESTA BEM ALI OH')
      board[ship_row][ship_col] = "I"
      print_board(board)
      print ("Tu perdeu, não adianta chorar...")
      end = input("aperte enter para encerrar")
    print_board(board)


