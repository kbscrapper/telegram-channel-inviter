#this code is arranged by Solved4You 2.0
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
import csv
import traceback
import time

#account details
api_id = 1219108
api_hash = '6a62fccfd576a92a04e6f021bd5c8bf2'
phone = '94705350802' 

session_name = 'scraper' #means that this session_name is for scraper
#this code is arranged by shamod
client = TelegramClient(str(session_name), api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

print('Fetching Members...')
all_participants = []

#enter target group or channel
target = 'carol5auth'
#this code is arranged by Solved4You 2.0
all_participants = client.iter_participants(target, limit=None, filter=None, aggressive=True)
#this code is arranged by Solved4You 2.0
print('Saving In file...')
with open("data.csv","w",encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['sr. no.', 'username', 'user id', 'name', 'Status'])
    i = 0
    for user in all_participants:

        i += 1
        if user.username:
            username = user.username
        else:
            username = ""
        if user.first_name:
            first_name = user.first_name
        else:
            first_name = ""
        if user.last_name:
            last_name = user.last_name
        else:
            last_name = ""
        name = (first_name + ' ' + last_name).strip()
        writer.writerow([i,username, user.id, name, 'group name'])
print('Members scraped successfully.')

#this code is arranged by Solved4You 2.0