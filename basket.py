class Basket(object):
    def __init__(self, space):
        self.space = space

    def space_basket(self, trash):
        if self.space - trash.size >= 0:
            print('OK!')
            self.space -= trash.size
        else:
            print('No space left!')


class pkg(Basket):

    def space_pkg(self, trash):
        if self.space - trash.size >= 0:
            print('OK!')
            self.space -= trash.size
        else:
            print('No space left!')

class Bottle(object):
    size = 1

    def __init__(self, mater):
        self.material = mater

class other_trash(Bottle):
    size = 0,5

print('What space of basket?')
user_basket = int(input())
print('What space of pkg?')
user_pkg = int(input())
print('How many bottles?')
user_bottles = int(input())
print('How many other trash?')
user_trash = int(input())

basket = Basket(user_basket)
packages = pkg(user_pkg)

for i in range(user_bottles):
    bottle = Bottle('plastic')
    basket.space_basket(bottle)