from typing import List
# from databases import Database
import databases
import sqlalchemy
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# import os
# import urllib
# from dotenv import load_dotenv
# load_dotenv()

database="df912qntf815eh" 
user="qntcbpuyzvkslk",
password="39b05f0abc02099fbed2afd0470964064380bc2a0a712cf125a939d4d3de5c49",
host="ec2-3-210-23-22.compute-1.amazonaws.com"
port="5432"


# host_server = os.environ.get('host_server')
# db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port')))
# database_name = os.environ.get('database_name')
# db_username = urllib.parse.quote_plus(str(os.environ.get('db_username')))
# db_password = urllib.parse.quote_plus(str(os.environ.get('db_password')))
# ssl_mode = urllib.parse.quote_plus(str(os.environ.get('ssl_mode')))
DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}'.format(user, password, host, port, database)
database = databases.Database(DATABASE_URL)
# metadata = sqlalchemy.MetaData()

# notes = sqlalchemy.Table(
#     "notes",
#     metadata,
#     sqlalchemy.Column("title", sqlalchemy.String),
#     sqlalchemy.Column("url", sqlalchemy.String)
# )

# engine = sqlalchemy.create_engine(
#     DATABASE_URL, pool_size=3, max_overflow=0
# )
# metadata.create_all(engine)

# class NoteIn(BaseModel):
#     text: str
#     completed: bool

# class Note(BaseModel):
#     id: int
#     text: str
#     completed: bool


# app = FastAPI(title="REST API using FastAPI PostgreSQL Async EndPoints")

# @app.on_event("startup")
# async def startup():
#     await database.connect()

# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()

# @app.get("/internship/", response_model=Note, status_code = status.HTTP_200_OK)
# async def read_notes(note_id: int):
#     query = notes.select().where(notes.c.id == note_id)
#     return await database.fetch_one(query)
