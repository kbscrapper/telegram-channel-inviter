from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
import csv
import traceback
import time
import random

# Define API credentials and phone number
api_id = 1219108
api_hash = '6a62fccfd576a92a04e6f021bd5c8bf2'
phone = '94705350802'

# Define session and channel details
session_name = ''
channel_username = 'newairdropsind'

# Connect to the Telegram client
client = TelegramClient(session_name, api_id, api_hash)
client.connect()

# Authorize the client if not already authorized
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

# Read user data from CSV file
input_file = 'data.csv'
users = []

with open(input_file, encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",", lineterminator="\n")
    next(rows, None)  # Skip header row
    for row in rows:
        user = {
            'srno': int(row[0]),
            'username': row[1],
            'id': int(row[2]),
            'name': row[4]
        }
        users.append(user)

# Get range of users to add
start_from = int(input("Start From = "))
end_to = int(input("End To = "))

# Invite users to the channel
n = 0
while True:
    try:
        for user in users:
            if start_from <= user['srno'] <= end_to:
                print(f"Adding user {user['id']}")

                if not user['username']:
                    print("No username, moving to next user.")
                    continue

                client(InviteToChannelRequest(channel_username, [user['username']]))

                wait_time = random.randrange(60, 130)
                print(f"Waiting for {wait_time} seconds...")
                time.sleep(wait_time)

                n += 1
                if n % 50 == 0:
                    print("Reached 50 users, sleeping for 15 minutes...")
                    time.sleep(900)

            elif user['srno'] > end_to:
                print("Members added successfully.")
                break

    except PeerFloodError as e:
        print(f"Getting Flood Error from Telegram: {e.message}. Script is waiting for 10 minutes.")
        time.sleep(600)  # Wait for 10 minutes before retrying

    except UserPrivacyRestrictedError:
        print("The user's privacy settings do not allow you to do this. Skipping user.")
        continue

    except Exception as e:
        traceback.print_exc()
        print(f"Unexpected error occurred: {e}. Continuing with next user.")
        continue

client.disconnect()
