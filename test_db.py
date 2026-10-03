import pymysql


def get_connection():
    connection = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        database="pup_dbms2_day1",
        charset="utf8mb4",
        connect_timeout=5
    )

    return connection


connection = None

try:
    connection = get_connection()
    print("Connected successfully!")

    with connection.cursor() as cursor:
        cursor.execute("SELECT DATABASE();")
        result = cursor.fetchone()

        print("Database:", result[0])

except pymysql.MySQLError as error:
    print("Database error:", error)

finally:
    if connection is not None:
        connection.close()
        print("Connection closed.")