import os

from azure.communication.email import EmailClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv()

service_name = os.getenv("SERVICE_NAME")
service_region = os.getenv("SERVICE_REGION")
access_key = os.getenv("ACCESS_KEY")
endpoint = f"https://{service_name}.{service_region}.communication.azure.com"
connection_string = f"{endpoint}/;accesskey={access_key}"

sender_address = os.getenv("SENDER_EMAIL")
recipient_address = os.getenv("RECIPIENT_EMAIL")

POLLER_WAIT_TIME = 10

message = {
    "senderAddress": sender_address,
    "recipients": {
        "to": [{"address": recipient_address}],
    },
    "content": {
        "subject": "Test email from Python Sample",
        "plainText": "This is plaintext body of test email.",
        "html": "<html><h1>This is the html body of test email.</h1></html>",
    },
}

try:
    credential = DefaultAzureCredential()

    client = EmailClient(endpoint, credential)

    poller = client.begin_send(message)

    time_elapsed = 0
    while not poller.done():
        print("Email send poller status: " + poller.status())

        poller.wait(POLLER_WAIT_TIME)
        time_elapsed += POLLER_WAIT_TIME

        if time_elapsed > 18 * POLLER_WAIT_TIME:
            raise RuntimeError("Polling timed out.")

    if poller.result()["status"] == "Succeeded":
        print(f"Successfully sent the email (operation id: {poller.result()['id']})")
    else:
        raise RuntimeError(str(poller.result()["error"]))

except Exception as ex:
    print(ex)
