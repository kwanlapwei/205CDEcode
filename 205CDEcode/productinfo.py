from flask import Flask, render_template, request, redirect, url_for
import pymysql

db=pymysql.connect("127.0.0.1", "root", "Kwan0813", "base")
app = Flask(__name__, static_folder='static')
app.secret_key = 'development key'

class productinfo():
	cursor = db.cursor()
	cursor.execute("SELECT * FROM `product`")
	results = cursor.fetchall()
	for row in results:
		id1 = row[0]
		name = row[1]
		price = row[2]

	db.commit()
	