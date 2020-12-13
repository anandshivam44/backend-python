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


class Pdf(BaseModel):
    url: str = "https://google.com"
    name: str = "I am pdf name"


class Item(BaseModel):
    type_of_archive: str = "IAS UPSC"
    list_of_pdfs: List[Pdf] = []


class Branch(BaseModel):
    branch_name: str = "Mechanical"
    branch_archive: List[Item] = []


class AllQuestionPaper(BaseModel):
    archive: List[Branch] = []


class Test(BaseModel):
    text: List[str] = "Hello"


@app.get("/pdf/")
async def pdf():
    cur.execute("SELECT BRANCH, CATEGORY, URL, NAME  from PDF")
    rows = cur.fetchall()
    # dd = {
    #     "branch_name": "Null",
    #     "branch_archive": {
    #         "type_of_archive": "Null",
    #         "list_of_pdfs": {
    #             '0': {
    #                 'url': "None",
    #                 'name': 'None'
    #             }
    #         }
    #     }
    # }
    dd = {}

    # dd = AllQuestionPaper()
    for row in rows:
        # dd['branch'] = row[0]
        if dd.get(row[0]) == None:
            dd[row[0]] = {}
            dd[row[0]]["type_of_archive"] = row[1]
        else:
            dd[row[0]]["type_of_archive"] = row[1]

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

    #     aa.url = row[2]
    #     aa.name = row[3]

    #     bb = Item()
    #     bb.type_of_archive = row[1]
    #     bb.list_of_pdfs.append(aa)

    #     cc = Branch()
    #     cc.branch_name = row[0]
    #     cc.branch_archive.append(bb)

    #     # dd.archive.append(cc)
    #     dd.archive.append(cc)

    # aa = Pdf()
    # aa.url = 'https://google.com'
    # aa.name = 'google'
    # aaa = Pdf()
    # aaa.url = 'https://yahoo.com'
    # aaa.name = 'Yahoo'
    # bb = Item()
    # bb.type_of_archive = "UPSC"
    # bb.list_of_pdfs.append(aa)
    # bb.list_of_pdfs.append(aaa)
    # cc = Branch()
    # cc.branch_name = "Mechanical"
    # cc.branch_archive.append(bb)
    # dd = AllQuestionPaper()
    # dd.archive.append(cc)

    # conn.commit()
    # tt = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
    # tt={}
    # tt['fname']='Shivam'
    # tt['lname']={'mname':'Anand'}
    return dd


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


# bb = AllQuestionPaper(archive=[
#         {
#             "branch_name": "Mechanical",
#             "branch_archive": [
#                 {
#                     "type_of_archive": "UPSC IAS",
#                     "list_of_pdfs": [
#                         {
#                             "url": "https://google.com",
#                             "name": "I am Google"
#                         },
#                         {
#                             "url": "https://Yahoo.com",
#                             "name": "I am Yahoo"
#                         }
#                     ]
#                 },
#                 {
#                     "type_of_archive": "College Notes",
#                     "list_of_pdfs": [
#                         {
#                             "url": "https://abc.com",
#                             "name": "I am ABC pdf"
#                         },
#                         {
#                             "url": "https://def.com",
#                             "name": "I am DEF pdf"
#                         },
#                         {
#                             "url": "https://ghi.com",
#                             "name": "I am GHI pdf"
#                         }
#                     ]
#                 }
#             ]
#         },
#         {
#             "branch_name": "Production",
#             "branch_archive": [
#                 {
#                     "type_of_archive": "Geology for IAS",
#                     "list_of_pdfs": [
#                         {
#                             "url": "https://google.com",
#                             "name": "I am Google"
#                         },
#                         {
#                             "url": "https://Yahoo.com",
#                             "name": "I am Yahoo"
#                         }
#                     ]
#                 },
#                 {
#                     "type_of_archive": "College Notes",
#                     "list_of_pdfs": [
#                         {
#                             "url": "https://abc.com",
#                             "name": "I am ABC pdf"
#                         },
#                         {
#                             "url": "https://def.com",
#                             "name": "I am DEF pdf"
#                         },
#                         {
#                             "url": "https://ghi.com",
#                             "name": "I am GHI pdf"
#                         }
#                     ]
#                 }
#             ]
#         }
#     ])

# @app.get("/pdf/")
# async def pdf():
#     cur.execute("SELECT BRANCH, CATEGORY, URL, NAME  from PDF")
#     rows = cur.fetchall()
#     dd={}
    # dd = AllQuestionPaper()
    # for row in rows:
    #     print("BRANCH = ", row[0])
    #     print("CATEGORY = ", row[1])
    #     print("URL = ", row[2])
    #     print("NAME = ", row[3])

    #     aa = Pdf()
    # dd['branch']=row[0]
    #     aa.url = row[2]
    #     aa.name = row[3]

    #     bb = Item()
    #     bb.type_of_archive = row[1]
    #     bb.list_of_pdfs.append(aa)

    #     cc = Branch()
    #     cc.branch_name = row[0]
    #     cc.branch_archive.append(bb)

    #     # dd.archive.append(cc)
    #     dd.archive.append(cc)

    # aa = Pdf()
    # aa.url = 'https://google.com'
    # aa.name = 'google'
    # aaa = Pdf()
    # aaa.url = 'https://yahoo.com'
    # aaa.name = 'Yahoo'
    # bb = Item()
    # bb.type_of_archive = "UPSC"
    # bb.list_of_pdfs.append(aa)
    # bb.list_of_pdfs.append(aaa)
    # cc = Branch()
    # cc.branch_name = "Mechanical"
    # cc.branch_archive.append(bb)
    # dd = AllQuestionPaper()
    # dd.archive.append(cc)

    # conn.commit()
    # tt = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
    # tt={}
    # tt['fname']='Shivam'
    # tt['lname']={'mname':'Anand'}
    # return dd
