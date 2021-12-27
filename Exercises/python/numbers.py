
class Circle():
    pi = 3.142
    def __init__(self,radius=1):
        self.r = radius

    def area(self):
        return self.r * self.r * Circle.pi

# myc = Circle(3)
# print(myc.r)
# print(myc.area())

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

cards_pack = [(s,r) for s in SUITE for r in RANKS]

new = cards_pack.pop()
new2 = cards_pack.pop()

# print(len(cards_pack))
# print(cards_pack)
print(new[1],new2[1])
if new[1] < new2[1]:
    print('yes')

else:
    print('no')
