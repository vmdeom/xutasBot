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
SQLModel.metadata.create_all(engine)

def runCommand(cmd):
	with Session(engine) as session:
		if cmd['method'] == 'read':
			command = select(Command).where(Command.command == cmd)
			result = session.exec(command).first
			print(result['message'])
		elif cmd['method'] == write:
			session.add(cmd)
			session.commit()
			session.refresh(cmd)
			

def readCommand(msg):
	cmd = formatter.formatterCmd(msg)
	if cmd is not False:
		runCommand(cmd)