class paint(object):

    def __init__(self, obj):
        l = []
        print('Now we can print')
        self.lenght = len(obj)
        for i in obj:
            l.append(int(i))

        print(self.lenght)
        print(l)

    def sqare(self, l):
        r = '#' * l[0]
        for i in range(l[0]):
            print(r)

print('Take some numbers: ')
# user_input = input().split()
user_input = '1'.split()
if len(user_input) == 1:
    paint.sqare(user_input)
