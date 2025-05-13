from zoo_data import data

def get_oldest_from_first_species(employee_id):
    employee = next((emp for emp in data['employees'] if emp['id'] == employee_id), None)
    if not employee:
        return []

    first_species_id = employee['responsibleFor'][0]

    species = next((spec for spec in data['species'] if spec['id'] == first_species_id), None)
    if not species:
        return []

    oldest_animal = max(species['residents'], key=lambda animal: animal['age'])

    return [oldest_animal['name'], oldest_animal['sex'], oldest_animal['age']]


print(get_oldest_from_first_species('4b40a139-d4dc-4f09-822d-ec25e819a5ad'))
print(get_oldest_from_first_species('56d43ba3-a5a7-40f6-8dd7-cbb05082383f'))
print(get_oldest_from_first_species(''))