from data import zoo_data

def get_employee_by_name(employee_name):
    if not employee_name:
        return []

    for employee in zoo_data['employee']:
        if employee['firstName'] == employee_name:
            return [employee]
        elif employee['lastName'] == employee_name:
            return [employee]

    else:
        return []

print(get_employee_by_name('Stephanie'))