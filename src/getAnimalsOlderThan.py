from zoo_data import data

def get_animals_older_than(species_name, min_age):
    for species in data['species']:
        if species['name'] == species_name:
            return all(resident['age'] >= min_age for resident in species['residents'])
    return False

print(get_animals_older_than('lions', 6))
print(get_animals_older_than('tigers', 18))
