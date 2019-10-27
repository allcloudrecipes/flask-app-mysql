import pymysql
from flask_table import Table, Col, LinkCol
from flask import flash, render_template, request, redirect
from werkzeug import generate_password_hash, check_password_hash
from flask import Flask
from flaskext.mysql import MySQL
app = Flask(__name__)
app.secret_key = "UZc4NNpys83SLHTb"

mysql = MySQL() 

app.config['MYSQL_DATABASE_USER'] = 'sahbi'
app.config['MYSQL_DATABASE_PASSWORD'] = 'UZc4NNpys83SLHTb'
app.config['MYSQL_DATABASE_DB'] = 'mydb'
app.config['MYSQL_DATABASE_HOST'] = 'sahbi-db-server.cxe7apfwy1cy.us-east-2.rds.amazonaws.com:3306'
mysql.init_app(app)

class Results(Table):
    task_id = Col('Id', show=False)
    task_name = Col('Name')
    delete = LinkCol('Delete', 'delete_task', url_kwargs=dict(id='task_id'))




@app.route('/new_task')
def add_task_view():
	return render_template('add.html')
		
@app.route('/task', methods=['POST'])
def add_task():
	try:		
		_name = request.form['inputName']
		if _name and request.method == 'POST':


			sql = "INSERT INTO tbl_task(task_name) VALUES(%s)"
			data = (_name)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			flash('Task added successfully!')
			return redirect('/')
		else:
			return 'Error while adding task'
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/')
def tasks():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM tbl_task")
		rows = cursor.fetchall()
		table = Results(rows)
		table.border = True
		return render_template('tasks.html', table=table)
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()


@app.route('/delete/<int:id>')
def delete_task(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM tbl_task WHERE task_id=%s", (id,))
		conn.commit()
		flash('Task deleted successfully!')
		return redirect('/')
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
	

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)