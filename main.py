import configparser
import twitch
import asyncio
import sys

if len(sys.argv) < 1:
	print('Usage: python main.py "HML" or "PRD"')

ENV = sys.argv[0]

file = 'config.cfg' if ENV == 'HML' else 'auth.cfg'

config = configparser.ConfigParser()
config.read(file)

token = config['AUTH']['token']
oauth = config['AUTH']['oauth']
client = config['AUTH']['client']
target = config['AUTH']['target']

targetChannel = twitch.Twitch(token, oauth, client, target)

#print(targetChannel.getChannelInfo())

asyncio.get_event_loop().run_until_complete(targetChannel.joinChannel())