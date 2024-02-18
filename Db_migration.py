# import sqlite3

# def create_worker_table(cursor):
#     statement = """CREATE TABLE Worker (national_id_number CHARACTER(10) PRIMARY KEY,
#                    first_name VARCHAR(255),
#                    last_name VARCHAR(255)
#                    );"""
#     cursor.execute(statement)



# def create_customer_table(cursor):
#     statement = """CREATE TABLE Customers (id CHARACTER(10) PRIMARY KEY,
#                     name VARCHAR(255),
#                     phone_number CHARACTER(10),
#                     email VARCHAR(255),
#                     address VARCHAR(255),
#                     age SMALLINT
#                     );"""
#     cursor.execute(statement)

# def delete_table(cursor, table_name):
#     statement = """DROP TABLE ? ;""", (table_name)
#     cursor.execute(statement)
#     print (f"{table_name} dropped")

# def create_customer_service_table(cursor):
#     statement = """CREATE TABLE CustomerService(
#                 ticket_id BIGINT,
#                 sale_id BIGINT, 
#                 details TEXT, 
#                 resolved_by TEXT, 
#                 worker_id CHARACTER(10), 
#                 timestamp TEXT,
#                 status CHARACTER(64),
#                 FOREIGN KEY ("worker_id") REFERENCES "Worker" ("id")
#                 );"""
#     cursor.execute(statement)

# def create_online_sellings(cursor):
#     statement = """CREATE TABLE OnlineSelling ( id BIGINT PRIMARY KEY,
#                     item_id BIGINT,
#                     costumer_id CHARACTER(10),
#                     sending_id VARCHAR(255),
#                     sale_price REAL,
#                     sale_timestamp TEXT,
#                     FOREIGN KEY (costumer_id) REFERENCES "Customers" ("id")
#                     );"""
#     cursor.execute(statement)

# def create_repairing_items(cursor):
#     statement = """CREATE TABLE RepairingItems (item_id BIGINT PRIMARY KEY,
#                     makat_id INT,
#                     manufacturer_name VARCHAR(255),
#                     model VARCHAR(255),
#                     case_type CHARACTER(15),
#                     processor VARCHAR(255),
#                     RAM VARCHAR(255),
#                     optical_drive VARCHAR(255),
#                     OS VARCHAR(255),
#                     id_technician CHARACTER(10),
#                     repairing_item_date TEXT
#                     );"""
#     cursor.execute(statement)


# def main():
#     conn = sqlite3.connect('Manual Database.db') 
#     cursor = conn.cursor()
#     create_worker_table(cursor)
#     create_customer_table(cursor)
#     create_customer_service_table(cursor)
#     create_online_sellings(cursor)
#     create_repairing_items(cursor)



##########################################################


import sqlite3

def table_exists(cursor, table_name):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    exists = cursor.fetchone() is not None
    if exists:
        print(f"Table {table_name} already exists, skipped")
    return exists

def create_worker_table(cursor):
    if not table_exists(cursor, 'Worker'):
        statement = """CREATE TABLE Worker (national_id_number CHARACTER(10) PRIMARY KEY,
                       first_name VARCHAR(255),
                       last_name VARCHAR(255)
                       );"""
        cursor.execute(statement)
        print("Table Worker created")

def create_customer_table(cursor):
    if not table_exists(cursor, 'Customers'):
        statement = """CREATE TABLE Customers (id CHARACTER(10) PRIMARY KEY,
                        name VARCHAR(255),
                        phone_number CHARACTER(10),
                        email VARCHAR(255),
                        address VARCHAR(255),
                        age SMALLINT
                        );"""
        cursor.execute(statement)
        print("Table Customers created")

def delete_table(table_name, cursor):
    # Adjusted for proper execution with SQL command
    if table_exists(table_name, cursor):
        cursor.execute(f"DROP TABLE {table_name};")  # Caution: Directly formatting SQL commands carries injection risk.
        print(f"{table_name} dropped")

def create_customer_service_table(cursor):
    if not table_exists(cursor, 'CustomerService'):
        statement = """CREATE TABLE CustomerService(
                    ticket_id BIGINT,
                    sale_id BIGINT, 
                    details TEXT, 
                    resolved_by TEXT, 
                    worker_id CHARACTER(10), 
                    timestamp TEXT,
                    status CHARACTER(64),
                    FOREIGN KEY ("worker_id") REFERENCES "Worker" ("national_id_number")
                    );"""
        cursor.execute(statement)
        print("Table CustomerService created")

def create_online_sellings(cursor):
    if not table_exists(cursor, 'OnlineSelling'):
        statement = """CREATE TABLE OnlineSelling ( id BIGINT PRIMARY KEY,
                        item_id BIGINT,
                        costumer_id CHARACTER(10),
                        sending_id VARCHAR(255),
                        sale_price REAL,
                        sale_timestamp TEXT,
                        FOREIGN KEY (costumer_id) REFERENCES "Customers" ("id")
                        );"""
        cursor.execute(statement)
        print("Table OnlineSelling created")

def create_repairing_items(cursor):
    if not table_exists(cursor, 'RepairingItems'):
        statement = """CREATE TABLE RepairingItems (item_id BIGINT PRIMARY KEY,
                        makat_id INT,
                        manufacturer_name VARCHAR(255),
                        model VARCHAR(255),
                        case_type CHARACTER(15),
                        processor VARCHAR(255),
                        RAM VARCHAR(255),
                        optical_drive VARCHAR(255),
                        OS VARCHAR(255),
                        id_technician CHARACTER(10),
                        repairing_item_date TEXT
                        );"""
        cursor.execute(statement)
        print("Table RepairingItems created")

def main():
    conn = sqlite3.connect('Manual Database.db') 
    cursor = conn.cursor()
    create_worker_table(cursor)
    create_customer_table(cursor)
    create_customer_service_table(cursor)
    create_online_sellings(cursor)
    create_repairing_items(cursor)
    conn.commit()
    conn.close()
    

##########################################################




if __name__ == "__main__":
    main()