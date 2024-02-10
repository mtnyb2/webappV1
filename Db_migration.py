import sqlite3

def create_worker_table(cursor):
    statement = """CREATE TABLE Worker (national_id_number CHARACTER(10) PRIMARY KEY,
                   first_name VARCHAR(255),
                   last_name VARCHAR(255)
                   );"""
    cursor.execute(statement)


def create_customer_table(cursor):
    statement = """CREATE TABLE Customers (id CHARACTER(10) PRIMARY KEY,
                    name VARCHAR(255),
                    phone_number CHARACTER(10),
                    email VARCHAR(255),
                    address VARCHAR(255),
                    age SMALLINT
                    );"""
    cursor.execute(statement)

# def delete_table(cursor, table_name):
#     statement = """DROP TABLE ?""", (table_name)
#     cursor(statement)
#     print (table_name + "dropped")

def create_customer_service_table(cursor):
    statement = """CREATE TABLE CustomerService(
                ticket_id BIGINT,
                sale_id BIGINT, 
                details TEXT, 
                resolved_by TEXT, 
                worker_id CHARACTER(10), 
                timestamp TEXT,
                status CHARACTER(64),
                FOREIGN KEY ("worker_id") REFERENCES "Worker" ("id")
                );"""
    cursor.execute(statement)

def create_online_sellings(cursor):
    statement = """CREATE TABLE OnlineSelling ( id BIGINT PRIMARY KEY,
                    item_id BIGINT,
                    costumer_id CHARACTER(10),
                    sending_id VARCHAR(255),
                    sale_price REAL,
                    sale_timestamp TEXT,
                    FOREIGN KEY (costumer_id) REFERENCES "Customers" ("id")
                    );"""
    cursor.execute(statement)

def create_repairing_items(cursor):
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

def main():
    conn = sqlite3.connect('Manual Database.db') 
    cursor = conn.cursor()
    # create_worker_table(cursor)
    # create_customer_table(cursor)
    # create_customer_service_table(cursor)
    # create_online_sellings(cursor)
    # create_repairing_items(cursor)

if __name__ == "__main__":
    main()