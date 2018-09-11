class Creature:
    name = ''
    weight = 0
    typeCreature = 'Существо'
    voice = 'Liar, lawyer, mirror, show me. What\'s the difference?'
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def setName(self, name):
        self.name = name
    
    def setWeight(self, weight):
        self.weight = weight
    
    def feed(self):
        print('покормить')

    def getVoice(self):
        print(self.voice)

    def getParents(self):
        return type(self).__bases__

class Bird(Creature):
    typeCreature = 'Птица'
    def getEgg(self):
        print('Сбор яиц')

class Chicken(Bird):
    voice = 'Ko ko ko'
    typeCreature = 'Курица'

class Duck(Bird):
    voice = 'Wat wat wat'
    typeCreature = 'Утка'
    
class Goose(Bird):
    voice = 'Gooooooosebumps'
    typeCreature = 'Гусь'

    def pinch(self):
        print('Ущипнуть за бок')

class Livestock(Creature):
    voice = 'So who are you to wave your finger?'

class LivestockMilk(Livestock):
    def milk(self):
        print('Подоить')

class Cow(LivestockMilk):
    voice = 'Muuuuuu'
    typeCreature = 'Корова'

class Goat(LivestockMilk):
    voice = 'Beeeee'
    typeCreature = 'Коза'

class Sheep(Livestock):
    voice = 'Beeeee'
    typeCreature = 'Овца'

    def shear(self):
        print('Подстричь')
