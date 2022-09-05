""" Ronald W. Sudol III """
'''IT140 Text Game Project: Robo Hobo vs Deputy Dawg'''
'''2/20/2022'''

rooms = {
        'Train Tracks': {'east': 'Strip Mall Parking Lot'},
        'Strip Mall Parking Lot': {'west': 'Train Tracks', 'north': 'Burger Bobs', 'east': 'PD Entrance',
                                   'south': 'Easy Petes', 'search': 'Oil Can'},
        'Burger Bobs': {'south': 'Strip Mall Parking Lot', 'east': 'Bobs Dumpster',
                        'search': 'Handful of Ketchup Packtets'},
        'Bobs Dumpster': {'west': 'Burger Bobs', 'search': 'Rubiks Cube'},
        'Easy Petes': {'north': 'Strip Mall Parking Lot', 'east': 'Petes Dumpster', 'search': 'Pool Ball'},
        'Petes Dumpster': {'west': 'Easy Petes', 'search': 'XXX Jug'},
        'PD Entrance': {'west': 'Strip Mall Parking Lot', 'north': 'Cop Castle', 'search': 'Sock'}
    }

current_room = 'Train Tracks'
inventory = []


def player_status():
    print('\n')
    print('~' * 40)
    print('Your current location is : {}'.format(current_room))
    print('-' * 40)
    print('Inventory: {}'.format(inventory))
    print('You have {} more items to find'.format(6 - len(inventory)))
    print('-' * 40)


def loot():
    if current_room == 'Train Tracks':
        print('!' * 40)
        print('No item to be found here\n LOOK SOMEWHERE ELSE')
        print('!' * 40)
    elif room_list[direction.lower()] in inventory:
        print('!' * 40)
        print('You already got that!!\n LOOK SOMEWHERE ELSE')
        print('!' * 40)
    else:
        inventory.append(room_list[direction.lower()])
        print('!' * 40)
        print('Congrats! You found a {}'.format(room_list[direction.lower()]))
        print('Certainly that will be useful...')
        print('!' * 40)


print('#' * 40)
print('Your name is Robo Hobo\n'
      ' and you have awoken next to the Train Tracks\n'
      ' with an insatiable thirst for malt liquor \n '
      'and VENGEANCE!\n'
      'Gather your gear before finding Deputy Dawg,\n'
      'and then RIP AND TEAR! ...until it is done!')
print('#' * 40)


while current_room != 'Cop Castle':
    player_status()
    available = []
    room_list = rooms[current_room]
    for key in room_list:
        available.append(key)
    print('Available Commands: {}'.format(available))
    direction = input('Enter a Direction or Search')

    if direction.lower() == 'search':
        loot()
    elif direction.lower() == 'exit':
        print('\n')
        print('^' * 40)
        print('Thanks for playing!\n Dont let the door hit ya!')
        print('^' * 40)
        break
    elif direction.lower() in room_list:
        current_room = room_list[direction.lower()]

    else:
        print('!' * 40)
        print('Invalid Input\n Try picking a different direction!\n '
              'Or maybe Search for an item?\n'
              'Your options are Search, North, South, East, or West')
        print('!' * 40)

if current_room == 'Cop Castle':
    if len(inventory) == 6:
        print('\n')
        print('@!$#'*10)
        print('Congratulations! You found the Cop Castle! \n '
              'This is particularly impressive \n considering you didnt have a map!\n'
              'You creep up quietly behind Deputy Dawg,\n'
              'who appears to be on a smoke break,\n'
              'and swing your inventory full of treasures\n'
              'with all your might. You land a crushing blow\n'
              'to that back of Deputy Dawgs head, killing him instantly.\n'
              'That will teach him to share his Jelly Doughnuts...\n'
              'As you sit, enjoying the fallen deputys tastey treats, \n'
              'a shadow begins to loom over you and at once you realize..\n'
              'You forgot all about the Sheriff!!!\n'
              '\n'
              'To Be Continued...?')
        print('-' * 40)
    else:
        print('!'*40)
        print('You FOOL!\n'
              'You have wandered into Deputy Dawgs lair without \n'
              'your inventory of treasures! Without these you lack\n'
              'the strength to take on Deputy Dawg! \n '
              'I mean, you barely even put up a fight...\n'
              'You are but a stain on the pavement now...\n'
              '\n'
              'You lose!\n'
              '\n'
              'loser...')
