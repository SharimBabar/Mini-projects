class Robot:
    def __init__(self, name, weight):
        self.name=name
        self.weight=weight
    def introduce (self):
        return 'My name is '+self.name
    def serve_human(self, drink='coffee'):
        return self.name +' has arrived with '+ drink
class AI:
    def __init__(self, chip):
        self.chip=chip
    def ai_level(self):
        return str(self.chip) + ' Level'

class Terminator(Robot, AI):
    def __init__(self, name, weight, chip, weapons):
        Robot.__init__(self,name,weight)
        AI.__init__(self, chip)
        # whatever instant we are using has been passed the dancer class
        self.weapons=weapons

    def attack(self):
        return self.name +  ' is trying to kill Sarah conner with '+ self.weapons

#
Arny=Terminator('Arny', 200, 5, 'MP5')
# Arny=Terminator('Arny',1800,'MG6')

print(Arny.attack())
print(Arny.ai_level())