import psycopg2
try:
    conn = psycopg2.connect(database="e_commerce",
                            host="localhost",
                            user="postgres",
                            password="root123",
                            port="5432")

    cursor = conn.cursor()
except Exception as error:
    print(error)



