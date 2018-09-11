from Creatures import *

class Main:
    creatures = []
    commonwWeight = 0
    maxWeightValue = 0
    maxWeightName = ''
    def __init__(self, listCreatures):
        for element in listCreatures:
            get_class = globals()[element['className']]
            creatureObject = get_class(element['name'], element['weight'])
            self.creatures.append(creatureObject)
        

    def run(self):
        for creature in self.creatures:
            print(creature.typeCreature, creature.name, creature.weight, 'кг')
            if creature.weight > self.maxWeightValue:
                self.maxWeightValue = creature.weight
                self.maxWeightName = creature.typeCreature

            self.commonwWeight += creature.weight
            creature.getVoice()

            creature.feed()

            if LivestockMilk in creature.getParents():
                creature.milk()

            if type(creature) is Sheep:
                creature.shear()

            if Bird in creature.getParents():
                creature.getEgg()
            
            if type(creature) is Goose:
                creature.pinch()
            
            print('---------------')
            
        print(f'Общий вес составил {self.commonwWeight} кг')
        print(f'Самое тяжелое животное это {self.maxWeightName}')