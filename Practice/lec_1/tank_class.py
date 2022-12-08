class Tanks:
    # def __init__(self, team, armor, strike_power):
    #     self.team = team
    #     self.armor = armor
    #     self.strike_power = strike_power
    team = 'def_team'
    armor = 'def_arm'
    strike_power = 'def_power'

    # def move(self, coord_x, coord_y):
    #     print(f'tank has moved on {coord_x}, {coord_y}')
    #
    # def shoot(self, coord_x, coord_y):
    #     print(f'tank has shoot at {coord_x}, {coord_y}')
    #
    # def damage(self, damage):
    #     print(f'tank has damage {damage}')


print(f"dict класса Tanks по умолчанию {Tanks.__dict__}")
Tanks.cool = 'not_cool'    # добавил атрибут и записал деф.значение
setattr(Tanks, 'setattr', 'new_attr')    # добавил атрибут и записал деф.значение сетом
print(f"добавил атрибуты в класс Tanks {Tanks.__dict__}")

Tanks.team = 'green'    # переписал значение атрибута
Tanks.armor = 777    # переписал значение атрибута
setattr(Tanks, 'strike_power', '999')    # переписал значение атрибута сетом
print(f"перезаписал значение атрибутов класса Tanks {Tanks.__dict__}")
print(Tanks.team, Tanks.armor, Tanks.strike_power, Tanks.cool, Tanks.setattr)

print(getattr(Tanks, 'armor'))
print(getattr(Tanks, 'ass', 'undefined'))
print()

t_34 = Tanks()
t_72 = Tanks()

print(f"дефолтный t_72: team = {t_72.team}, armor = {t_72.armor},  strike = {t_72.strike_power}, cool = {t_72.cool}")

t_34.team = 'red'
t_34.armor = 10
t_34.strike_power = 1
t_34.pokemon = 'pikachu'

print('броня t_72 - ', getattr(t_72, 'armor'))
print('жопа t_72 - ', getattr(t_72, 'ass', 'атрибут отсутствует'))

print(f"забитый t_34: team = {t_34.team}, armor = {t_34.armor},  strike = {t_34.strike_power}, symbol = {t_34.pokemon}")
print()
print(f"атрибуты t_34 {t_34}, {id(t_34)}, {t_34.__dict__}")
print(f"атрибуты t_72 {t_72}, {id(t_72)}, {t_72.__dict__}")
print()
print(f"итоговый dict класса {Tanks.__dict__}")
print(f"атрибуты объекта t_34 'symbol' и перезаписанные значения атрибутов не повлияли на словарь класса")
# t_34 = Tanks('red', 10, 1)
# t_34.move(5, 10)
# t_34.shoot(7, 9)
# t_34.damage(10)
