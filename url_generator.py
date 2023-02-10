import os
import boto3
import time
import dotenv
import requests
clientlogs = boto3.client('logs',
                        region_name= 'us-east-1',
                        aws_access_key_id = os.environ.get('AWS_ACCESS_KEY'),
                        aws_secret_access_key = os.environ.get('AWS_SECRET_KEY')
                        )


def url_gen_goes(input):
    write_logs(message="url_generator_starts")
    arr = input.split("_")
    tproduct_code = arr[1].split("-")
    s1 = tproduct_code[2]
    finalProductCode =tproduct_code[0]+"-"+tproduct_code[1]+"-"+ ''.join([i for i in s1 if not i.isdigit()])
    write_logs(finalProductCode)
    date = arr[3]
    year, day_of_year, hour = date[1:5], date[5:8], date[8:10]
    fs = "https://noaa-goes18.s3.amazonaws.com/{}/{}/{}/{}/{}".format(finalProductCode,year,day_of_year,hour,input)
    write_logs(fs)
    return fs


def url_gen_nexrad(input):
    arr = input.split("_")[0]
    year, day, hour, station = arr[4:8], arr[8:10], arr[10:12], arr[0:4]
    fs = "https://noaa-nexrad-level2.s3.amazonaws.com/{}/{}/{}/{}/{}".format(year,day,hour,station,input)
    write_logs(fs)
    return fs

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
def check_filename(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        if filename in response.text:
            return True
        else:
            return False
    else:
        return False
def file_validator(file_name):
    # define the expected format for the file name
    expected_format = "OR_ABI-L1b-RadC-M6C01_G18_s{year}{day}{hour}{time}_{end_time}_c{creation_time}.nc"

    # split the file name into different parts
    file_parts = file_name.split("_")
    if len(file_parts) == 6 and file_parts[0] == "OR" and file_parts[1] == "ABI-L1b-RadC-M6C01" and file_parts[2] == "G18":
        year = file_parts[3][1:5]
        day = file_parts[3][5:8]
        hour = file_parts[3][8:10]
        time = file_parts[3][10:]
        end_time = file_parts[4]
        creation_time = file_parts[5][1:-3]
        if expected_format.format(year=year, day=day, hour=hour,time = time, end_time=end_time, creation_time=creation_time) == file_name:
            url = url_gen_goes(file_name)
            check = check_filename(url,file_name)
            print(check)
            if(check):
                return '0'
            else:
                return '2'
    
    else:
        return '1'

df = file_validator("OR_ABI-L1b-RadC-M6C01_G18_s20230410001170_e20230410003543_c20230410003571.nc")
# df = check_filename('https://noaa-goes18.s3.amazonaws.com/index.html#ABI-L1b-RadC/2023/041/00/','OR_ABI-L1b-RadC-M6C01_G18_s20230410001170_e20230410003543_c20230410003571.nc')
#print(df)
# input_string = "KABR20230210_000240_V06"

# test = "OR_ABI-L2-DSRC-M6_G18_s20223180501179_e20223180503552_c20223180508262.nc"
# url_gen_nexrad(input_string)
# #url_gen(test)

