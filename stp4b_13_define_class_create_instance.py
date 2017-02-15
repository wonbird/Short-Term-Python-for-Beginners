# define class
class Hero:
    level = 1

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def level_up(self):
        self.level += 1
        print('<' + self.name + '의 레벨이 ' + str(self.level) + '으로 업그레이드 되었음>')

    def say_hello(self):
        print('내 이름은 ' + self.name + '. 나는 ' + self.__class__.__name__ + '이다.')
        print('현재 레벨은 ' + str(self.level) + '이다.')

    def attack(self):
        pass


class Knight(Hero):
    def __init__(self, name, sex, country):
        Hero.__init__(self, name, sex)
        self.country = country

    def attack(self):
        print('내 칼을 받아라!')


class Wizard(Hero):
    def __init__(self, name, sex, totem):
        Hero.__init__(self, name, sex)
        self.totem = totem

    def attack(self):
        print('마법의 주문으로 공격!')


# create instances
tom = Knight('Tom', 'M', 'Wonderland')
jane = Wizard('Jane', 'F', 'Wolf')

# instance run methods
tom.say_hello()
tom.attack()
tom.level_up()
tom.attack()
tom.level_up()
tom.attack()
tom.level_up()
jane.say_hello()
tom.say_hello()
