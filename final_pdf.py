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

@app.get("/pdf/")
async def pdf():
    cur.execute("SELECT BRANCH, CATEGORY, URL, NAME  from PDF")
    rows = cur.fetchall()
    dd = {}

    for row in rows:
        if dd.get(row[0]) == None:
            dd[row[0]] = {}
        #     dd[row[0]]["type_of_archive"] = row[1]
        # else:
        #     dd[row[0]]["type_of_archive"] = row[1]

        if dd[row[0]].get("list_of_pdfs") == None:
            dd[row[0]]["list_of_pdfs"] = {}
            dd[row[0]]["list_of_pdfs"][0] = {}
            dd[row[0]]["list_of_pdfs"][0]["url"] = row[2]
            dd[row[0]]["list_of_pdfs"][0]["name"] = row[3]
        else:
            n = len(dd[row[0]]["list_of_pdfs"].keys())
            print('n = ', n)
            dd[row[0]]["list_of_pdfs"][n] = {}
            dd[row[0]]["list_of_pdfs"][n]["url"] = row[2]
            dd[row[0]]["list_of_pdfs"][n]["name"] = row[3]
    return dd


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
