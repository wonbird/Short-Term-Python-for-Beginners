# define class
class Night:
    level = 1
    life = 10

    def __init__(self, name):
        self.name = name

    def attack(self):
        print('Yap!')
        self.life -= 1

    def check_life(self):
        if self.life <= 0:
            print('나 ' + self.name + ', 너와 함께 한 시간 모두 눈부셨다. 이 불멸의 저주를 끝내고 무로 돌아간다.')
        else:
            print('나 ' + self.name + ', 생명이 ' + str(self.life) + ' 남았다. 죽음이 나에게로 걸어온다.')

# create instances
night1 = Night('김신')
night2 = Night('무신')

# instance run methods
night1.attack()
night2.attack()
night2.attack()
night1.check_life()
night2.check_life()
