from typing import List
import databases
import sqlalchemy
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import urllib
from dotenv import load_dotenv
load_dotenv() 
#I want to show data  in the left of screen to API okay

host_server = os.environ.get('host_server')
db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port')))
database_name = os.environ.get('database_name')
db_username = urllib.parse.quote_plus(str(os.environ.get('db_username')))
db_password = urllib.parse.quote_plus(str(os.environ.get('db_password')))
ssl_mode = urllib.parse.quote_plus(str(os.environ.get('ssl_mode')))
# DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username, db_password, host_server, db_server_port, database_name, ssl_mode)
DATABASE_URL = 'postgres://qntcbpuyzvkslk:39b05f0abc02099fbed2afd0470964064380bc2a0a712cf125a939d4d3de5c49@ec2-3-210-23-22.compute-1.amazonaws.com:5432/df912qntf815eh?sslmode=disable'

conn = psycopg2.connect(database="df912qntf815eh", user="qntcbpuyzvkslk",
                        password="39b05f0abc02099fbed2afd0470964064380bc2a0a712cf125a939d4d3de5c49",
                        host="ec2-3-210-23-22.compute-1.amazonaws.com", port="5432")
# database = databases.Database(DATABASE_URL)
cur = conn.cursor()
metadata = sqlalchemy.MetaData()

table = sqlalchemy.Table(
    "startups",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("organisation", sqlalchemy.String),
    sqlalchemy.Column("url", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("completed", sqlalchemy.Boolean),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, pool_size=3, max_overflow=0
)
metadata.create_all(engine)
# this class NoteIn is used to take input for quering in the database.
class NoteIn(BaseModel):
    title: str
    organisation: str
    url: str
    description: str
    completed: bool
# this class Note is used for printing the qurey result
class Note(BaseModel):
    id: int
    title: str
    organisation: str
    url: str
    description: str
    completed: bool


app = FastAPI(title="REST API using FastAPI PostgreSQL Async EndPoints")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)



@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()



@app.get("/")
async def read_main():
    return {"msg": "connected ,api working fine:-)"}

@app.get("/notes/", response_model=List[Note], status_code = status.HTTP_200_OK)
async def read_notes(skip: int = 0, take: int = 20):
    query = table.select().offset(skip).limit(take)
    return await database.fetch_all(query)

@app.get("/notes/{note_id}/", response_model=Note, status_code = status.HTTP_200_OK)
async def read_notes(note_id: int):
    query = table.select().where(table.c.id == note_id)
    return await database.fetch_one(query)

@app.post("/notes/", response_model=Note, status_code = status.HTTP_201_CREATED)
async def create_note(data: NoteIn):
    query = table.insert().values(title=data.title,organisation=data.organisation,url=data.url,description=data.description, completed=data.completed)
    last_record_id = await database.execute(query)
    return {**data.dict(), "id": last_record_id}

@app.put("/notes/{note_id}/", response_model=Note, status_code = status.HTTP_200_OK)
async def update_note(note_id: int, data: NoteIn):
    query = table.update().where(table.c.id == note_id).values(title=data.title,organisation=data.organisation,url=data.url,description=data.description, completed=data.completed)
    await database.execute(query)
    return {**data.dict(), "id": note_id}

@app.delete("/notes/{note_id}/", status_code = status.HTTP_200_OK)
async def delete_note(note_id: int):
    query = table.delete().where(table.c.id == note_id)
    await database.execute(query)
    return {"message": "data with id: {} deleted successfully!".format(note_id)}