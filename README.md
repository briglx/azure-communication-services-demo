# Azure Communciation Service - Learn Together

This project is a demo of the Azure Communication Service. It's a place to explore the capabilities of the service and learn together.

## Goals

- Learn about the Azure Communication Service

## Learnings so Far

- [x] How to create a phone number
- [ ] How to send a text message
- [x] How to send an email
- [ ] Make a phone call

## How to Create a Phone Number

The subscription I'm using only allows me to create a trial phone number. This is a limitation of the subscription, not the service.

When I attempt to use the script `./phone-numbers-quickstart/phone_numbers_sample.py` I get the following error:

```bash
(InsufficientPermissions) The subscription subscriptionId 00000000-0000-0000-0000-000000000000 is unable to purchase numbers at this time.
```

## How to Send an Email

- Setup Eamil communciation Service
- Verify Domain

```bash
python ./send-email/send-email.py
```

## How to Make a Phone Call

TBD

# References
* Quick Starts https://github.com/Azure-Samples/communication-services-python-quickstarts