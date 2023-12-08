import os

from azure.communication.sms import SmsClient
from azure.identity import DefaultAzureCredential

from dotenv import load_dotenv

load_dotenv()

service_name = os.getenv("SERVICE_NAME")
service_region = os.getenv("SERVICE_REGION")
endpoint = f"https://{service_name}.{service_region}.communication.azure.com"

sender = os.getenv("SENDER_PHONE")
recipient = os.getenv("RECIPIENT_PHONE")

try:
    # Quickstart code goes here
    # Create the SmsClient object which will be used to send SMS messages
    credential = DefaultAzureCredential()
    sms_client = SmsClient(endpoint, credential)

    ## Send a 1:1 SMS Message
    # calling send() with sms values
    sms_responses = sms_client.send(
        from_=sender,
        to=recipient,
        message="Hello World via SMS",
        enable_delivery_report=True,  # optional property
        tag="custom-tag",
    )  # optional property

    # # Send a 1:N SMS Message
    # # calling send() with sms values
    # sms_responses = sms_client.send(
    #     from_="<from-phone-number>",
    #     to=["<to-phone-number-1>", "<to-phone-number-2>"],
    #     message="Hello World via SMS Python",
    #     enable_delivery_report=True,  # optional property
    #     tag="custom-tag",
    # )  # optional property
except Exception as ex:
    print("Exception:")
    print(ex)
