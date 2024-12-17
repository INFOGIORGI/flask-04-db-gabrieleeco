from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"] = "138.41.20.102"
app.config["MYSQL_PORT"] = 53306
app.config["MYSQL_DB"] = "w3schools"
app.config["MYSQL_USER"] = "ospite"
app.config["MYSQL_PASSWORD"] = "ospite"
mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("home.html", titolo="Home Page")

@app.route("/products")
def products():
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM products"
    cursor.execute(query)
    prodotti = cursor.fetchall()
    return render_template("products.html", titolo = "Products", prodotti = prodotti)

app.run()
