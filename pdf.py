import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Set, Dict
app = FastAPI(debug=True)


class Pdf(BaseModel):
    url: str = "https://google.com"
    name: str = "I am pdf name"


class Item(BaseModel):
    type_of_archive: str = "IAS UPSC"
    list_of_pdfs: List[Pdf] = None


class Branch(BaseModel):
    branch_name: str = "Mechanical"
    branch_archive: List[Item] = None


class AllQuestionPaper(BaseModel):
    archive: List[Branch] = None


@app.get("/pdf/")
async def home():
    bb = AllQuestionPaper(archive=[
        {
            "branch_name": "Mechanical",
            "branch_archive": [
                {
                    "type_of_archive": "UPSC IAS",
                    "list_of_pdfs": [
                        {
                            "url": "https://google.com",
                            "name": "I am Google"
                        },
                        {
                            "url": "https://Yahoo.com",
                            "name": "I am Yahoo"
                        }
                    ]
                },
                {
                    "type_of_archive": "College Notes",
                    "list_of_pdfs": [
                        {
                            "url": "https://abc.com",
                            "name": "I am ABC pdf"
                        },
                        {
                            "url": "https://def.com",
                            "name": "I am DEF pdf"
                        },
                        {
                            "url": "https://ghi.com",
                            "name": "I am GHI pdf"
                        }
                    ]
                }
            ]
        },
        {
            "branch_name": "Production",
            "branch_archive": [
                {
                    "type_of_archive": "Geology for IAS",
                    "list_of_pdfs": [
                        {
                            "url": "https://google.com",
                            "name": "I am Google"
                        },
                        {
                            "url": "https://Yahoo.com",
                            "name": "I am Yahoo"
                        }
                    ]
                },
                {
                    "type_of_archive": "College Notes",
                    "list_of_pdfs": [
                        {
                            "url": "https://abc.com",
                            "name": "I am ABC pdf"
                        },
                        {
                            "url": "https://def.com",
                            "name": "I am DEF pdf"
                        },
                        {
                            "url": "https://ghi.com",
                            "name": "I am GHI pdf"
                        }
                    ]
                }
            ]
        }
    ])
    return bb


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
