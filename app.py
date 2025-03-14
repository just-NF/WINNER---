from flask import Flask, render_template, request 
import mysql.connector

app = Flask(__name__)


@app.route("/details", methods = ["POST", "GET"])
def details ():
    user_name = request.form['user_name']
    phone_number = request.form['phone_number']
    number_of_items = request.form['number_of_items']
    total_amount = request.form['total_amount']
    order_date = request.form['order_date']
    # connect to the data base
       
    mydb = mysql.connector.connect(
    host="sql8.freesqldatabase.com",
    user = "sql8767356",
    password = "BhBIbEl4hN",   
    database = "sql8767356"
)
    
    mycursor = mydb.cursor()
    mycursor.execute('INSERT INTO CustomerDetails (user_name, phone_number, number_of_items, total_amount, order_date) VALUES (%s, %s, %s, %s, %s )', (user_name, phone_number, number_of_items, total_amount, order_date))
    mydb.commit()
    return render_template('index.html')


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/winner!")
def winner():
    mydb = mysql.connector.connect(
    host="sql8.freesqldatabase.com",
    user = "sql8767356",
    password = "BhBIbEl4hN",   
    database = "sql8767356"
    )
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM CustomerDetails ORDER BY total_amount DESC')
    account = mycursor.fetchone()
    if account:
        user_name = account[1]
        phone_number = account[2]
        return render_template("winner.html", user_name = user_name, phone_number = phone_number)  
    else:
        return render_template("winner.html")



app.run(host="0.0.0.0", port=80, debug=True)