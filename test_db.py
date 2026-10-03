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
            sql = """SELECT equipment_id, item_name, quantity, location FROM equipment WHERE location = %s ORDER BY equipment_id;"""
            cursor.execute(sql, (location,))
            records = cursor.fetchall()
            return records

    finally:
        connection.close()
        print("Connection closed.")

# Main Program Execution

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



# ACTIVITY 4

def add_equipment():
    connection = get_connection()

    try:
        equipment_id = int(input("Enter Equipment ID: "))
        item_name = input("Enter Item Name: ").strip()
        category = input("Enter Category: ").strip()
        quantity = int(input("Enter Quantity: "))
        unit_price = float(input("Enter Unit Price: "))
        location = input("Enter Location (Lab A / Lab B / Stockroom): ").strip()
        note = input("Enter Note: ").strip()

        if note == "":
            note = None

        with connection.cursor() as cursor:
            sql = """
                INSERT INTO equipment
                (equipment_id, item_name, category, quantity, unit_price, location, note)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            cursor.execute(
                sql,
                (
                    equipment_id,
                    item_name,
                    category,
                    quantity,
                    unit_price,
                    location,
                    note
                )
            )

            connection.commit()

            print("\nEquipment added successfully.")

    except ValueError:
        print("Invalid input. Equipment ID and Quantity must be whole numbers, and Unit Price must be a number.")

    except pymysql.MySQLError as error:
        connection.rollback()
        print("Database error:", error)

    finally:
        connection.close()
        print("Connection closed.")


add_equipment()

