def formatter(msg):
	if type(msg) is not bool:
		smsg = msg.split(' :', 1)
		if len(smsg) == 2:
			nmsg = f'{smsg[0]}: {smsg[1]}'
			return nmsg
		return(msg)
	else:
		return False

def formatterCmd(msg):
	data = formatter(msg).split(': ') if type(msg) is not bool else False
	
	response = ''

	if type(data) == bool:
		response = {
			'user': 'bool',
			'method': 'error',
			'command': '',
			'message': '',
			'enabled': 'false'
			}
	elif len(data) == 2 and not False:
		usr = data[0]
		res = data[1].split(' ', 1) if len(data) >= 1 else ['None', 'None']
		cmd = res[0]
		exe = res[1] if len(res) > 1 else 'this is a message'
		#print(f'"{usr}" used the "{cmd}" command and got the "{exe}" response')



		if cmd[0] == '!':
			response = {
				'user': usr,
				'method': 'read',
				'command': cmd,
				'message': 'reading command',
				'enabled': True
				}
			if cmd == '!register':
				response = {
					'user': usr,
					'method': 'write',
					'command': exe.split(' ', 1)[0],
					'message': exe.split(' ', 1)[1],
					'enabled': True
					}
		else:
			response = False
		
	return response