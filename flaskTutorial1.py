
from flask import Flask,redirect,url_for, render_template,request,session,flash
from datetime import timedelta
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key="123"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'u?%9b9+D6DCG-WN'
app.config['MYSQL_DB'] = 'team_data'
 
app.permanent_session_lifetime=timedelta(minutes=10)

db=MySQL(app)

@app.route("/test")
def test_connection():
    try:
        cursor = db.connection.cursor()
        cursor.execute('SELECT 1')
        cursor.close()
        return 'Connection to MySQL database is successful'
    except Exception as e:
        return "failed"


@app.route("/",methods=["POST","GET"])
def home():
    if "user" in session:
        return redirect(url_for("user"))
    else:
        return redirect(url_for("login"))
    
    
@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent=True
        user = request.form["nm"]
        password = request.form["pw"]
        if user == "admin" and password == "admin":
            session["user"]=user
            return redirect(url_for("user"))
        else:
            flash("Wrong info! >:(")
            return redirect(url_for("login"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user",methods=["POST","GET"])
def user():
    if "user" in session:
        cursor = db.connection.cursor()
        if request.method == "POST":
            if request.form["submit"] == "View Data":
                cursor.execute("SELECT * FROM team_data.users")
                users = cursor.fetchall()
                return render_template("viewDatabase.html",all_users=users)
            elif request.form["submit"] == "Add team member":
                id= request.form["id"]
                name= request.form["name"]
                age= request.form["age"]
                cgpa= request.form["cgpa"]
                cursor.execute("SELECT * FROM users WHERE id = %s",(id,))
                existing_user = cursor.fetchone()
                if existing_user:
                    flash(f"ID {id} is already in database ;)")
                    return render_template("index.html")
                else:
                    cursor.execute("INSERT INTO users (id, name, age, cgpa) VALUES (%s, %s, %s, %s)", (id, name, age, cgpa))
                    db.connection.commit()
                flash("Team member added :D")
                return render_template("index.html")
            elif request.form["submit"] == "Delete team member":
                id= request.form["id"]
                cursor.execute("SELECT * FROM users WHERE id = %s",(id,))
                existing_user = cursor.fetchone()
                if existing_user:
                    cursor.execute("DELETE FROM users WHERE id = %s",(id,))
                    db.connection.commit()
                    flash("Someone has been deleted TwT")
                    return render_template("index.html")
                else:
                    flash(f"ID {id} doesn't exist :(")
                    return render_template("index.html")
            else:
                return "not entering any if statement for some unknown reason..."
        else:
            return render_template("index.html")
    else:
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    global cursor
    if "user" in session:
        session.pop("user",None)
        flash("You have been logged out XD")

    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

