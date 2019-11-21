import random

print('Game of Rock, Paper, Scissors!')
print('\n')

playing = True

t = ['rock','paper','scissors']


while playing == True:

	player = input('Please choose Rock, Paper, or Scissors: ').lower()
	computer = random.choice(t)
	print('\n')

	while player not in t:
		player = input('That is not a valid choice. Please choose Rock, Paper, or Scissors: ')
	if player in t:
		playing = True
		if player == computer:
			print(f'computer chooses: {computer}')
			print('Tie Game!')
			print('\n')
			new_game = input('Would you like to play again, Yes or No? ').lower()
			if new_game[0] == 'y':
				playing = True
				print('\n')
			else:
				playing = False
				break

		elif player == 'rock':
			if computer == 'scissors':
				print(f'computer chooses: {computer}')
				print('Rock breaks scissors, Player Wins!')
				print('\n')
				new_game = input('Would you like to play again, Yes or No? ').lower()
				if new_game[0] == 'y':
					playing = True
					print('\n')
				else:
					playing = False
					break

			else:
				print(f'computer chooses: {computer}')
				print('Paper covers Rock, Computer Wins!')
				print('\n')
				new_game = input('Would you like to play again, Yes or No? ').lower()
				if new_game[0] == 'y':
					playing = True
					print('\n')
				else:
					playing = False
					break

		elif player == 'paper':
			if computer == 'scissors':
				print(f'computer chooses: {computer}')
				print('Scissors cut Paper, Computer Wins!')
				print('\n')
				new_game = input('Would you like to play again, Yes or No? ').lower()
				if new_game[0] == 'y':
					playing = True
					print('\n')
				else:
					playing = False
					break
			else:
				print(f'computer chooses: {computer}')
				print('Paper covers Rock, Player Wins!')
				print('\n')
				new_game = input('Would you like to play again, Yes or No? ').lower()
				if new_game[0] == 'y':
					playing = True
					print('\n')
				else:
					playing = False
					break

		elif player == 'scissors':
			if computer == 'paper':
				print(f'computer chooses: {computer}')
				print('Scissors cut Paper, Player Wins!')
				print('\n')
				new_game = input('Would you like to play again, Yes or No? ').lower()
				if new_game[0] == 'y':
					playing = True
					print('\n')
				else:
					playing = False
					break
			else:
				print(f'computer chooses: {computer}')
				print('Rock breaks Scissors, Computer Wins!')
				print('\n')
				new_game = input('Would you like to play again, Yes or No? ').lower()
				if new_game[0] == 'y':
					playing = True
					print('\n')
				else:
					playing = False
					break