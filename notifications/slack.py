from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Slack Bot Token
SLACK_TOKEN = "your-slack-bot-token"
CHANNEL_ID = "your-channel-id"

client = WebClient(token=SLACK_TOKEN)

def send_slack_message(message):
    try:
        response = client.chat_postMessage(channel=CHANNEL_ID, text=message)
        print(f"Message sent: {response['ts']}")
    except SlackApiError as e:
        print(f"Error sending message: {e.response['error']}")

# Example usage
send_slack_message("Hello, Slack! This is an automated message.")
