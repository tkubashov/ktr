def double(arg):
    print ('Before:', arg)
    arg = arg * 2
    print('After', arg)
number = 5
double(number)
print(number)

def change(args):
    print('Before', args)
    args.append('More data')
    print('After', args)

numbers = [10,5,6]
change(numbers)
print(numbers)