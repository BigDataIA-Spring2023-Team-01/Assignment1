import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, date
import os
import boto3
import logging
from dotenv import load_dotenv
import io
import requests
from bs4 import BeautifulSoup
import time
# from IPython.core.display import display, HTML
load_dotenv()

s3client = boto3.client('s3',region_name='us-east-1',
                        aws_access_key_id = os.environ.get('AWS_ACCESS_KEY'),
                        aws_secret_access_key = os.environ.get('AWS_SECRET_KEY'))

bucket = 'noaa-goes18'
prefix = 'ABI-L1b-RadC/'


col1, col2 = st.columns(2)

with col1:
    st.write("Download file through field selection:")
    #Selecting Year
    year_nexrad = st.selectbox(
        'Please select the year',
        ('2022', '2023'))

    #Month of Year
    month_of_year_nexrad = st.text_input('Month of Year ', max_chars=2, type='default', 
                                    placeholder='Please enter Month of Year in MM format')

    #Day of Month
    day_of_month_nexrad = st.text_input('Enter Day of Month', max_chars=2, placeholder='Enter Date of Month in DD format')


    bucket = 'noaa-nexrad-level2'
    prefix = '{}/{}/{}/'.format(year_nexrad,month_of_year_nexrad,day_of_month_nexrad)

    #Station code selector 
    def display_stationcode(bucket_name,prefix):
        try:
            result = s3client.list_objects(Bucket=bucket_name, Prefix=prefix, Delimiter ='/')
            object_list = [x.get("Prefix").split("/")[-2] for x in result.get("CommonPrefixes")]
            selected_object = st.selectbox("Select station code:", object_list)
            return selected_object
        except Exception as e:
            st.write("An error occurred:", e)
            return None

    selected_stationcode = display_stationcode(bucket, prefix)

    if display_stationcode:
        st.write("You selected:", selected_stationcode)
    else:
        st.write("No objects found")

    #MADE CHANGES TO BELOW FUNCTION - ADDED PREFIX_FILE 
    prefix_file = '{}/{}/{}/{}/'.format(year_nexrad,month_of_year_nexrad,day_of_month_nexrad,selected_stationcode)
    #Filename selector 
    def list_files_as_dropdown(bucket_name, prefix):
        try:
            result = s3client.list_objects(Bucket=bucket_name, Prefix=prefix, Delimiter ='/')
            object_list = [x["Key"].split("/")[-1] for x in result["Contents"]]
            selected_object = st.selectbox("Select file for download:", object_list)
            return selected_object
        except Exception as e:
            st.write("An error occurred:", e)
            return None

    selected_file = list_files_as_dropdown(bucket, prefix_file)

    if selected_file:
        st.write("You selected:", selected_file)
    else:
        st.write("No objects found")

    # https://noaa-nexrad-level2.s3.amazonaws.com/index.html#2023/02/01/DOP1/
    #URL of file to be uploaded

    final_url = 'https://{}.s3.amazonaws.com/index.html#{}/{}/{}/{}/{}'.format(bucket,year_nexrad,month_of_year_nexrad,day_of_month_nexrad,selected_stationcode,selected_file)
    name_of_file = selected_file

    # check_file_exists
    def check_file_exists(filename, bucket_name):
        try:
            s3client.head_object(Bucket=bucket_name, Key=filename)
            return True
        except Exception as e:
            return False

    #Transfer file to S3 bucket
    def transfer_file_to_S3():
        try:
            st.write("Uploading the file to S3 bucket for download...")
            with open(selected_file, "wb") as data:
                data.write(requests.get(final_url).content)
                s3client.upload_file(selected_file, USER_BUCKET_NAME, name_of_file)
                with st.spinner('Almost there...'):
                    time.sleep(5)
                    st.write("File uploaded successfully")
            st.write('Click to download from S3 bucket', 'https://{}.s3.amazonaws.com/{}'.format(USER_BUCKET_NAME,name_of_file))
        except Exception as e:
            st.write("An error occurred:", str(e))

    #Transfering selected file to S3 bucket 
    if st.button('Submit'):
        with st.spinner('Retrieving details for the file you selected, wait for it....!'):
            time.sleep(5)
            if check_file_exists(name_of_file, USER_BUCKET_NAME):
                st.write(f"The file {name_of_file} already exists in the {USER_BUCKET_NAME} bucket.")
            else:
                st.write(f"The file {name_of_file} does not exist in the {USER_BUCKET_NAME} bucket.")
                transfer_file_to_S3()


with col2:

    # # filename_entered = st.text_input("Enter filename for download", placeholder='OR_ABI-L1b-RadC-M6C01_G18_s20230212001171_e20230212003548_c20230212003594.nc')
    # def generate_url_from_filename():
    #     # Get the filename entered by the user
    #     filename = st.text_input("Enter the filename:")
    #     if filename:
    #         if st.button("Go to website"):
    #             with st.spinner('Fetching link to file... '):
    #                 time.sleep(3)

    #                 # Base URL of the Nexrad website
    #                 base_url = "https://noaa-nexrad-level2.s3.amazonaws.com/index.html#"
                    
    #                 # Combine the base URL with the year, day of year, and hour to get the URL
    #                 file_url = base_url + filename
                    
    #                 # Display the URL
    #                 st.write("Access :", file_url)

    # generate_url_from_filename()

    # https://noaa-nexrad-level2.s3.amazonaws.com/index.html#2023/02/01/KABR/
    # https://noaa-nexrad-level2.s3.amazonaws.com/index.html2023/02/01/KABR/
    # KABR20230201_000458_V06

    def generate_url_from_filename():
        # Get the filename entered by the user
        filename = st.text_input("Enter the filename:")
        if filename:
            if st.button("Go to website"):
                with st.spinner('Fetching link to Nexrad bucket...'):
                    time.sleep(3)
                    # Split the filename into parts
                    parts = filename.split("_")
                    
                    # Get the year, day of year, and hour from the filename
                    # KABR20230201
                    station_code = parts[0][:4]
                    year = parts[0][4:8]
                    day_of_year = parts[0][8:10]
                    hour = parts[0][10:]
                    
                    # Base URL of the Nexrad website
                    base_url = "https://noaa-nexrad-level2.s3.amazonaws.com/index.html#{}/{}/{}/{}/".format(year,day_of_year,hour,station_code)
                    
                    # Combine the base URL with the year, day of year, and hour to get the URL
                    # file_url = base_url + f"{year}/{day_of_year}/{hour}/{station_code}/"
                    
                    # Display the URL
                    st.write("Access link:", base_url)

    generate_url_from_filename()
