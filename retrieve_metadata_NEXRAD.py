import sqlite3
import boto3
import os
import logging
from dotenv import load_dotenv
import pandas as pd
import time

load_dotenv()
s3 = boto3.client('s3',region_name='us-east-1',
                        aws_access_key_id = os.environ.get('AWS_ACCESS_KEY'),
                        aws_secret_access_key = os.environ.get('AWS_SECRET_KEY'))

clientlogs = boto3.client('logs',
                        region_name= 'us-east-1',
                        aws_access_key_id = os.environ.get('AWS_ACCESS_KEY'),
                        aws_secret_access_key = os.environ.get('AWS_SECRET_KEY')
                        )

def write_logs(message: str):
    clientlogs.put_log_events(
    logGroupName =  "Assignment_1",
    logStreamName = "nexrad",
    logEvents= [
        {
            'timestamp' : int(time.time() * 1e3),
            'message' : message,
        }
    ]   
)  

conn = sqlite3.connect("s3_nexrad.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS folders (month text, day text,nexrad_station text, Is2023 text)")
bucket = 'noaa-nexrad-level2'
year = ['2022','2023']
write_logs(bucket)


def create_list(result,level):
    l = []
    for o in result.get('CommonPrefixes'):
        val = o.get("Prefix").split('/')
        l.append(val[level])
    return l

def retrieve_metadata_NEXRAD(bucket,prefix,level):
    month,day,nexrad_station = [],[],[]
    result = s3.list_objects(Bucket=bucket, Prefix=prefix, Delimiter='/')
    month = create_list(result,1)

    for i in month:
        tprefix = prefix + str(i) + "/"
        result_1 = s3.list_objects(Bucket=bucket, Prefix=tprefix, Delimiter='/')
        dy = create_list(result_1,2)
        day.append(dy)

        for j in dy:
            ttprefix = tprefix + str(j) + "/"
            result_2 = s3.list_objects(Bucket=bucket, Prefix=ttprefix, Delimiter='/')
            h = create_list(result_2,3)
            nexrad_station.append(h)

    populate_db(month,day,nexrad_station,level)

def populate_db(month, day,nexrad_station,level):
    i = 0
    for y in month:
        day_aaray = day[i]
        j = 0
        for d in day_aaray:
            nexrad_station_array = nexrad_station[j]
            for h in nexrad_station_array:
                
                cursor.execute("INSERT INTO folders VALUES(?,?,?,?)",(y,d,h,level))
            j+=1
        i+=1


for i in range(len(year)):
    prefix = year[i] + '/'
    retrieve_metadata_NEXRAD(bucket,prefix,i)
# Commit the changes to the database
conn.commit()


# Close the connection to the database
conn.close()
