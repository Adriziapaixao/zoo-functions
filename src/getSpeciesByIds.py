from zoo_data import data

def get_species_by_ids(*ids):
    if not ids:
        return []

    return [species for species in data['species'] if species['id'] in ids]

print(get_species_by_ids('0938aa23-f153-4937-9f88-4858b24d6bce'))
print(get_species_by_ids())
print(get_species_by_ids('baa6e93a-f295-44e7-8f70-2bcdc6f6948d', 'ef3778eb-2844-4c7c-b66c-f432073e1c6b'))