from random import randint

options = ['Rock', 'Paper', 'Scissors']

computer = options[randint(0,2)]
player = False

while player == False:
    player = input('Rock, Paper, Scissors ? ')
    if player == computer:
       print('Tie!')
    elif player == 'Rock':
        if computer == 'Paper':
           print("You lose!", computer, 'covers', player)
        else:
           print('You Win!', player, 'crush', computer )    
    elif player == 'Scissors':
         if computer == 'Rock':
           print('You Lose!', computer, 'crush', player)
         else:
           print('You Win!', player, 'cut', computer)    
    elif player == 'Paper':
         if computer == 'Scissors':
           print('You Lose!', computer, 'cut', player)
         else:
           print('You Win!', player, 'covers', computer)    
    else:
        print("That's not a valid play. Check your spelling!")

player = False
computer = options[randint(0,2)]
