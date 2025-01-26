import psycopg2
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
            price VARCHAR(20) ,
            one_hour_change VARCHAR(20) ,
            twenty_four_hour_change VARCHAR(20) ,
            seven_day_change VARCHAR(20) ,
            twenty_four_hour_volume VARCHAR(20) ,
            market_cap VARCHAR(20) 
        );'''
        
        cur.execute(create_script)
        
        
        insert_script = '''INSERT INTO crypto_data (serial_no, coin_name, price, one_hour_change, twenty_four_hour_change, seven_day_change, twenty_four_hour_volume, market_cap) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''

        insert_value = ("1", 'Bitcoin', '1', '2', '3', '4', '5', '6')

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




