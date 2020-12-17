import psycopg2

conn = psycopg2.connect(database="df912qntf815eh", user="qntcbpuyzvkslk",
                        password="39b05f0abc02099fbed2afd0470964064380bc2a0a712cf125a939d4d3de5c49",
                        host="ec2-3-210-23-22.compute-1.amazonaws.com", port="5432")

cur = conn.cursor()
cur.execute("SELECT TITLE, URL  from INTERNSHIP")
rows = cur.fetchall()
i=0
internship_json = {}
for row in rows:
    # print(row[0])
    # print(row[1])
    # print("\n")

    if internship_json.get(row[0]) == None:
            internship_json[i] = {}
            internship_json[i]["titlle"]=row[0]
            internship_json[i]["titlle"]=row[1]
    else:
        internship_json[i]["titlle"]=row[0]
        internship_json[i]["titlle"]=row[1]
    i=i+1
    # if internship_json[row[0]].get("list_of_pdfs") == None:
    #         internship_json[row[0]]["list_of_pdfs"] = {}
    #         internship_json[row[0]]["list_of_pdfs"][0] = {}
    #         internship_json[row[0]]["list_of_pdfs"][0]["url"] = row[2]
    #         internship_json[row[0]]["list_of_pdfs"][0]["name"] = row[3]


    print(internship_json)
