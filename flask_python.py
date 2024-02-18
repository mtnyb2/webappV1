import contextlib
from flask import Flask, redirect, url_for, render_template, request, jsonify
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





# #WORKER args
# @contextlib.contextmanager
# def _get_cursor():
#     conn = sqlite3.connect('Manual Database.db') 
#     yield conn.cursor()
#     conn.commit()
#     conn.close()


# @app.route("/'worker'", methods=['GET', 'POST'])
# def get_customers():
#     with _get_cursor() as cursor:
#         if request.method == 'GET':
#             args = request.args
#             if not args:
#                 all_customers_result = cursor.execute("SELECT * FROM 'Customers'")
#                 customers = []
#                 for id, name, fname, city, address, phone_num, email, gender, department, role, cared_by, emergency_contact_name, emergency_contact_phone in all_customers_result.fetchall():
#                     customers.append({
#                         "id": id,
#                         "name": name,
#                         "fname": fname,
#                         "city": city,
#                         "address": address,
#                         "phone_num": phone_num,
#                         "email": email,
#                         "gender": gender,
#                         "department": department,
#                         "role": role,
#                         "cared_by": cared_by,
#                         "emergency_contact_name": emergency_contact_name,
#                         "emergency_contact_phone": emergency_contact_phone
#                     })
#             else:
#                 query_parts = []
#                 values = []
#                 for key in args.keys():
#                     if key in ['gender', 'department', 'role', 'cared_by']:
#                         query_parts.append(f"{key} = ?")
#                         values.append(args[key])
#                 query_string = " AND ".join(query_parts)
#                 sql_query = f"SELECT * FROM Customers"
#                 if query_parts:
#                     sql_query += f" WHERE {query_string}"
#                 cursor.execute(sql_query, values)
#                 customers = cursor.fetchall()
#                 return customers
#         else:
#             id = request.form.get('id')
#             name = request.form.get('name')
#             fname = request.form.get('fname')
#             city = request.form.get('city')
#             address = request.form.get('address')
#             phone_num = request.form.get('phone_num')
#             email = request.form.get('email')
#             gender = request.form.get('gender')
#             department = request.form.get('department')
#             role = request.form.get('role')
#             cared_by = request.form.get('cared_by')
#             emergency_contact_name = request.form.get('emergency_contact_name')
#             emergency_contact_phone = request.form.get('emergency_contact_phone')
#             try:
#                 cursor.execute('INSERT INTO "worker" (id, name, fname, city, address, phone_num, email, gender, department, role, cared_by, emergency_contact_name, emergency_contact_phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (id, name, fname, city, address, phone_num, email, gender, department, role, cared_by, emergency_contact_name, emergency_contact_phone))
#                 return "INSERTED"
#             except Exception as e:
#                 print(f"Failed to insert worker {name} {fname} with id {id}")
#                 return "Failed to insert", 400

@app.route("/worker/<id>", methods=['GET', 'POST'])
def get_worker_details(id: str):
    with _get_cursor() as cursor:
        if request.method == 'GET':
            worker_result = cursor.execute('SELECT * FROM worker WHERE id=?', (id,)).fetchone()
            id, name, fname, city, address, phone_num, email, gender, department, role, cared_by, emergency_contact_name, emergency_contact_phone = worker_result
            worker_details = ({
                "id": id,
                "name": name,
                "fname": fname,
                "city": city,
                "phone_num": phone_num,
                "gender": gender,
                "department":  department,
                "role": role,
                "cared_by": cared_by,
                "emergency_contact_name": emergency_contact_name,
                "emergency_contact_phone": emergency_contact_phone
            })
            return worker_details
        else:
            id = request.form.get('id')
            name = request.form.get('name')
            fname = request.form.get('fname')
            city = request.form.get('city')
            address = request.form.get('address')
            phone_num = request.form.get('phone_num')
            email = request.form.get('email')
            gender = request.form.get('gender')
            department = request.form.get('department')
            role = request.form.get('role')
            cared_by = request.form.get('cared_by')
            emergency_contact_name = request.form.get('emergency_contact_name')
            emergency_contact_phone = request.form.get('emergency_contact_phone')
            try:
                cursor.execute("""UPDATE worker SET
                                id = ?,
                                name = ?,
                                fname = ?,
                                city = ?,
                                address = ?,
                                phone_num = ?,
                                email = ?,
                                gender = ?,
                                department = ?
                                role = ?,
                                cared_by= ?,
                                emergency_contact_name = ?,
                                emergency_contact_phone = ?""",
                                (id, name, fname, city, address, phone_num, email, gender, department, role, cared_by, emergency_contact_name, emergency_contact_phone))
                return "Worker updated"
            except Exception as e:
                print(f"Failed to update worker {name} {fname} with id = {id}")
                return "Failed to insert", 400
















# @app.route("/worker", methods=['GET', 'POST'])
# def get_workers():
#     with _get_cursor() as cursor:
#         if request.method == 'GET':
#             all_workers_result = cursor.execute("select national_id_number, first_name, last_name from 'Worker'")
#             workers = []
#             for national_id_number, first_name, last_name in all_workers_result.fetchall():
#                 workers.append({
#                     "id": national_id_number,
#                     "first_name": first_name,
#                     "last_name": last_name
#                 })
#             return workers
#         else:
#             first_name = request.form.get('first_name')
#             last_name = request.form.get('last_name')
#             national_id_number = request.form.get('national_id_number')
#             try:
#                 cursor.execute('INSERT INTO "Worker"  (first_name, last_name, national_id_number) VALUES (?, ?, ?)', (first_name, last_name, national_id_number))
#                 return "INSERTED"
#             except Exception as e:
#                 print(f"Failed to insert worker {first_name} {last_name} with id {national_id_number}")
#                 return "Failed to insert", 400

# @app.route("/worker/<worker_national_id>", methods=['GET', 'POST'])
# def get_worker_details(worker_national_id: str):
#     with _get_cursor() as cursor:
#         if request.method == 'GET':
#             worker_result = cursor.execute('SELECT * FROM Worker WHERE national_id_number=?', (worker_national_id,)).fetchone()
#             worker_national_id, first_name, last_name = worker_result
#             worker_details = ({
#                 "id": worker_national_id,
#                 "first_name": first_name,
#                 "last_name": last_name
#             })
#             return worker_details
#         else:
#             first_name = request.form.get('first_name')
#             last_name = request.form.get('last_name')
#             try:
#                 cursor.execute("""UPDATE Worker SET
#                                first_name = ?,
#                                last_name = ?
#                                WHERE national_id_number=?""",
#                                (first_name, last_name, worker_national_id))
#                 return "Worker updated"
#             except Exception as e:
#                 print(f"Failed to update worker with id = {national_id_number}")
#                 return "Failed to insert", 400



















# #Customers args not GPT
# @contextlib.contextmanager
# def _get_cursor():
#     conn = sqlite3.connect('Manual Database.db') 
#     yield conn.cursor()
#     conn.commit()
#     conn.close()


# @app.route("/customers", methods=['GET', 'POST'])
# def get_customers():
#     with _get_cursor() as cursor:
#         if request.method == 'GET':
#             args = request.args
#             if not args:
#                 all_customers_result = cursor.execute("SELECT * FROM 'Customers'")
#                 customers = []
#                 for id, name, phone_number, email, address, age in all_customers_result.fetchall():
#                     customers.append({
#                         "id": id,
#                         "name": name,
#                         "phone_number": phone_number,
#                         "email": email,
#                         "address": address,
#                         "age": age
#                     })
#             else:
#                 query_parts = []
#                 values = []
#                 for key in args.keys():
#                     if key in ['name', 'phone_number', 'email', 'address', 'age']:
#                         query_parts.append(f"{key} = ?")
#                         values.append(args[key])
#                 query_string = " AND ".join(query_parts)
#                 sql_query = f"SELECT * FROM Customers"
#                 if query_parts:
#                     sql_query += f" WHERE {query_string}"
#                 cursor.execute(sql_query, values)
#                 customers = cursor.fetchall()
#                 return customers
#         else:
#             id = request.form.get('id')
#             name = request.form.get('name')
#             phone_number = request.form.get('phone_number')
#             email = request.form.get('email')
#             address = request.form.get('address')
#             age = request.form.get('age')
#             try:
#                 cursor.execute('INSERT INTO "Customers" (id, name, phone_number, email, address, age) VALUES (?, ?, ?, ?, ?, ?)', (id, name, phone_number, email, address, age))
#                 return "INSERTED"
#             except Exception as e:
#                 print(f"Failed to insert worker {name} with id {id}")
#                 return "Failed to insert", 400

# @app.route("/customers/<id>", methods=['GET', 'POST'])
# def get_customer_details(id: str):
#     with _get_cursor() as cursor:
#         if request.method == 'GET':
#             customer_result = cursor.execute('SELECT * FROM Customers WHERE id=?', (id,)).fetchone()
#             id, name, phone_number, email, address, age = customer_result
#             customer_details = ({
#                 "id": id,
#                 "first_name": name,
#                 "phone_number": phone_number,
#                 "email": email,
#                 "address": address,
#                 "age": age
#             })
#             return customer_details
#         else:
#             id = request.form.get('id')
#             name = request.form.get('name')
#             phone_number = request.form.get('phone')
#             email = request.form.get('email')
#             address = request.form.get('address')
#             age = request.form.get('age')
#             try:
#                 cursor.execute("""UPDATE Customers SET
#                                name = ?,
#                                phone_number = ?,
#                                email = ?,
#                                address = ?,
#                                age = ?
#                                WHERE id = ?""",
#                                (name, phone_number, email, address, age, id))
#                 return "Customer updated"
#             except Exception as e:
#                 print(f"Failed to update customer with id = {id}")
#                 return "Failed to insert", 400


#GPT:
from flask import Flask, request, jsonify, render_template
import sqlite3
import contextlib

app = Flask(__name__)

# Customers args
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
            args = request.args
            if not args:
                all_customers_result = cursor.execute("SELECT * FROM 'Customers'")
                customers = [dict(id=row[0], name=row[1], phone_number=row[2], email=row[3], address=row[4], age=row[5]) for row in all_customers_result.fetchall()]
                return jsonify(customers)
            else:
                if 'search' in args:
                    the_query = "SELECT * FROM 'Customers' customer where customer.name || customer.phone_number || customer.email || customer.address || customer.age like (?)"
                    all_customers_result = cursor.execute(the_query, (f"%{args['search']}%",))
                    customers = [dict(id=row[0], name=row[1], phone_number=row[2], email=row[3], address=row[4], age=row[5]) for row in all_customers_result.fetchall()]
                    return customers
                else:
                    query_parts = []
                    values = []
                    for key in args.keys():
                        if key in ['name', 'phone_number', 'email', 'address', 'age']:
                            query_parts.append(f"{key} = ?")
                            values.append(args[key])
                    query_string = " AND ".join(query_parts)
                    sql_query = "SELECT * FROM Customers"
                    if query_parts:
                        sql_query += f" WHERE {query_string}"
                    all_customers_result = cursor.execute(sql_query, values)
                    customers = [dict(id=row[0], name=row[1], phone_number=row[2], email=row[3], address=row[4], age=row[5]) for row in all_customers_result.fetchall()]
                    return jsonify(customers)
        elif request.method == 'POST':
            data = request.json
            try:
                cursor.execute('INSERT INTO "Customers" (id, name, phone_number, email, address, age) VALUES (?, ?, ?, ?, ?, ?)',
                               (data['id'], data['name'], data['phone_number'], data['email'], data['address'], data['age']))
                return jsonify({"success": True, "message": "Customer added successfully"}), 201
            except Exception as e:
                print(f"Failed to insert customer {data['name']} with id {data['id']}: {e}")
                return jsonify({"success": False, "message": "Failed to insert customer"}), 400




##Customer_Service
@contextlib.contextmanager
def _get_cursor():
    conn = sqlite3.connect('Manual Database.db') 
    yield conn.cursor()
    conn.commit()
    conn.close()


@app.route("/customerService", methods=['GET', 'POST'])
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
        else:
            ticket_id = request.form.get('ticket_id')
            sale_id = request.form.get('sale_id')
            details = request.form.get('details')
            resolved_by = request.form.get('resolved_by')
            worker_id = request.form.get('worker_id')
            timestamp = request.form.get('timestamp')
            status = request.form.get('status')
            try:
                cursor.execute('INSERT INTO "CustomerService" (ticket_id, sale_id, details, resolved_by, worker_id, timestamp, status) VALUES (?, ?, ?, ?, ?, ?, ?)', (ticket_id, sale_id, details, resolved_by, worker_id, timestamp, status))
                return "INSERTED"
            except Exception as e:
                print(f"Failed to open new ticket for sale number {sale_id}")
                return "Failed to insert", 400


@app.route("/customerService/<ticket_id>", methods=['GET', 'POST'])
def get_customer_tickets(ticket_id: str):
    with _get_cursor() as cursor:
        if request.method == 'GET':
            ticket_result = cursor.execute('SELECT * FROM CustomerService WHERE ticket_id=?', (ticket_id,)).fetchone()
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
            details = request.form.get('details')
            resolved_by = request.form.get('resolved_by')
            worker_id = request.form.get('worker_id')
            status = request.form.get('status')
            try:
                cursor.execute("""UPDATE CustomerService SET
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
    return render_template('add_ticket.html')

@app.route('/customer-search')
def customer_search():
    return render_template('customer_search.html')




@app.route('/api/items')
def get_items():
    # Example: Fetching items from a database
    items = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]  # This should be replaced with your database query
    return jsonify(items)


@app.route('/api/submit-ticket', methods=['POST'])
def submit_ticket():
    data = request.json
    selected_item_id = data['itemId']
    comment = data['comment']
    # Here, you would insert the data into your database
    print(f"Item ID: {selected_item_id}, Comment: {comment}")  # Placeholder for actual database insertion
    return jsonify({"success": True, "message": "Ticket submitted successfully"})





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
#http://127.0.0.1:5002/customers




from flask import Flask, jsonify

app = Flask(__name__)

# Example data - replace with actual database queries
users = {"123": {"first_name": "John", "last_name": "Doe", "address": "123 Elm Street"}}
orders = {"456": {"order_number": "456", "items": ["Item A", "Item B"]}}
problem_types = ["Delivery Issue", "Product Issue", "Payment Issue"]

@app.route('/api/users/<user_id>')
def get_user(user_id):
    # Replace with actual data retrieval logic
    user = users.get(user_id, {})
    return jsonify(user)

@app.route('/api/orders/<order_id>')
def get_order(order_id):
    # Replace with actual data retrieval logic
    order = orders.get(order_id, {})
    return jsonify(order)

@app.route('/api/problem-types')
def get_problem_types():
    return jsonify(problem_types)



