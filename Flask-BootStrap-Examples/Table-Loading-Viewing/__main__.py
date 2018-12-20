from flask import Flask, render_template, request, redirect, url_for
import sqlite3


db = sqlite3.connect(':memory:')

cursor = db.cursor()
cursor.execute('''
    CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
                       phone TEXT, email TEXT unique, password TEXT)
''')
db.commit()

cursor = db.cursor()
name1 = 'Andres'
phone1 = '3366858'
email1 = 'user@example.com'
# A very secure password
password1 = '12345'

name2 = 'John'
phone2 = '5557241'
email2 = 'johndoe@example.com'
password2 = 'abcdef'

# Insert user 1
cursor.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES(?,?,?,?)''', (name1,phone1, email1, password1))

# Insert user 2
cursor.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES(?,?,?,?)''', (name2,phone2, email2, password2))

db.commit()





app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET","POST"])
def template_test():
    result_list = cursor.execute('''SELECT name, email, phone FROM users''').fetchall()
    column_names = [d[0] for d in cursor.description]
    return render_template('template.html', my_string="yooo!", my_list=list(result_list), column_names=column_names)


@app.route('/addrec', methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
            name = request.form['name']
            phone = request.form['phone']
            email = request.form['email']
            password = request.form['password']

            cursor.execute('''INSERT INTO users(name, phone, email, password)
                VALUES(?,?,?,?)''', (name, phone, email, password))

            db.commit()

            result_lst = cursor.execute('''SELECT name, email, phone FROM users''').fetchall()
            column_nams = [d[0] for d in cursor.description]
            return render_template('template.html', my_string="weeeeeeeee!", my_list=list(result_lst), column_names=column_nams)


if __name__ == '__main__':
    app.run(debug=True)
