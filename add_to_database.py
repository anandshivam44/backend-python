import csv
import psycopg2
conn = psycopg2.connect(database="df912qntf815eh", user="qntcbpuyzvkslk",
                        password="39b05f0abc02099fbed2afd0470964064380bc2a0a712cf125a939d4d3de5c49",
                        host="ec2-3-210-23-22.compute-1.amazonaws.com", port="5432")
cur = conn.cursor()

with open('lost_found.csv', 'r') as file:
    reader = csv.reader(file)
    # print(len(reader))
    for row in reader:
        # print(len(row))
        # cur.execute("INSERT INTO PDF (BRANCH,CATEGORY,URL,NAME) \
        #     VALUES ('"+row[0]+"', '"+row[1]+"', '"+row[2]+"', '"+row[3]+"' )")
        cur.execute("INSERT INTO lostfound (category ,brand ,main_color ,second_color ,description ,date_found ,found_location ,found_suite_no  ,message_me  ,drooped_off  ,Note ) \
            VALUES ('"+row[0]+"' , '"+row[1]+"' , '"+row[2]+"' , '"+row[3]+"' , '"+row[4]+"' , '"+row[5]+"' , '"+row[6]+"' , '"+row[7]+"' , '"+row[8]+"' , '"+row[9]+"' , '"+row[10]+"')")
        # print(row[0])
        # print(row[1])
        # print(row[2])
        # print(row[3])

conn.commit()
print("Records created successfully")
conn.close()
