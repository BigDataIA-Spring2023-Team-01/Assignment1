
import sqlite3
import pandas as pd


def query_into_dataframe():
    conn = sqlite3.connect("results/s3_nexrad.db")
    cursor = conn.cursor()
    df = pd.read_sql_query("SELECT * FROM folders", conn)
    conn.close()
    return df


def retieve_months(year):
    conn = sqlite3.connect("results/s3_nexrad.db")
    cursor = conn.cursor()
    query = "SELECT distinct month FROM folders where Is2023 = ?"
    tdf = pd.read_sql_query(query, conn, params=(year,))
    df = [x for x in tdf]
    conn.close()
    return tdf

def retieve_days(year,month):
    conn = sqlite3.connect("results/s3_nexrad.db")
    cursor = conn.cursor()
    query = "SELECT distinct day FROM folders where Is2023 = ? and month = ?"
    tdf = pd.read_sql_query(query, conn,params=(year,month))
    df = [x for x in tdf]
    conn.close()
    return tdf

def retieve_stations(year,month,day):
    conn = sqlite3.connect("results/s3_nexrad.db")
    cursor = conn.cursor()
    query = 'SELECT distinct nexrad_station FROM folders where Is2023 = ? and month = ? and day = ?'
    tdf = pd.read_sql_query(query, conn,params=(year,month,day))
    df = [x for x in tdf]
    conn.close()

    return tdf

df = retieve_stations('1','02','06')
print(df)