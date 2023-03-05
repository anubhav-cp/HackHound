from twilio.rest import Client

def send_sms():
    account_sid = "AC1db2e94c2b09fd81a104c9cf087c54fa"
    auth_token = "b98d988212e9240beaf0bd8f62bc2f0f"
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Your Order is Confirmed! WE'll deliver it Asap.",
                        from_='+15674074460',
                        to='+919289397706'
                    )

    print(message.sid)