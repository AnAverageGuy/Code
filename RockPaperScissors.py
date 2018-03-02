#!/bin/python3
# Program written by Joshua Martinez

from random import randint

playerScore = 0
cpuScore = 0
while True:
  print('Current score: ', playerScore, '-', cpuScore)
  player = input('Rock, Paper, Scissors!')
  if player.lower() == "exit":
    print('Thanks for playing!')
    break
  cpu = randint(1,3)
  
# 1 - rock, 2 - paper, 3 - scissors
  if player.lower() == "rock" and cpu == 1:
    print('Tie!')
  elif player.lower() == "rock" and cpu == 2:
    print('Computer Wins!')
    cpuScore += 1
  elif player.lower() == "rock" and cpu == 3:
    print('Player Wins!')
    playerScore += 1
  elif player.lower() == "paper" and cpu == 1:
    print('Player Wins!')
    playerScore += 1
  elif player.lower() == "paper" and cpu == 2:
    print('Tie!')
  elif player.lower() == "paper" and cpu == 3:
    print('Computer Wins!')
    cpuScore += 1
  elif player.lower() == "scissors" and cpu == 1:
    print('Computer Wins!')
    cpuScore += 1
  elif player.lower() == "scissors" and cpu == 2:
    print('Player Wins!')
    playerScore += 1
  elif player.lower() == "scissors" and cpu == 3:
    print('Tie!')
  else:
    print('Sorry I don\'t understand you\n')
    continue
  print()
  
  if cpu == 1:
    print('Computer picks Rock!')
  elif cpu == 2:
    print('Computer picks Paper!')
  elif cpu == 3:
    print('Computer picks Scissors!')  