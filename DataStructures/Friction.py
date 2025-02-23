def GCD(n1, n2, ):
    b, l = (n2, n1) if n2 > n1 else (n1, n2)
    while l:
        b , l = l , b%l
    return b
class Friction:

    def __init__(self,bolen,bolunen):
        self.bolen = bolen
        self.bolunen = bolunen
    def show(self):
        print(f"{self.bolen}/{self.bolunen}")
    def __add__(self, other_fr):
        new_bolen = self.bolen * other_fr.bolunen + self.bolunen * other_fr.bolen
        new_bolunen = self.bolunen * other_fr.bolunen
        return Friction(new_bolen,new_bolunen)
    def __eq__(self, other):
        return self.bolen * other.bolunen == self.bolunen * other.bolen
    def get_num (self):
        return self.bolen
    def get_den(self):
        return self.bolunen



print(GCD(35,21))

myfr = Friction(3,5)
myfr.show()
f2 = Friction(4,8)
myfr.__add__(f2).show()
