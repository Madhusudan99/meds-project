text = "Paracetamol 2 times a day for 3 days"
#text = "Azithromicine 3 times a day for 2 days"
#text = "Hydroxychloroquine 3 times a day for 3 days"

elements = text.lower().split()

drugs = ['paracetamol', 'azithromicine', 'hydroxychloroquine']
frequency = ['1', '2', '3', '4', '5']
days_week = ['days', 'week', 'weeks']
elements = text.lower().split()
medicine_dict = {}
for idx, element in enumerate(elements):
    if element in drugs:
        medicine_dict['Drug'] = element
    if element == 'times':
        medicine_dict['Frequency/Day'] = elements[idx-1]
    if element in days_week:
        medicine_dict['Days of dosage'] = elements[idx-1]
        medicine_dict['Quantity of meds'] = int(medicine_dict['Days of dosage']) * int(medicine_dict['Frequency/Day'])

print(text)
print(f"Drug: {medicine_dict['Drug']}")
print(f"Frequency/Day: {medicine_dict['Frequency/Day']}")
print(f"Days of dosage: {medicine_dict['Days of dosage']}")
print(f"Quantity of meds: {medicine_dict['Quantity of meds']}")