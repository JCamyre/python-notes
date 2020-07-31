# a literally forgot the word for parameters, yikes, pass arguments


def greeting(name, greeting='Hello my name is '):
    print(greeting + name + '.')


greeting('Joseph')
greeting('Joseph', 'Hi my name is ')
greeting(greeting='Greetings my name is ', name='Charles')
greeting('Joseph', greeting='Hi my name is ')


def greeting_(*name):
    print(name)

    for x in name:
        print('Hi my name is ' + x + '.')


greeting_('Joseph', 'John')


hello1 = lambda: print('I didn\'t know you could use numbers in variable names')


hello1()
