
import sqlite3
import pandas as pd



conn = sqlite3.connect("s3_goes.db")
cursor = conn.cursor()


def query_into_dataframe():
    conn = sqlite3.connect("s3_goes.db")
    cursor = conn.cursor()
    df = pd.read_sql_query("SELECT * FROM folders", conn)
    print(df)
    conn.close()

def retieve_year():
    conn = sqlite3.connect("results/s3_goes.db")
    cursor = conn.cursor()
    query = "SELECT distinct year FROM folders"
    tdf = pd.read_sql_query(query, conn)
    df = [x for x in tdf]
    conn.close()
    return tdf


def retieve_day_of_year(year):
    conn = sqlite3.connect("results/s3_goes.db")
    cursor = conn.cursor()
    query = "SELECT distinct day_of_year FROM folders where year = ?"
    tdf = pd.read_sql_query(query, conn,params=(year,))
    df = [x for x in tdf]
    conn.close()
    return tdf

def retieve_hour(year,day_of_year):
    conn = sqlite3.connect("results/s3_goes.db")
    cursor = conn.cursor()
    query = "SELECT distinct hour FROM folders where year = ? and day_of_year = ?"
    tdf = pd.read_sql_query(query, conn,params=(year,day_of_year))
    df = [x for x in tdf]
    conn.close()
    print(tdf)
    return tdf

df = retieve_hour('2023','001')
print(df)