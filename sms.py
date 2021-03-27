from clx.xms import Client
from clx.xms.api import MtBatchTextSmsCreate


def send_sms(text):
    my_service_plan = "c1d84367c9f24b23af75b7d43a15d767"
    my_token = "bb69349187a04ce09d4fd0614a6b131e"
    client = Client(my_service_plan, my_token)
    # Code to send messages in batch:
    # batch_parms = MtBatchTextSmsCreate()
    # batch_parms.sender = '12345'
    # batch_parms.recipients = {'918209759721'}
    # batch_params.body = 'Hello, World!'
    # result = client.create_batch(batch_params)
    client.create_text_message(sender='1234', recipient='918209759721', body=text)

if __name__ == '__main__':
    from speech import GSpeech
    speech_obj = GSpeech()
    send_sms(my_service_plan, my_token, text=speech_obj.recognize())
    print("Sucess!!")