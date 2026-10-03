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


def get_equipment():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            sql = """SELECT equipment_id, item_name, quantity, location FROM equipment ORDER BY equipment_id"""
            cursor.execute(sql)
            records = cursor.fetchall()

            for record in records:
                print(record)

    finally:
        connection.close()
        print("Connection closed.")


get_equipment()
