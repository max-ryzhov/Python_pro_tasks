class Tanks:
    game = 'Tanks'
    slogan = 'Fuck them all'

    # def __init__(self, team, armor, strike_power):
    #     self.team = team
    #     self.armor = armor
    #     self.strike_power = strike_power

#    def manual_set(self, team, armor, strike_power):
    def manual_set():
        return print('calling manual_set')


print(Tanks.manual_set())
t_34 = Tanks()
t_34.team = 1
t_34.armor = 2
t_34.strike_power = 3

print(t_34.__dict__)
print(Tanks.__dict__)

