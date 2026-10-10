import os
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def send_telegram_alert(message):
  """Sends an automated message to your Telegram chat using the Telegram Bot API."""
  url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
  payload = {"chat_id": CHAT_ID, "text": message}

  try:
    response = requests.post(url, json=payload)
    if response.status_code == 200:
      print("Alert sent successfully to Telegram!")
    else:
      print(f"Failed to send alert. Status code: {response.status_code}")
      print(response.text)
  except Exception as e:
    print(f"An error occurred: {e}")


def button_pressed():
  """Triggered when the button is pressed."""
  print("Button was pressed! Triggering alert...")
  send_telegram_alert(
      "Someone pressed the alert button."
  )


if __name__ == "__main__":
  print("Waiting for button press...")
  input("Press [Enter] to simulate pressing the button: ")
  button_pressed()