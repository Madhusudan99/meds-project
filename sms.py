from clx.xms import Client
from clx.xms.api import MtBatchTextSmsCreate


def send_sms(text, mobile_number):
    my_service_plan = "934aef9ae78d42f896710cacf237ba1d"
    my_token = "f36c211603074528a759770fba2451eb"
    client = Client(my_service_plan, my_token)
    # Code to send messages in batch:
    # batch_parms = MtBatchTextSmsCreate()
    # batch_parms.sender = '12345'
    # batch_parms.recipients = {'918209759721'}
    # batch_params.body = 'Hello, World!'
    # result = client.create_batch(batch_params)
    client.create_text_message(sender='1234', recipient="91"+mobile_number, body=text)

if __name__ == '__main__':
    from speech import HiddenMarkovModel
    speech_obj = HiddenMarkovModel()
    send_sms(text="hello world!!", mobile_number="7023222498")
    print("Sucess!!")