from creatures import *


class Farm:
    
    def __init__(self, list_creatures):
        self.creatures = []
        self.common_weight = 0
        self.max_weight_value = 0
        self.max_weight_name = ''

        for element in list_creatures:
            creature_object = self.create_object(element['className'], element['name'], element['weight'])
            if creature_object:
                self.creatures.append(creature_object)
        
    def run(self):
        for creature in self.creatures:
            print(creature.type_creature, creature.name, creature.weight, 'кг')
            if creature.weight > self.max_weight_value:
                self.max_weight_value = creature.weight
                self.max_weight_name = creature.type_creature

            self.common_weight += creature.weight
            creature.get_voice()
            creature.feed()

            if LivestockMilk in creature.get_parents():
                creature.milk()

            if type(creature) is Sheep:
                creature.shear()

            if Bird in creature.get_parents():
                creature.get_egg()
            
            if type(creature) is Goose:
                creature.pinch()
            
            print('---------------')
            
        print(f'Общий вес составил {self.common_weight} кг')
        print(f'Самое тяжелое животное это {self.max_weight_name}')

    def create_object(self, class_name_text, name='', weight=0):
        try:
            class_name = globals()[class_name_text]
            creature_object = class_name(name, weight)
            return creature_object
        except KeyError:
            return False
