# Start a new game
# Create adventure game 
# Turn game on. Would you like to play
name = input('Please enter your name: ')
print('Welcome', name, 'to this adventure game')

answer = input('Would you like to play the adventure game? Y or N: ').lower()

if answer == 'y':
    answer = input('You are walking along a path. You come to a wide river crossing. Would you like to take the bridge or go by boat?: Enter bridge or boat ').lower
    
