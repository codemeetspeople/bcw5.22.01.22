if __name__ == '__main__':
    x, y = 10, 20

    params = {
        'first': x,
        'second': y,
        'result': x + y
    }

    print('%d + %d = %d' % (x, y, x + y))
    print('%(first)d + %(second)d = %(result)d' % {'first': x, 'second': y, 'result': x+y})
    print('%(first)d + %(second)d = %(result)d' % params)
    print('{} + {} = {}'.format(x, y, x + y))
    print('{first} + {second} = {result}'.format(first=x, second=y, result=x+y))
    print('{first} + {second} = {result}'.format(**params))
    print('{0} + {1} = {2}'.format(x, y, x + y))
    print('{1} + {0} = {2}'.format(x, y, x + y))
    print(f'{x} + {y} = {x+y}')

