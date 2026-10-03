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

# ACTIVITY 3

def filter_by_location(location):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            sql = """SELECT equipment_id, item_name, quantity, location
                     FROM equipment
                     WHERE location = %s
                     ORDER BY equipment_id;"""
            cursor.execute(sql, (location,))
            records = cursor.fetchall()
            return records

    finally:
        connection.close()
        print("Connection closed.")


location = input("Enter Location (Lab A / Lab B / Stockroom): ").strip()

try:
    equipment_records = filter_by_location(location)

    if equipment_records:
        print(f"\nEQUIPMENT IN {location}")
        print(f"{'ID':<5} {'Item':<28} {'Qty':>5} {'Location'}")

        for record in equipment_records:
            equipment_id, item_name, quantity, item_location = record
            print(f"{equipment_id:<5} {item_name:<28} {quantity:>5} {item_location}")

        print(f"\nMatching equipment records: {len(equipment_records)}")

    else:
        print("No Equipment")

except pymysql.MySQLError as error:
    print("Database error:", error)

