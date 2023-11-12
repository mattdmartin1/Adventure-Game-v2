# Start a new game
# Create adventure game 
# Turn game on. Would you like to play
name = input('Please enter your name: ')
print('Welcome', name, 'to this adventure game')

answer = input('Would you like to play the adventure game? Y or N: ').lower()

if answer == 'y':
    answer = input('You are walking along a path and you have come to a river crossing. \n'
                   'Would you like to take the bridge or go by boat?: Enter bridge or boat: ').lower()
    
    if answer == 'bridge':
        answer = input('You have now walked across the river and have made it to the jungle. \n'
                       'You can either tarzan across the tree line on rope or walk through the jungle: Enter rope or walk: ').lower()
        if answer == 'rope':
            answer = input('Good choice. You avoided the jaguars. Now you have gotten past the jungle and reached the desert. \n'
                           'Would you like to radio in help or run 5 miles to the end. Enter radio or run: ').lower()
            if answer == 'radio':
                print('Luckily a helicopter came to your rescue and flew you to safety. You have won the adventure game!! ')
            elif answer == 'run':
                print('You ran 3 miles and got too dehydrated from the extreme heat. End game. ')
                
        elif answer == 'walk':
            print('A jaguar snuck up behind you while walking and killed you. End Game. ')
            
    elif answer == 'boat':
        print('Your boat was poorly made and you sunk and died crossing the river. End game. ')
        
else:
    print('Please retry again. ')
        
        
    