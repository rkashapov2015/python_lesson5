from Main import Main

listCreatures = [
    {'name': 'Серый', 'weight': 10, 'className': 'Goose'},
    {'name': 'Белый', 'weight': 13, 'className': 'Goose'},
    {'name': 'Манька', 'weight': 203, 'className': 'Cow'},
    {'name': 'Барашек', 'weight': 130, 'className': 'Sheep'},
    {'name': 'Кудрявый', 'weight': 129, 'className': 'Sheep'},
    {'name': 'Ко-ко', 'weight': 4, 'className': 'Chicken'},
    {'name': 'Кукареку', 'weight': 4, 'className': 'Chicken'},
    {'name': 'Рога', 'weight': 50, 'className': 'Goat'},
    {'name': 'Копыта', 'weight': 41, 'className': 'Goat'},
    {'name': 'Кряква', 'weight': 20, 'className': 'Duck'}
]

main = Main(listCreatures)

main.run()