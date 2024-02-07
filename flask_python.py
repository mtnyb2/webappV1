from flask import Flask, redirect, url_for, render_template

app = Flask(__name__) #__name__ השם של קובץ ההרצה


@app.route('/') #זה המסלול לדף הבית שאני רוצה לפתוח באינטרנט
def first():
    return 'Hello, yeso meeeee'


@app.route('/home') #זה המסלול לדף הבית שאני רוצה לפתוח באינטרנט
def home():
    return render_template('index.html') ##פקודה שאומרת לפתוח את הדף אינדקס

@app.route('/sign-in')
def sign_in():
    return render_template('sign-in.html')

@app.route('/manager-view') 
def manager_view():
    return render_template('manager-view.html')

@app.route('/customer-service-view')
def customer_service_view():
    return render_template('customer-service-view.html')

@app.route('/worker_ticket')
def worker_tickets():
    return render_template('my-ticket.html')

@app.route('/new-ticket')
def new_ticker():
    return 'Open new ticket here'


if __name__ == '__main__':
    app.run(debug=True, port=5002)

#http://127.0.0.1:5000/
#http://127.0.0.1:5002/
#http://127.0.0.1:5002/home
#http://127.0.0.1:5002/sign-in
#http://127.0.0.1:5002/manager-view
#http://127.0.0.1:5002/customer-service-view
#http://127.0.0.1:5002/worker_ticket
#http://127.0.0.1:5002/new-ticket