import csv
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

with open('Book1.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        cur.execute("INSERT INTO PDF (BRANCH,CATEGORY,URL,NAME) \
            VALUES ('"+row[0]+"', '"+row[1]+"', '"+row[2]+"', '"+row[3]+"' )")
        print(row[0])
        print(row[1])
        print(row[2])
        print(row[3])

conn.commit()
print ("Records created successfully")
conn.close()




