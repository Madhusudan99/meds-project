import speech_recognition as sr
import sms
import formatting

class HiddenMarkovModel:
    def __init__(self):
        self.r = sr.Recognizer()
    def recognize(self, mobile_number):
        with sr.Microphone() as source:
            try:
                audio = self.r.listen(source, phrase_time_limit=6)
                predicted_string = self.r.recognize_google(audio)
                sms.send_sms(text= formatting.format(predicted_string), mobile_number=mobile_number)
                return predicted_string, formatting.format(predicted_string)
            except sr.WaitTimeoutError:
                return "Say Something....\nWhat are you waiting for"
    def s_recognize(self):
        with sr.Microphone() as source:
            try:
                audio = self.r.listen(source, phrase_time_limit=6)
                predicted_string = self.r.recognize_sphinx(audio)
                return predicted_string
            except:
                return "Invalid Input\nSomething went wrong"

if __name__ == "__main__":
    drugs = ['paracetamol']
    frequency = ['1', '2', '3', '4', '5', 'one', 'two', 'three']
    days_week = ['days', 'week', 'weeks']
    speech_obj = HiddenMarkovModel()
    text = speech_obj.recognize()
    print(text)
    # elements = text.lower().split()
    # medicine_dict = {}
    # for idx, element in enumerate(elements):
    #     if element in drugs:
    #         medicine_dict['Drug'] = element
    #     if element == 'times':
    #         medicine_dict['Frequency/Day'] = elements[idx-1]
    #     if element in days_week:
    #         medicine_dict['Days of dosage'] = elements[idx-1]
    #         medicine_dict['Quantity of meds'] = int(medicine_dict['Days of dosage']) * int(medicine_dict['Frequency/Day'])
            
    # print(f"Drug: {medicine_dict['Drug']}")
    # print(f"Frequency/Day: {medicine_dict['Frequency/Day']}")
    # print(f"Days of dosage: {medicine_dict['Days of dosage']}")
    # print(f"Quantity of meds: {medicine_dict['Quantity of meds']}")