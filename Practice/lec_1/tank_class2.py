class Tanks:
    # эти атрибуты в словаре класса
    game = 'Tanks'
    slogan = 'Fuck them all'

    # эти атрибуты в словаре объекта и появляются только в момент его инициализации
    def __init__(self, team, armor, strike_power):
        self.team = team
        self.armor = armor
        self.strike_power = strike_power

    # метод экземпляра класса Tanks
    def get_characteristic(self, characteristic):
        res = 'undefined'
        if characteristic == 'team':
            res = self.team
        elif characteristic == 'armor':
            res = self.armor
        elif characteristic == 'strike_power':
            res = self.strike_power
        return res


print(Tanks.__dict__)

t34 = Tanks(1, 20, 3)
print(t34.__dict__)

print(hasattr(t34, 'speed'))
setattr(t34, 'speed', '30')
print(hasattr(t34, 'speed'))
print(getattr(t34, 'game'))    # значение атрибута взято из класса

arm = getattr(t34, 'armor', 'paper')
print('armor = ', arm)

strike = t34.get_characteristic('strike_power')
print('strike_power = ', strike)
