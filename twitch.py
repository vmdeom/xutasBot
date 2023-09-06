import requests
import websockets
import asyncio
import formatter
from chat import Command, readCommand


class Twitch:
	def __init__(self, token, oauth, client_id, target_id):
		self.token = token
		self.oauth = oauth
		self.client_id = client_id
		self.target_id = target_id
		
		self.headers = {
			'Authorization': self.token,
			'Client-Id': self.client_id
			}

		self.params = {
			'broadcaster_id': self.target_id
			}

		self.url = 'https://api.twitch.tv/helix/channels'
		self.uri = 'ws://irc-ws.chat.twitch.tv:80'

	def getChannelInfo(self):
		
		response = requests.get(self.url, headers=self.headers, params=self.params)

		if response.status_code == 200:
			data = response.json()
			return (data)
		else:
			return (f'Erro: {response.status_code}')

	async def joinChannel(self):
		
		async with websockets.connect(self.uri) as websocket:
		
			print(f'>>>>>Websocket connected')
			await websocket.send(f'CAP REQ :twitch.tv/membership twitch.tv/tags twitch.tv/commands')
			await websocket.send(f'PASS {self.oauth}')
			await websocket.send(f'NICK exutasbot')
			await websocket.send(f'JOIN #exutas')
			#await websocket.send(f'PRIVMSG #exutas :This is a sample message')
			
			command = Command()

			while True:
				response = await websocket.recv()
				response_split = response.split('#')
				message = response_split[len(response_split) - 1]
				f_message = formatter.formatter(message)
				print(f_message)
				c_message = formatter.formatterCmd(message)
				print(c_message)
				cmm = readCommand(c_message)
				await websocket.send(f'PRIVMSG #exutas :{cmm}')