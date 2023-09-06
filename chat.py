import json
from typing import Optional
from sqlmodel import Field, SQLModel, create_engine, Session, select
import formatter

class Command(SQLModel, table=True):
	id: Optional[int] = Field(default=None, nullable=True, primary_key=True)
	user: str
	method: str
	command: str = Field(unique=True)
	message: str
	enabled: bool

engine = create_engine("sqlite:///database.db")
#SQLModel.metadata.create_all(engine)

def runCommand(cmd):
	data = Command(**cmd)
	with Session(engine) as session:
		if cmd['method'] == 'read':
			cmm = cmd['command']
			com = cmm.split('!')[1].replace('\r\n', '')
			command = select(Command).where(Command.command == com)
			result = session.exec(command).first()
			message = json.loads(result.json())['message'].replace('\r\n', '')
			return message
		elif cmd['method'] == 'write':
			try:
				session.add(data)
				session.commit()
				session.refresh(data)
				return 'command added successfully'
			except:
				return 'command already created'