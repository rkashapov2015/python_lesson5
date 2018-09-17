

class Creature:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.type_creature = 'Существо'
        self.voice = 'Liar, lawyer, mirror, show me. What\'s the difference?'

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, weight):
        self.__weight = weight
    
    def feed(self):
        print('покормить')

    def get_voice(self):
        print(self.voice)

    def get_parents(self):
        return type(self).__bases__
    
    def pinch(self):
        pass


class Bird(Creature):

    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.type_creature = 'Птица'

    def get_egg(self):
        print('Сбор яиц')


class Chicken(Bird):
    
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'Ko ko ko'
        self.type_creature = 'Курица'
        
    def get_egg(self):
        print('Сбор куриных яиц')


class Duck(Bird):

    def __init__(self, name, weight):    
        super().__init__(name, weight)
        self.voice = 'Wat wat wat'
        self.type_creature = 'Утка'
        
    def get_egg(self):
        print('Сбор утиных яиц')
    

class Goose(Bird):
    
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'Gooooooosebumps'
        self.type_creature = 'Гусь'

    def pinch(self):
        print('Ущипнуть за бок')

    def get_egg(self):
        print('Сбор гусиных яиц')


class Livestock(Creature):
    
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'So who are you to wave your finger?'

    def shear(self):
        pass


class LivestockMilk(Livestock):

    def milk(self):
        print('Подоить')


class Cow(LivestockMilk):
    
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'Muuuuuu'
        self.type_creature = 'Корова'

    def milk(self):
        print('Доим корову')


class Goat(LivestockMilk):

    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'Beeeee'
        self.type_creature = 'Коза'
    
    def milk(self):
        print('Доим козу')


class Sheep(Livestock):

    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'Beeeee'
        self.type_creature = 'Овца'

    def shear(self):
        print('Подстричь')

