user_input = 'x'
print('type help for options')
while user_input != 'quit':
    user_input = input('>')
    if user_input == 'help':
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
    elif user_input == 'start':
        print('car started... ready to go ')
    elif user_input == 'stop':
        print('car stopped')
    elif user_input == 'quit':
        break
    else:
        print("I don't understand that...")