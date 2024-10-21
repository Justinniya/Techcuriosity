from flask import Flask, request, redirect, url_for, render_template,flash,session
from flask_mysqldb import MySQL
import random
import sqlite3


class Techcuriosity:
    def __init__(self,main):
        self.app = Flask(main)
        self.app.secret_key = "a"
        self.app.config['MYSQL_HOST'] = "localhost"
        self.app.config['MYSQL_USER'] = "root"
        self.app.config['MYSQL_PASSWORD'] = ""
        self.app.config["MYSQL_DB"] = "Techcuriosity"
        self.mysql = MySQL(self.app)
        self.setup_route()
        self.run()

    

    

    def setup_route(self):
        @self.app.route('/')
        def landing_page():
            return render_template("landingpage.html")

        @self.app.route('/login', methods=["GET","POST"])
        def login():
            if request.method == "POST":
                email = request.form["email"]
                password = request.form["password"]
                self.cursor = self.mysql.connection.cursor()
                self.cursor.execute(f"SELECT tech_id FROM users WHERE email = %s AND password= %s", (email,password,))
                self.loggedin = self.cursor.fetchone()
                if self.loggedin:
                    session['tech_id'] = self.loggedin[0]
                    return redirect(url_for('home'))
                else:
                    return render_template("login.html",error=True)
            else:
                return render_template("login.html",error=False)

        @self.app.route('/signup', methods=["GET","POST"])
        def signup():
            if request.method == "POST":
                name = request.form["name"]
                email = request.form["email"]
                password = request.form["password"]
                repeat = request.form["repeat"]
                self.cursor = self.mysql.connection.cursor()
                tech_id = random.randint(100000000000,999999999999)
                self.cursor.execute(f"INSERT INTO users (tech_id,email,name,password,money) VALUES(%s,%s,%s,%s,0)",(str(tech_id),email,name,password,))
                self.cursor.execute(f"INSERT INTO courses (tech_id) VALUES(%s)",(str(tech_id),))
                self.mysql.connection.commit()
                return redirect(url_for("landing_page"))
            else:
                return render_template("signup.html")


        @self.app.route('/home')
        def home():
            if 'tech_id' in session:
                self.cursor = self.mysql.connection.cursor()
                self.cursor.execute(f"SELECT * FROM courses WHERE tech_id={session['tech_id']}")
                self.loggedin = self.cursor.fetchone()
                print(self.loggedin)
                return render_template("home.html",paid=self.loggedin)
            else:
                return redirect('/')

        @self.app.route('/forgotpassword/<string:email>',methods=["GET","POST"])
        def forgotpassword(email):
            print(email)
            if 'email1' in session:
                if request.method == "POST":
                    newpass = request.form["newpass"]
                    newconpass = request.form["newconpass"]
                    print(newconpass)
                    if newpass == newconpass:
                        self.cursor = self.mysql.connection.cursor()
                        self.cursor.execute(f"UPDATE users SET password = %s WHERE email = %s",(newconpass,email))
                        self.mysql.connection.commit()
                        return render_template("resetpassword.html",success = True)
                    else:
                        return render_template('resetpassword.html',email=email,error=True)
                else:
                    return render_template('resetpassword.html',email=email)
            else:
                return redirect('/forgot')

        @self.app.route('/whatweoffer')
        def whatweoffer():
            return render_template("whatweoffer.html")

        @self.app.route('/aboutus')
        def aboutus():
            return render_template('about.html')

        @self.app.route('/forgot',methods=["GET","POST"])
        def forgot():
            if request.method == "POST":
                email = request.form["email"]
                self.cursor = self.mysql.connection.cursor()
                self.cursor.execute(f"SELECT email FROM users WHERE email = %s",(email,))
                self.result = self.cursor.fetchone()
                email1 = self.result[0]
                print("a")
                if self.result:
                    print("b")
                    session['email1'] = email1
                    return redirect(f"/forgotpassword/{email1}")
                    
                else:
                    print("c")
                    return render_template('forgotpassword.html',error = True)
            else:
                return render_template('forgotpassword.html')

        # @self.app.route('/courses/<string:coursename>',methods=["GET"])
        # def courses(coursename):
        #     if coursename == "introduction to computing":
        #         return redirect("/course/introduction")
        #     elif coursename == "html":
        #         return redirect("/course/compiler")
        #     elif coursename == "python programming":
        #         return redirect('/course/pythoneditor')

        @self.app.route('/payment/<string:name>',methods=['POST','GET'])
        def payment(name):
            abillpython = 2500
            abillcomfun = 1800
            abilldatabase = 2000
            abillnetworking = 1200
            abillcomgraph = 1500
            abillcloud = 1900
            tech_id = session["tech_id"]
            print(tech_id,name)
            if request.method == "POST":
                
                if name == "billpython":
                    self.cursor = self.mysql.connection.cursor()
                    self.cursor.execute(f"UPDATE courses SET python_subs = 'TRUE' WHERE tech_id = {tech_id};")
                    self.mysql.connection.commit()
                    return redirect(f"/home")
                elif name == "billcomfund":
                    self.cursor = self.mysql.connection.cursor()
                    self.cursor.execute(f"UPDATE courses SET computing_fund = 'TRUE' WHERE tech_id = {tech_id};")
                    self.mysql.connection.commit()
                    return redirect(f"/home")
                elif name =="billdatabase":
                    self.cursor = self.mysql.connection.cursor()
                    self.cursor.execute(f"UPDATE courses SET database_subs = 'TRUE' WHERE tech_id = {tech_id};")
                    self.mysql.connection.commit()
                    return redirect(f"/home")
                elif name =="billnetworking":
                    self.cursor = self.mysql.connection.cursor()
                    self.cursor.execute(f"UPDATE courses SET networking_subs = 'TRUE' WHERE tech_id = {tech_id};")
                    self.mysql.connection.commit()
                    return redirect(f"/home")
                elif name =="billcomgraph":
                    self.cursor = self.mysql.connection.cursor()
                    self.cursor.execute(f"UPDATE courses SET computer_graphics = 'TRUE' WHERE tech_id = {tech_id};")
                    self.mysql.connection.commit()
                    return redirect(f"/home")
                elif name =="abillcloud":
                    self.cursor = self.mysql.connection.cursor()
                    self.cursor.execute(f"UPDATE courses SET cloud_computing = 'TRUE' WHERE tech_id = {tech_id};")
                    self.mysql.connection.commit()
                    return redirect(f"/home")
                elif name =="freeintro":
                    self.cursor = self.mysql.connection.cursor()
                    self.cursor.execute(f"UPDATE courses SET introduction_to_it = 'TRUE' WHERE tech_id = {tech_id};")
                    self.mysql.connection.commit()
                    return redirect(f"/home")
                elif name =="freeweb":
                    self.cursor = self.mysql.connection.cursor()
                    self.cursor.execute(f"UPDATE courses SET html = 'TRUE' WHERE tech_id = %s;",(tech_id,))
                    self.mysql.connection.commit()
                    return redirect(f"/home")
            return render_template('payment.html',course = name)

        @self.app.route('/modals')
        def modals():
            return render_template('modal.html')

        @self.app.route('/course/html')
        def htmlcompiler():
            return render_template('compilereditor.html')

        @self.app.route('/course/compiler')
        def compiler():
            return render_template('compilereditor.html')
        import sys
        def maincode(code):
            filename = 'file.txt'
            try:
                original_stdout = sys.stdout
                sys.stdout = open(filename, 'w', encoding='utf-8', errors='ignore')
                
                exec(code)
                sys.stdout.close()
                sys.stdout = original_stdout
                with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
                    output = f.read()

            except Exception as e:
                sys.stdout = original_stdout
                output = str(e)

            return output

        @self.app.route("/course/pythonfirst")
        def pythonfirst():
            return render_template("pythonfiirst.html")

        @self.app.route('/course/pythoneditor', methods=['POST',"GET"])
        def pythoneditor():
            if request.method == "POST":
                code = request.form["code"]
                result = maincode(f"""{code}""")
                print(result)
                print(code)
                return render_template("pythoneditor.html",result=result,code=code)
            else:
                return render_template("pythoneditor.html")


        @self.app.route("/course/datafirst")
        def datafirst():
            return render_template("database.html")

        def get_db_connection():
            conn = sqlite3.connect('database.db')
            conn.row_factory = sqlite3.Row
            return conn

        @self.app.route('/course/sql', methods=['POST',"GET"])
        def sql():
            if request.method == "POST":
                sql_query  = request.form["code"]
                try:
                    conn = get_db_connection()
                    cursor = conn.cursor()
                    cursor.execute(f"{sql_query}")
                    
                    if sql_query.strip().lower().startswith('select'):
                        results = cursor.fetchall()
                        
                        return render_template('sql.html', results=results,sql_query=sql_query)
                    else:
                        conn.commit()
                        return render_template('sql.html', message='Query executed successfully!')
                    
                except sqlite3.Error as e:
                    return render_template('sql.html', error=str(e))
                finally:
                    conn.close()
            else:
                return render_template('sql.html')

        @self.app.route("/course/networkingfirst")
        def networkingfirst():
            return render_template("networking.html")

        @self.app.route("/course/cloudfirst")
        def cloudfirst():
            return render_template("cloudcomputing.html")

        @self.app.route("/course/comgraphfirst")
        def comgraphfirst():
            return render_template("computergraphics.html")

        @self.app.route("/course/webfirst")
        def webfirst():
            return render_template("htmlfirst.html")
        
        @self.app.route("/course/comfundfirst")
        def compundfirst():
            return render_template("computing.html")

        @self.app.route("/course/compufirst")
        def cumpufiirst():
            return render_template("introduction.html")

        @self.app.route('/users/logout')
        def logout():
            session.pop("tech_id")
            return redirect("/")


    def run(self):
        self.app.run(debug=True)

app = Techcuriosity(__name__)