import psycopg2
import csv

def connect():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="password",
            port="5432"
        )
        print("[INFO] Connected to database")
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print("[ERROR] Connection failed:", error)
        return None


def createTable(cursor):
    query = """
        CREATE TABLE IF NOT EXISTS phonebook2 (
            id SERIAL PRIMARY KEY,
            phone VARCHAR(11),
            name VARCHAR(255) UNIQUE
        );
    """
    cursor.execute(query)


def call_insert_or_update(cursor, name, phone):
    cursor.execute("CALL insert_or_update_user(%s, %s)", (name, phone))


def call_insert_many(cursor, names, phones):
    cursor.execute("SELECT * FROM insert_many_users(%s, %s)", (names, phones))
    invalids = cursor.fetchall()
    if invalids:
        print("[INVALID ENTRIES]")
        for name, phone in invalids:
            print(f"{name}: {phone}")
    else:
        print("[ALL ENTRIES VALID]")


def call_search_pattern(cursor, pattern):
    cursor.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
    results = cursor.fetchall()
    print("[PATTERN MATCHES]")
    for row in results:
        print(row)


def call_paginated(cursor, limit, offset):
    cursor.execute("SELECT * FROM get_phonebook_paginated(%s, %s)", (limit, offset))
    results = cursor.fetchall()
    print("[PAGINATED RESULTS]")
    for row in results:
        print(row)


def call_delete_user(cursor, input_value):
    cursor.execute("CALL delete_user(%s)", (input_value,))
    print(f"[DELETED]: {input_value}")


def getTable(cursor):
    cursor.execute("SELECT * FROM phonebook2")
    rows = cursor.fetchall()
    print("\n[CURRENT PHONEBOOK ENTRIES]")
    for row in rows:
        print(row)


# MAIN PROGRAM
conn = connect()
if conn is None:
    exit()

cursor = conn.cursor()
createTable(cursor)

print("Type of query: insert, insertbycsv, pattern, paginate, delete")
typ = input().strip()

if typ == "insert":
    name = input("Name: ")
    phone = input("Phone: ")
    call_insert_or_update(cursor, name, phone)

elif typ == "insertmany":
    n = int(input("How many users? "))
    names, phones = [], []
    for _ in range(n):
        name = input("Name: ")
        phone = input("Phone: ")
        names.append(name)
        phones.append(phone)
    call_insert_many(cursor, names, phones)

elif typ == "insertbycsv":
    csv_name = input("CSV file name (without .csv): ")
    names, phones = [], []
    try:
        with open(f"data/{csv_name}.csv", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            for row in reader:
                name, phone = row[0].split(';')
                names.append(name)
                phones.append(phone)
        call_insert_many(cursor, names, phones)
    except Exception as e:
        print(f"[ERROR] Failed to load CSV: {e}")

elif typ == "pattern":
    pattern = input("Enter search pattern: ")
    call_search_pattern(cursor, pattern)

elif typ == "paginate":
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))
    call_paginated(cursor, limit, offset)

elif typ == "delete":
    val = input("Enter name or phone to delete: ")
    call_delete_user(cursor, val)

conn.commit()
getTable(cursor)
cursor.close()
conn.close()
