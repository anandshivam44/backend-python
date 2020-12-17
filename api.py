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


class InternshipModel(BaseModel):
    id: int = 0
    title: str = "null"
    url: str = "null"


class PDFModel(BaseModel):
    id: int = 0
    branch: str = "null"
    # semester: str = "null"
    category: str = "null"
    url: str = "null"
    name:str="null"


@app.get("/internship/")
async def internship():
    cur.execute("SELECT TITLE,URL from INTERNSHIP")
    rows = cur.fetchall()
    i = 0
    internship_json: List[InternshipModel] = []
    for row in rows:
        internship_item = InternshipModel()
        internship_item.id = i
        i = i+1
        internship_item.title = row[0]
        internship_item.url = row[1]
        internship_json.append(internship_item)

    # print(internship_json)
    return internship_json


@app.get("/pdf/")
async def pdf():
    cur.execute("SELECT BRANCH, CATEGORY, URL, NAME  from PDF")
    rows = cur.fetchall()
    PDF_json: List[PDFModel] = []
    i=0
    for row in rows:
        PDF_item = PDFModel()
        PDF_item.id = i
        i = i+1
        PDF_item.branch=row[0]
        # PDF_item.semester
        PDF_item.category=row[1]
        PDF_item.url=row[2]
        PDF_item.name=row[3]
        PDF_json.append(PDF_item)
        
    return PDF_json


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
