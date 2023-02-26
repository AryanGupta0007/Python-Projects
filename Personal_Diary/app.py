from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import datetime
app = Flask(__name__)
conn = sqlite3.connect('database.db', check_same_thread=False)
app.secret_key = 'super secret key'
 
# cursor object
crsr = conn.cursor()
 

# crsr.execute("DROP TABLE IF EXISTS DIARY")
# crsr.execute("DROP TABLE IF EXISTS DATA")

# Creating table
db = """ CREATE TABLE IF NOT EXISTS DATA (
            
            Email CHAR(255) PRIMARY KEY,
            Name CHAR(25) NOT NULL,
            Password TEXT NOT NULL
        ); """
# crsr.execute("DROP TABLE DIARY") 
diary = """CREATE TABLE IF NOT EXISTS DIARY (
        Email CHAR(255),
        Notes CHAR(255),
        Date_time TEXT NOT NULL
        )"""
crsr.execute(diary)        
crsr.execute(db)
crsr.execute("SELECT * FROM DATA")
# # print(N)
# output = crsr.execute("SELECT Email FROM DATA")
# for row in output:
#         print(row)


@app.route("/")
def homepage():

    return render_template("index.html")    

@app.route("/login", methods=["GET", "POST"])
def login():
    if (request.method) == "POST":
        Password = request.form.get("password")
        Name = request.form.get("name")
        Email = request.form.get("email")
        crsr.execute("SELECT   Password FROM DATA  WHERE  Email = ? ", (Email,))
        order = crsr.fetchall()
        try:
            for row in order:
                for column in row:
                    password = column
            if (password == Password):
                return redirect(url_for("diary", email= Email))
            else:
                return redirect("/login")
        except:
            return redirect("/signup")
        
    elif (request.method) == "GET":
        
        return render_template("login.html")    

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if (request.method) == "POST":
        Password = request.form.get("password")
        Name = request.form.get("name")
        Email = request.form.get("email")
        try:
            crsr.execute("INSERT INTO DATA (Email, Name, Password) VALUES (?, ?, ?)", (Email, Name, Password))
            conn.commit()
        except:
            return render_template("failure.html") 
        else:
            output = crsr.execute("SELECT * FROM DATA")
            for row in output:
                print(row)
        
            return redirect(url_for("diary", email= Email))
    else:
        return render_template("signup.html")    

@app.route("/diary", methods = ["GET", "POST"])
def diary():
    
    if request.method == "GET":
        email = request.args.get("email")
        session["Email"] = email
        try:
            old_notes = crsr.execute("SELECT Notes, Date_time FROM DIARY WHERE Email = ?", (email,))             
            return render_template("diary.html", old_notes=old_notes)
        except:
                       
            return render_template("diary.html", old_notes="")
            
    elif request.method == "POST":
        email = session.get("Email", None)
        notes = request.form.get("diary")
        current_date_time = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        crsr.execute("INSERT INTO DIARY (Email, Notes, Date_time) VALUES  (?, ?, ?)", (email, notes, current_date_time))
        conn.commit()
        old_notes = crsr.execute("SELECT Notes, Date_time FROM DIARY where email = ?", (email,))   
        return render_template("diary.html", old_notes=old_notes)

        
        
@app.route("/logout")
def logout():
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)