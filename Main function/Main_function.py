def say_hello(name):
    print('Hello there, ' + '{}'.format(name))
print('Hi again')

def main():
    print('Hello World! ' + __name__)

if __name__ == '__main__':
    main()
else:
    print('This isn\'t the original file!')
