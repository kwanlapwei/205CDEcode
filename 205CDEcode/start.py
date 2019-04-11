from flask import Flask, render_template, request, flash, url_for, session, redirect
import pymysql
from productinfo import productinfo

#open database connection
db=pymysql.connect("127.0.0.1", "root", "Kwan0813", "base")
app = Flask(__name__)
app.secret_key = 'development key'

@app.route("/login", methods = ['POST', 'GET'])
def login():
	error = None
	if request.method == 'POST':
		usrname = request.form["usrname"]
		pwd = request.form['pwd']
		cursor = db.cursor()
		cursor.execute("SELECT usrname, pwd FROM signup WHERE usrname = '"+usrname+"' AND pwd = '"+pwd+"'")
		db.commit()
		results = cursor.fetchall()
		if results == ():
			flash('Invalid Username or password') 
			return render_template('Login.html')
		else:
			for row in results:
				user = row[0]
				session['usrname'] = user
			return redirect(url_for('customer', guest=user))
		db.close()
	else:
		return render_template('Login.html')


@app.route("/customer/<guest>", methods=['POST', 'GET'])
def customer(guest):
		flash('Welcome, %s!'% guest )
		return render_template('Home.html', guest=guest)

@app.route("/index")
@app.route("/")
def index():
	if 'usrname' in session:
		return 'Logged in as '+ session['usrname']+'<br>'+"<a href = '/logout'>Click here to log out</a>"
	else:
		return "Hello 205CDE Class! You are not logged in <br><a href= '/login'>Click here to log in</a>"

@app.route("/logout")
def logout():
	session.pop('usrname', None)
	flash('You have logged out!')
	return render_template('Home.html')

@app.route("/register", methods=['POST','GET'])
def register():
	error=None 
	if request.method == 'POST':
		Rname = request.form["Rname"]
		Rhome = request.form['Rhome']
		Remail = request.form["Remail"]
		Rpwd = request.form["Rpwd"] 
		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		# Execute the SQL command
		cursor.execute("SELECT * FROM signup WHERE usrname = '"+Rname+"' OR email = '"+Remail+"'")
		# Commit your changes in the database
		results = cursor.fetchall()
		db.commit()
		if results == ():
			cursor.execute("INSERT INTO signup VALUES (%s, %s, %s, %s)",(Rname, Rhome, Remail, Rpwd))
			db.commit()
			flash('Registration success! ')
			return render_template('Login.html')
		else:
			flash('Registed Username or Email ')
			return render_template('Login.html')
		
		
		db.close()
	else:
		return render_template('Login.html')




	
@app.route("/add", methods=['POST', 'GET'])
def add():
	cursor = db.cursor()
	cursor.execute("SELECT * FROM `product`")
	results = cursor.fetchall()
	for row in results: 
		id1 = row[0]
		name = row[1]
		price = row[2]
	if request.method == 'POST':
		pname = request.form["Pname"]
		pprice = request.form["Pprice"]
		cursor = db.cursor()
		# prepare a cursor object using cursor() method
		cursor.execute("INSERT INTO cart SELECT id, name, price FROM product WHERE name = '"+pname+"'")
		db.commit()
		return render_template('product.html', prod=results)
	else:
		return render_template('product.html', prod=results)

@app.route('/home')
def home():
	return render_template("Home.html")
	
@app.route("/product")
def product():
	prod=productinfo()
	return render_template("product.html", prod=prod.results)

@app.route("/cart", methods=['POST','GET']) 
def cart():
	cursor = db.cursor()
	cursor.execute("SELECT * FROM `cart`")
	results = cursor.fetchall()
	for row in results:
		id1 = row[0]
		name = row[1]
		price = row[2] 
	if request.method =='POST':
		cname = request.form["Cname"]
		cursor = db.cursor()
		cursor.execute("DELETE FROM cart WHERE name = '"+cname+"' ")			
		db.commit()
		flash('Product is removed from Shopping Cart')
		return render_template('cart.html', prod=results)
	else:
		return render_template('cart.html', prod=results)

@app.route('/str', methods = ['POST', 'GET'])
def str():	
	if request.method =='POST':
		customer = request.form["customer"]
		string = request.form["string"]
		date = request.form['date']
		time = request.form['time']
		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		#maxid = cursor.fetchone()
		# Execute the SQL command
		cursor.execute("INSERT INTO string (customer, string, date1, time1) VALUES (%s, %s, %s, %s)", 
			(customer, string, date, time))
		# Commit your changes in the database
		db.commit()
		##custPwd = passwordreturn render_template("login.html", error = error)
		db.close()
		flash('Booking has received. Please remeber and arrive.') 
		return render_template('Home.html')
	else:
		return render_template('String.html')

@app.route('/order', methods=['POST', 'GET'])
def order():
	if request.method == 'POST':
		cursor = db.cursor()
		cursor.execute("SELECT * FROM `cart`")
		results = cursor.fetchall()
		if results == ():
			flash('No Product in Shopping cart')
			return render_template('cart.html')
		else:
			return render_template('info.html')
	else:
		flash('Please Login first')
		return render_template('Home.html')
		

@app.route('/info', methods=['POST', 'GET'])
def info():
	cursor = db.cursor()
	cursor.execute("SELECT * FROM `cart`")
	results = cursor.fetchall()
	for row in results:
		id1=row[0]
		name=row[1]
		price=row[2]
	if request.method == 'POST':
		iname = request.form["Iname"]
		icard = request.form["Icard"]
		ikey = request.form['Ikey']
		cursor = db.cursor()
		cursor.execute("INSERT INTO order_queue (username, credit, pin) VALUES (%s, %s, %s)", (iname, icard, ikey))
		db.commit()
		cursor.execute("SELECT * FROM `order_queue`")
		column = cursor.fetchall()
		for i in column:
			Lorder=column[-1]
			orderid=Lorder[1] 
		cursor.execute("INSERT INTO ordered (product_id, product, price, order_id) VALUES (%s, %s, %s, %s)",
			(id1, name, price, orderid))
		 
		db.commit()
		##custPwd = passwordreturn render_template("login.html", error = error)
		db.close()
		flash('Payment is done, product will arrive after 3-5 working days ')
		return render_template('Home.html')
	else:
		flash('Please Login first')
		return render_template('Home.html')

 


if __name__ == '__main__':
	app.run(debug = True)
							