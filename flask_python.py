import contextlib
from flask import Flask, redirect, url_for, render_template, request
import sqlite3

app = Flask(__name__) #__name__ השם של קובץ ההרצה

# @app.route('/') #זה המסלול לדף הבית שאני רוצה לפתוח באינטרנט
# def first():
#     return 'Hello, yeso meeeee'


# @app.route('/home') #זה המסלול לדף הבית שאני רוצה לפתוח באינטרנט
# def home():
#     return render_template('index.html') ##פקודה שאומרת לפתוח את הדף אינדקס

# @app.route('/sign-in')
# def sign_in():
#     return render_template('sign-in.html')


@contextlib.contextmanager
def _get_cursor():
    conn = sqlite3.connect('Manual Database.db') 
    yield conn.cursor()
    conn.commit()
    conn.close()






















#Add new worker (post), get ALL workers info (get), update details (post), get one worker info (get)
@app.route("/worker", methods=['GET', 'POST'])
def get_workers():
    with _get_cursor() as cursor:
        if request.method == 'GET':
            all_workers_result = cursor.execute("select national_id_number, first_name, last_name from 'Worker'")
            workers = []
            for national_id_number, first_name, last_name in all_workers_result.fetchall():
                workers.append({
                    "id": national_id_number,
                    "first_name": first_name,
                    "last_name": last_name
                })
            return workers
        else:
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            national_id_number = request.form.get('national_id_number')
            try:
                cursor.execute('INSERT INTO "Worker"  (first_name, last_name, national_id_number) VALUES (?, ?, ?)', (first_name, last_name, national_id_number))
                return "INSERTED"
            except Exception as e:
                print(f"Failed to insert worker {first_name} {last_name} with id {national_id_number}")
                return "Failed to insert", 400

@app.route("/worker/<worker_national_id>", methods=['GET', 'POST'])
def get_worker_details(worker_national_id: str):
    with _get_cursor() as cursor:
        if request.method == 'GET':
            worker_result = cursor.execute('SELECT * FROM Worker WHERE national_id_number=?', (worker_national_id,)).fetchone()
            worker_national_id, first_name, last_name = worker_result
            worker_details = ({
                "id": worker_national_id,
                "first_name": first_name,
                "last_name": last_name
            })
            return worker_details
        else:
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            try:
                cursor.execute("""UPDATE Worker SET
                               first_name = ?,
                               last_name = ?
                               WHERE national_id_number=?""",
                               (first_name, last_name, worker_national_id))
                return "Worker updated"
            except Exception as e:
                print(f"Failed to update worker with id = {national_id_number}")
                return "Failed to insert", 400


















#Customers
@contextlib.contextmanager
def _get_cursor():
    conn = sqlite3.connect('Manual Database.db') 
    yield conn.cursor()
    conn.commit()
    conn.close()


@app.route("/customers", methods=['GET', 'POST'])
def get_customers():
    with _get_cursor() as cursor:
        if request.method == 'GET':
            all_customers_result = cursor.execute("SELECT * FROM 'Customers'")
            customers = []
            for id, name, phone_number, email, address, age in all_customers_result.fetchall():
                customers.append({
                    "id": id,
                    "name": name,
                    "phone_number": phone_number,
                    "email": email,
                    "address": address,
                    "age": age
                })
            return customers
        else:
            id = request.form.get('id')
            name = request.form.get('name')
            phone_number = request.form.get('phone_number')
            email = request.form.get('email')
            address = request.form.get('address')
            age = request.form.get('age')
            try:
                cursor.execute('INSERT INTO "Customers" (id, name, phone_number, email, address, age) VALUES (?, ?, ?, ?, ?, ?)', (id, name, phone_number, email, address, age))
                return "INSERTED"
            except Exception as e:
                print(f"Failed to insert worker {name} with id {id}")
                return "Failed to insert", 400

@app.route("/customers/<id>", methods=['GET', 'POST'])
def get_customer_details(id: str):
    with _get_cursor() as cursor:
        if request.method == 'GET':
            customer_result = cursor.execute('SELECT * FROM Customers WHERE id=?', (id,)).fetchone()
            id, name, phone_number, email, address, age = customer_result
            customer_details = ({
                "id": id,
                "first_name": name,
                "phone_number": phone_number,
                "email": email,
                "address": address,
                "age": age
            })
            return customer_details
        else:
            id = request.form.get('id')
            name = request.form.get('name')
            phone_number = request.form.get('phone')
            email = request.form.get('email')
            address = request.form.get('address')
            age = request.form.get('age')
            try:
                cursor.execute("""UPDATE Customers SET
                               name = ?,
                               phone_number = ?,
                               email = ?,
                               address = ?,
                               age = ?
                               WHERE id = ?""",
                               (name, phone_number, email, address, age, id))
                return "Customer updated"
            except Exception as e:
                print(f"Failed to update customer with id = {id}")
                return "Failed to insert", 400

























##Customer_Service
@contextlib.contextmanager
def _get_cursor():
    conn = sqlite3.connect('Manual Database.db') 
    yield conn.cursor()
    conn.commit()
    conn.close()


@app.route("/customersService", methods=['GET', 'POST'])
def get_customers_tickets():
    with _get_cursor() as cursor:
        if request.method == 'GET':
            all_customers_tickets_result = cursor.execute("SELECT * FROM 'CustomerService'")
            customers_tickets = []
            for ticket_id, sale_id, details, resolved_by, worker_id, timestamp, status in all_customers_tickets_result.fetchall():
                customers_tickets.append({
                    "ticket_id": ticket_id,
                    "sale_id": sale_id,
                    "details": details,
                    "resolved_by": resolved_by,
                    "worker_id": worker_id,
                    "timestamp": timestamp,
                    "status": status
                })
            return customers_tickets
        else: ##ERROR
            breakpoint()
            ticket_id = request.form.get('ticket_id')
            sale_id = request.form.get('sale_id')
            details = request.form.get('details')
            resolved_by = request.form.get('resolved_by')
            worker_id = request.form.get('worker_id')
            timestamp = request.form.get('timestamp')
            status = request.form.get('status')
            try:
                cursor.execute('INSERT INTO "CustomersService" (ticket_id, sale_id, details, resolved_by, worker_id, timestamp, status) VALUES (?, ?, ?, ?, ?, ?, ?)', (ticket_id, sale_id, details, resolved_by, worker_id, timestamp, status))
                return "INSERTED"
            except Exception as e:
                print(f"Failed to open new ticket for sale number {sale_id}")
                return "Failed to insert", 400


@app.route("/customersService/<id>", methods=['GET', 'POST'])
def get_customer_tickets(id: str):
    with _get_cursor() as cursor:
        if request.method == 'GET':
            ticket_result = cursor.execute('SELECT * FROM Customers WHERE id=?', (id,)).fetchone()
            ticket_id, sale_id, details, resolved_by, worker_id, timestamp, status = ticket_result
            customer_details = ({
                "ticket_id": ticket_id,
                "sale_id": sale_id,
                "details": details,
                "resolved_by": resolved_by,
                "worker_id": worker_id,
                "timestamp": timestamp,
                "status": status
            })
            return customer_details
        else:
            details = request.form.get('id')
            resolved_by = request.form.get('name')
            worker_id = request.form.get('phone')
            status = request.form.get('email')
            try:
                cursor.execute("""UPDATE Customers SET
                               details = ?,
                               resolved_by = ?,
                               worker_id = ?,
                               status = ? """,
                               (details, resolved_by, worker_id, status))
                return "Ticket is updated"
            except Exception as e:
                print(f"Failed to update ticked with id = {ticket_id}")
                return "Failed to insert", 400











# @app.route("")

# @app.route('/manager-view') 
# def manager_view():
#     return render_template('manager-view.html')

# @app.route('/customer-service-view')
# def customer_service_view():
#     return render_template('customer-service-view.html')

# @app.route('/worker_ticket')
# def worker_tickets():
#     return render_template('my-ticket.html')

# the below is called endpoint --- 
@app.route('/new-ticket')
def new_ticket():
    return 'Open new ticket here'


if __name__ == '__main__':
    # connet to SQLite DB 
    # make endpoit with POST method to register a new worker, use the SQLite3 cursor to put the row in the DB.
    app.run(debug=True, port=5002)

#http://127.0.0.1:5000/
#http://127.0.0.1:5002/
#http://127.0.0.1:5002/home
#http://127.0.0.1:5002/sign-in
#http://127.0.0.1:5002/manager-view
#http://127.0.0.1:5002/customer-service-view
#http://127.0.0.1:5002/worker_ticket
#http://127.0.0.1:5002/new-ticket
