from typing import List
import uvicorn

# from databases import Database
import databases
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import urllib
# from dotenv import load_dotenv
# load_dotenv()

# database="df912qntf815eh" 
# user="qntcbpuyzvkslk",
# password="39b05f0abc02099fbed2afd0470964064380bc2a0a712cf125a939d4d3de5c49",
# host="ec2-3-210-23-22.compute-1.amazonaws.com"
# port="5432"
# ssl_mode='prefer'
# host_server = os.environ.get('host_server')
# db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port')))
# database_name = os.environ.get('database_name')
# db_username = urllib.parse.quote_plus(str(os.environ.get('db_username')))
# db_password = urllib.parse.quote_plus(str(os.environ.get('db_password')))
# ssl_mode = urllib.parse.quote_plus(str(os.environ.get('ssl_mode')))
# DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username, db_password, host_server, db_server_port, database_name, ssl_mode)
# DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username, db_password, host_server, db_server_port, database_name, ssl_mode)
DATABASE_URL = 'postgres://qntcbpuyzvkslk:39b05f0abc02099fbed2afd0470964064380bc2a0a712cf125a939d4d3de5c49@ec2-3-210-23-22.compute-1.amazonaws.com:5432/df912qntf815eh?sslmode=prefer'

# engine = create_engine(DATABASE_URL, echo=True)
# meta = MetaData()
app = FastAPI(debug=True)
# internship = Table(
#     'internship', meta,
#     Column("title", String),
#     Column("url", String)
# )
# conn = engine.connect()


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )
database = databases.Database(DATABASE_URL)
metadata = MetaData()

internship = Table(
    "internship",
    metadata,
    Column("title", String),
    Column("url", String)
)
engine = create_engine(
    DATABASE_URL, pool_size=3, max_overflow=0
)

# engine = sqlalchemy.create_engine(
#     DATABASE_URL,echo=True
# )
# metadata.create_all(engine)

# class Note(BaseModel):
#     title: str
#     url: str


@app.on_event("startup")
async def startup():
    await engine.connect()
    # pass

# @app.on_event("shutdown")
# async def shutdown():
#     # await database.disconnect()
#     pass


# @app.get("/internship/", response_model=Note, status_code = status.HTTP_200_OK)
# async def internship(note_id: int):
#     query = internship.select()
#     return await database.fetch_one(query)

# @app.get("/pdf/")
# async def pdf():
#     s = internship.select()
#     result = conn.execute(s)
#     return {}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
