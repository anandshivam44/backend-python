# import uvicorn
import psycopg2
# import json
# from fastapi import FastAPI
# from pydantic import BaseModel, Field, HttpUrl, parse_obj_as
# from typing import List, Set, Dict, Text
# app = FastAPI(debug=True)
conn = psycopg2.connect(database="df912qntf815eh", user="qntcbpuyzvkslk",
                        password="39b05f0abc02099fbed2afd0470964064380bc2a0a712cf125a939d4d3de5c49",
                        host="ec2-3-210-23-22.compute-1.amazonaws.com", port="5432")
cur = conn.cursor()
# cur = conn.cursor()
# cur.execute('''CREATE TABLE PDF
#       (BRANCH           TEXT     ,
#       CATEGORY            TEXT    ,
#       URL        TEXT,
#       NAME         TEXT);''')
cur.execute('''CREATE TABLE lostfound
      (id serial primary key,
       category text,
       brand text,
       main_color text,
       second_color text,
       description text,
       date_found text,
       found_location text,
       found_suite_no text ,
       message_me  text,
       drooped_off  text,
       Note text);''')
print("Table created successfully")

conn.commit()
conn.close()
