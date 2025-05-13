from zoo_data import data

def get_employee_by_name(employee_name):
    if not employee_name:
        return []

    for employee in data['employees']:
        if employee['firstName'] == employee_name or employee['lastName'] == employee_name:
            return [employee]

    else:
        return []

print(get_employee_by_name('Wilburn'))
print(get_employee_by_name(''))
