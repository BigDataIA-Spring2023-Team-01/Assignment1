import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, date
import os
import boto3
import logging
# from dotenv import load_dotenv
import io
import requests
from bs4 import BeautifulSoup
import time
# from IPython.core.display import display, HTML

col1, col2 = st.columns(2)

with col1:
    #Selecting station 
    station_geos = st.text_input(
        'Please select the station', placeholder= 'GEOS 18')

    #Selecting Year
    year_geos = st.selectbox(
        'Please select the year',
        ('2022', '2023'))


    #Day of Year
    day_of_year_geos = st.text_input('Day of Year ', max_chars=3, type='default', 
                                    placeholder='Please enter Date of Year in DDD format ')

    #Hour of Day
    hour_of_day = st.text_input('Enter Hour of Day', max_chars=2, placeholder='Enter Hour in 24H format')

    bucket = 'noaa-goes18'
    prefix = 'ABI-L1b-RadC/{}/{}/{}/'.format(year_geos,day_of_year_geos,hour_of_day)


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

    selected_file = list_files_as_dropdown(bucket, prefix)

    if selected_file:
        st.write("You selected:", selected_file)
    else:
        st.write("No objects found")

    # https://noaa-goes18.s3.amazonaws.com/index.html#ABI-L1b-RadC/2023/001/00/
    final_url = 'https://{}.s3.amazonaws.com/index.html#ABI-L1b-RadC/{}/{}/{}/{}'.format(bucket,year_geos,day_of_year_geos,hour_of_day,selected_file)
    name_of_file = selected_file

    # check_file_exists
    def check_file_exists(filename, bucket_name):
        try:
            s3client.head_object(Bucket=bucket_name, Key=filename)
            return True
        except Exception as e:
            return False


    def get_file_url(year, day_of_year, hour):
        # Base URL of the GEOS website
        base_url = "https://noaa-goes18.s3.amazonaws.com/index.html#ABI-L1b-RadC/"
        
        # Year, day of year, and hour are formatted as strings with leading zeros
        year = str(year).zfill(4)
        day_of_year = str(day_of_year).zfill(3)
        hour = str(hour).zfill(2)
        
        # Combine the base URL with the user inputs to get the file URL
        file_url = base_url + f"{year}/{day_of_year}/{hour}"
        
        st.write("Link to file on GEOS website ",file_url) 


    #Transfer file to S3 bucket
    def transfer_file_to_S3():
        try:
            
            st.write("Uploading the file to S3 bucket for download...")
            with open(selected_file, "wb") as data:
                data.write(requests.get(final_url).content)
                s3client.upload_file(selected_file, USER_BUCKET_NAME, name_of_file)
                with st.spinner('Wait for it...'):
                    time.sleep(7)
                    st.write("File uploaded successfully")
            st.write('Click to download from S3 bucket', 'https://{}.s3.amazonaws.com/{}'.format(USER_BUCKET_NAME,name_of_file))
        except Exception as e:
            st.write("An error occurred:", str(e))

    #Transfering selected file to S3 bucket 
    if st.button('Submit'):
        with st.spinner('Retrieving details for the file you selected, wait for it....!'):
            time.sleep(5)
            if check_file_exists(name_of_file, USER_BUCKET_NAME):
                st.write(f"The file {name_of_file} already exists in the S3: {USER_BUCKET_NAME} bucket.")
                st.write('Click to download from S3 bucket', 'https://{}.s3.amazonaws.com/{}'.format(USER_BUCKET_NAME,name_of_file))
            else:
                st.write(f"The file {name_of_file} does not exist in the S3: {USER_BUCKET_NAME} bucket.")
                transfer_file_to_S3()
                get_file_url(year_geos,day_of_year_geos,hour_of_day)

with col2:

    # filename_entered = st.text_input("Enter filename for download", placeholder='OR_ABI-L1b-RadC-M6C01_G18_s20230212001171_e20230212003548_c20230212003594.nc')
    
    def generate_url_from_filename():
        # Get the filename entered by the user
        filename = st.text_input("Enter the filename:")
        if filename:
            if st.button("Go to website"):
                with st.spinner('Fetching link to GEOS bucket...'):
                    time.sleep(3)
                    # Split the filename into parts
                    parts = filename.split("_")
                    
                    # Get the year, day of year, and hour from the filename
                    year = parts[5][1:5]
                    day_of_year = parts[5][5:8]
                    hour = parts[5][8:10]
                    
                    # Base URL of the GEOS website
                    base_url = "https://noaa-goes18.s3.amazonaws.com/index.html#ABI-L1b-RadC/"
                    
                    # Combine the base URL with the year, day of year, and hour to get the URL
                    file_url = base_url + f"{year}/{day_of_year}/{hour}/"
                    
                    # Display the URL
                    st.write("Access link:", file_url)

    generate_url_from_filename()





