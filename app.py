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
        user = "sql8764909",
        password = "8cEtjHmsu5",
        database = "sql8764909"
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
    return render_template("winner.html")

app.run(host="0.0.0.0", port=80, debug=True)