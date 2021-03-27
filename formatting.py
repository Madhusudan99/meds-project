def text_to_num(text):
    fq_words = {
        'one': '1',
        'two': '2', 
        'three': '3', 
        'four': '4', 
        'five': '5'
        }
    elements = text.lower().split()
    for idx, element in enumerate(elements):
        if element in fq_words.keys():
            elements[idx] = fq_words[element]
    return elements

def format(text):
    elements = text_to_num(text=text)
    drugs = ['paracetamol', 'azithromicine', 'hydroxychloroquine']
    frequency = ['1', '2', '3', '4', '5']
    days_week = ['days', 'week', 'weeks']
    medicine_dict = {}
    for idx, element in enumerate(elements):
        if element in drugs:
            medicine_dict['Drug'] = element
        if element == 'times':
            medicine_dict['Frequency/Day'] = elements[idx-1]
        if element in days_week:
            medicine_dict['Days of dosage'] = elements[idx-1]
            medicine_dict['Quantity of meds'] = int(medicine_dict['Days of dosage']) * int(medicine_dict['Frequency/Day'])
    result = f"Drug: {medicine_dict['Drug']}\nFrequency/Day: {medicine_dict['Frequency/Day']}\nDays of dosage: {medicine_dict['Days of dosage']}\nQuantity of meds: {medicine_dict['Quantity of meds']}"
    return result

if __name__ == '__main__':
    text = "Paracetamol two times a day for two days"
    print(format(text))