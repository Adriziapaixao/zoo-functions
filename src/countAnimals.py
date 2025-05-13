from zoo_data import data
def count_animals(animal=None):
    if animal is None:
        return {species['name']: len(species['residents']) for species in data['species']}

    specie_name = animal.get('specie')
    species = next((s for s in data['species'] if s["name"] == specie_name), None)

    if not species:
        return 0

    if 'sex' in animal:
        return len([resident for resident in species['residents'] if resident['sex'] == animal['sex']])
    return len(species['residents'])

print(count_animals())
print(count_animals({'specie': 'giraffes'}))
print(count_animals({'specie': 'penguins', 'sex': "female"}))