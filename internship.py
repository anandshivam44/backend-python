import uvicorn
import psycopg2
import json
from fastapi import FastAPI
from pydantic import BaseModel, Field, HttpUrl, parse_obj_as
from typing import List, Set, Dict, Text
app = FastAPI(debug=True)
conn = psycopg2.connect(database="df912qntf815eh", user="qntcbpuyzvkslk",
                        password="39b05f0abc02099fbed2afd0470964064380bc2a0a712cf125a939d4d3de5c49",
                        host="ec2-3-210-23-22.compute-1.amazonaws.com", port="5432")
cur = conn.cursor()

@app.get("/internship/")
async def pdf():
    cur.execute("SELECT TITLE, URL  from INTERNSHIP")
    rows = cur.fetchall()
    internship_json = {}
    i=0

    for row in rows:

        if internship_json.get(row[0]) == None:
            internship_json[i] = {}
            internship_json[i]["titlle"]=row[0]
            internship_json[i]["url"]=row[1]
        else:
            internship_json[i]["titlle"]=row[0]
            internship_json[i]["url"]=row[1]
        i=i+1

    print(internship_json)
    return internship_json


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


'''
SAMPLE OUTPUT
------------------------
{
    "Mechanical": {
        "list_of_pdfs": {
            "0": {
                "url": "https://google.com",
                "name": "Google"
            },
            "1": {
                "url": "https://flipkart.com",
                "name": "Flipkart"
            }
        }
    },
    "Production": {
        "list_of_pdfs": {
            "0": {
                "url": "https://yahoo.com",
                "name": "Yahoo"
            }
        }
    }
}
'''