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


class Testing(BaseModel):
    name: str = "Shivam"
    age: int = 21

bb =Testing(name="Shivam Anand",age=22)
# bb:Testing =None
bb.name="Abc"
bb.age=23
print(bb)


# people = {'num': {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
#           3: {'name': 'Luna', 'age': '24', 'sex': 'Female'},
#           4: {'name': 'Peter', 'age': '29', 'sex': 'Male'}}

# del people[3], people[4]
# print(people.dict)
