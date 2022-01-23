from zoo.animals import ANIMALS

if __name__ == '__main__':
    try:
        while True:
            ANIMALS['wolf'].moon()
            actions_available = ', '.join(list(ANIMALS.keys())+['exit'])
            print(f'available actions: {actions_available}')
            print('choose one: ')
            action = input().strip().lower()

            if action == 'exit':
                print('Bye-bye!')
                exit()

            if action not in ANIMALS:
                print(f'Sorry, {action} is not available...')
                print()
                continue

            ANIMALS[action].make_sound()
            print()
    except KeyboardInterrupt:
        print('Bye-bye!')
        exit()
