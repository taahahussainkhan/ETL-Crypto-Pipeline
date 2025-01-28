import psycopg2
# from dotenv import load_dotenv
import os

# from scrappers.coingecko import scrape_gecko

hostname = 'localhost'
database = 'crypto_data'
username = 'postgres'
password = 'taaha'
port = 5432


def insert_data(data):

    conn = None
    cur = None

    # data = scrape_gecko()

    try:
        conn = psycopg2.connect(
            host=hostname,
            database=database,
            user=username,
            password=password,
            port=port
        )

        cur = conn.cursor()

        create_script = '''CREATE TABLE IF NOT EXISTS crypto_data (
            serial_no  INT,
            coin_name  VARCHAR(20),
            price VARCHAR(30) ,
            one_hour_change VARCHAR(30) ,
            twenty_four_hour_change VARCHAR(30) ,
            seven_day_change VARCHAR(30) ,
            twenty_four_hour_volume VARCHAR(30) ,
            market_cap VARCHAR(30) ,
            source VARCHAR(20)
        );'''
        
        cur.execute(create_script)
        
        
        insert_script = '''INSERT INTO crypto_data (serial_no, coin_name, price, one_hour_change, twenty_four_hour_change, seven_day_change, twenty_four_hour_volume, market_cap, source) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)'''


        cur.execute(insert_script, data)
        
        conn.commit()
        print("Database connection successful!")

    except Exception as e:
        print("Database connection failed",e)

    finally:
        if conn is not None:
            cur.close()
        if cur is not None:
            conn.close()




