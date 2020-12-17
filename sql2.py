from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
DATABASE_URL = 'postgres://qntcbpuyzvkslk:39b05f0abc02099fbed2afd0470964064380bc2a0a712cf125a939d4d3de5c49@ec2-3-210-23-22.compute-1.amazonaws.com:5432/df912qntf815eh?sslmode=prefer'

engine = create_engine(DATABASE_URL, echo=True)
meta = MetaData()

# students = Table(
#     'students', meta,
#     Column('id', Integer, primary_key=True),
#     Column('name', String),
#     Column('lastname', String), This example from tutorialspoint workked
# )
internship = Table(
    'internship', meta,
    Column("title", String),
    Column("url", String)
)

conn = engine.connect()
s = internship.select()
result = conn.execute(s)

for row in result:
    print(row[0])
    print(row[1])

