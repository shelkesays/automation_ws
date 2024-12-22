from twilio.rest import Client

# Twilio credentials
ACCOUNT_SID = "your-account-sid"
AUTH_TOKEN = "your-auth-token"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_sms(to, message):
    from_phone = "+1234567890"  # Your Twilio phone number
    client.messages.create(
        body=message,
        from_=from_phone,
        to=to
    )
    print(f"SMS sent to {to}")

# Example usage
send_sms("+919224876939", "Hello! This is an automated SMS.")
