# -*- coding: utf-8 -*-
"""Copy of Housie ticket generator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U6CmM-AYcOOkBteqOzOLsGRDz_la2A5H
"""

import numpy as np
import random
from tabulate import tabulate

def get_HousieTickets():
  # Create a 2D array[3x9] of 0s
  ticket_array = np.zeros((3, 9), dtype=int)

  # Creating list of indices of each row seperately
  firstrow_indices = [(0, j) for j in range(9)]
  secondrow_indices = [(1, j) for j in range(9)]
  thirdrow_indices = [(2, j) for j in range(9)]
  #print(firstrow_indices)

  # Generating 15 random indices satisfying the rules of housie
  random_indices = []
  first_row = random.sample(firstrow_indices, 5)
  second_row = random.sample(secondrow_indices, 5)
  #print(first_row)
  #print(second_row)
  for i in first_row:
      random_indices.append(i)

  for i in second_row:
      random_indices.append(i)
  #Below block of code is to satisfy the condition that each column must have atleast one number
  for i in range(9):
    if (0,i) not in random_indices:
      if (1,i) not in random_indices:
        random_indices.append((2,i))
        thirdrow_indices.remove((2,i))
  third_row = random.sample(thirdrow_indices, 15-len(random_indices))
  for i in third_row:
      random_indices.append(i)

  # Filling these random indices with random numbers satisfying the rules of housie
  firstcolumn = list(range(1,9)) # list of numbers from 1 to 9
  secondcolumn = list(range(10,19))
  thirdcolumn = list(range(20,29))
  fourthcolumn = list(range(30,39))
  fifthcolumn = list(range(40,49))
  sixthcolumn = list(range(50,59))
  seventhcolumn = list(range(60,69))
  eighthcolumn = list(range(70,79))
  ninthcolumn = list(range(80,90))
  for idx in random_indices:
      if idx[1] == 0:
          number = random.choice(firstcolumn)
          ticket_array[idx] = number
          firstcolumn.remove(number)
      elif idx[1] == 1:
          number = random.choice(secondcolumn)
          ticket_array[idx] = number
          secondcolumn.remove(number)
      elif idx[1] == 2:
          number = random.choice(thirdcolumn)
          ticket_array[idx] = number
          thirdcolumn.remove(number)
      elif idx[1] == 3:
          number = random.choice(fourthcolumn)
          ticket_array[idx] = number
          fourthcolumn.remove(number)
      elif idx[1] == 4:
          number = random.choice(fifthcolumn)
          ticket_array[idx] = number
          fifthcolumn.remove(number)
      elif idx[1] == 5:
          number = random.choice(sixthcolumn)
          ticket_array[idx] = number
          sixthcolumn.remove(number)
      elif idx[1] == 6:
          number = random.choice(seventhcolumn)
          ticket_array[idx] = number
          seventhcolumn.remove(number)
      elif idx[1] == 7:
          number = random.choice(eighthcolumn)
          ticket_array[idx] = number
          eighthcolumn.remove(number)
      elif idx[1] == 8:
          number = random.choice(ninthcolumn)
          ticket_array[idx] = number
          ninthcolumn.remove(number)
  # To sort the numbers present in every column
  for col in range(9):

    # if all the rows are filled with a random number

      if(ticket_array[0][col] != 0 and ticket_array[1][col] != 0 and ticket_array[2][col] != 0):
          l = [ticket_array[0][col],ticket_array[1][col],ticket_array[2][col]]
          l.sort()
          ticket_array[0][col] = l[0]
          ticket_array[1][col] = l[1]
          ticket_array[2][col] = l[2]

    # if 1st and 2nd row are filled by random number

      elif(ticket_array[0][col] != 0 and ticket_array[1][col] != 0 and ticket_array[2][col] == 0):
          if ticket_array[0][col] > ticket_array[1][col]:
              temp = ticket_array[0][col]
              ticket_array[0][col] = ticket_array[1][col]
              ticket_array[1][col] = temp


    # if 1st and 3rd row are filled by random number

      elif(ticket_array[0][col] != 0 and ticket_array[2][col] != 0 and ticket_array[1][col] == 0):
          if ticket_array[0][col] > ticket_array[2][col]:
              temp = ticket_array[0][col]
              ticket_array[0][col] = ticket_array[2][col]
              ticket_array[2][col] = temp

    # if 2nd and 3rd rows are filled with random numbers

      elif(ticket_array[0][col] == 0 and ticket_array[1][col] != 0 and ticket_array[2][col] != 0):
          if ticket_array[1][col] > ticket_array[2][col]:
              temp = ticket_array[1][col]
              ticket_array[1][col] = ticket_array[2][col]
              ticket_array[2][col] = temp
  return ticket_array
#Take number of tickets from user as input
numberOfTickets = int(input("Enter no. of tickets you need : "))
tickets = []

for i in range(int(numberOfTickets)):
       ticket = get_HousieTickets()
       tickets.append(ticket)

for ticket in tickets:
      print(tabulate(ticket, tablefmt="fancy_grid", numalign="center"))