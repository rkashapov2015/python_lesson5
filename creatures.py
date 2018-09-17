

class Creature:
    name = ''
    weight = 0
    type_creature = 'Существо'
    voice = 'Liar, lawyer, mirror, show me. What\'s the difference?'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def set_name(self, name):
        self.name = name
    
    def set_weight(self, weight):
        self.weight = weight
    
    def feed(self):
        print('покормить')

    def getVoice(self):
        print(self.voice)

    def getParents(self):
        return type(self).__bases__
    
    def pinch(self):
        pass


class Bird(Creature):
    type_creature = 'Птица'

    def get_egg(self):
        print('Сбор яиц')


class Chicken(Bird):
    voice = 'Ko ko ko'
    type_creature = 'Курица'

    def get_egg(self):
        print('Сбор куриных яиц')


class Duck(Bird):
    voice = 'Wat wat wat'
    type_creature = 'Утка'

    def get_egg(self):
        print('Сбор утиных яиц')
    

class Goose(Bird):
    voice = 'Gooooooosebumps'
    type_creature = 'Гусь'

    def pinch(self):
        print('Ущипнуть за бок')

    def get_egg(self):
        print('Сбор гусиных яиц')


class Livestock(Creature):
    voice = 'So who are you to wave your finger?'

    def shear(self):
        pass


class LivestockMilk(Livestock):

    def milk(self):
        print('Подоить')


class Cow(LivestockMilk):
    voice = 'Muuuuuu'
    type_creature = 'Корова'

    def milk(self):
        print('Доим корову')


class Goat(LivestockMilk):
    voice = 'Beeeee'
    type_creature = 'Коза'
    
    def milk(self):
        print('Доим козу')


class Sheep(Livestock):
    voice = 'Beeeee'
    type_creature = 'Овца'

    def shear(self):
        print('Подстричь')

