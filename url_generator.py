import os
import boto3
import time
import dotenv

def write_logs(message: str):
    clientlogs.put_log_events(
    logGroupName =  "Assignment_1",
    logStreamName = "URL_GEN",
    logEvents= [
        {
            'timestamp' : int(time.time() * 1e3),
            'message' : message,
        }
    ]   
)   

clientlogs = boto3.client('logs',
                        region_name= 'us-east-1',
                        aws_access_key_id = os.environ.get('AWS_ACCESS_KEY'),
                        aws_secret_access_key = os.environ.get('AWS_SECRET_KEY')
                        )

write_logs("Connected to s3")

def url_gen_goes(input):
    write_logs("url_generator_starts")
    arr = input.split("_")
    tproduct_code = arr[1].split("-")
    s1 = tproduct_code[2]
    finalProductCode =tproduct_code[0]+"-"+tproduct_code[1]+"-"+ ''.join([i for i in s1 if not i.isdigit()])
    write_logs("Final Product Code")
    write_logs(finalProductCode)
    date = arr[3]
    year, day_of_year, hour = date[1:5], date[5:8], date[8:10]
    fs = "https://noaa-goes18.s3.amazonaws.com/{}/{}/{}/{}/{}".format(finalProductCode,year,day_of_year,hour,input)
    write_logs("GOES url")
    write_logs(fs)
    print(fs)
    return fs


def url_gen_nexrad(input):
    arr = input.split("_")[0]
    year, day, hour, station = arr[4:8], arr[8:10], arr[10:12], arr[0:4]
    fs = "https://noaa-nexrad-level2.s3.amazonaws.com/{}/{}/{}/{}/{}".format(year,day,hour,station,input)
    write_logs("NEXRAD url")
    write_logs(fs)
    print(fs)
    return fs




input_string = "KBYX20150804_000940_V06.gz"

EXACT_URL = "https://noaa-goes18.s3.amazonaws.com/ABI-L1b-RadC/2023/002/01/OR_ABI-L1b-RadC-M6C01_G18_s20230020101172_e20230020103548_c20230020103594.nc"
test = "OR_ABI-L2-DSRC-M6_G18_s20223180501179_e20223180503552_c20223180508262.nc"
test_fs = url_gen_goes(test)

# assert(test_fs == EXACT_URL)
write_logs("test url")
write_logs(test)