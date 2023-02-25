from flask import Flask, render_template, request, redirect
import sqlite3
import datetime
app = Flask(__name__)
conn = sqlite3.connect('database.db', check_same_thread=False)
 
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
 
diary = """CREATE TABLE IF NOT EXISTS DIARY (
        Notes CHAR(255),
        Date_time TEXT NOT NULL
        )"""
crsr.execute(diary)        
crsr.execute(db)
# # print(N)
# output = crsr.execute("SELECT Email FROM DATA")
# for row in output:
#         print(row)


@app.route("/")
def homepage():

    return render_template("index.html")    

@app.route("/login")
def login():

    return render_template("login.html")    

@app.route("/signup")
def signup():

    return render_template("signup.html")    

@app.route("/diary")
def diary():
    old_notes = crsr.execute("SELECT * FROM DIARY WHERE ")# buggy code the data imported should be of the logged in user 
    
    return render_template("diary.html", old_notes=old_notes)    

@app.route("/note_added", methods=["POST"])
def notes_added():
    notes = request.form.get("diary")
    current_date_time = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    crsr.execute("INSERT INTO DIARY (Notes, Date_time) VALUES  (?, ?)", (notes, current_date_time))
    
    return redirect("\diary")


@app.route("/success", methods = ["POST"])
def success_register():
    Password = request.form.get("password")
    Name = request.form.get("name")
    Email = request.form.get("email")
    try:
        crsr.execute("INSERT INTO DATA (Email, Name, Password) VALUES (?, ?, ?)", (Email, Name, Password))
    except:
        return render_template("failure.html") 
    else:
        output = crsr.execute("SELECT * FROM DATA")
        for row in output:
            print(row)
    
        return render_template("success.html")    

        
@app.route("/login_success", methods = ["POST"])
def successful_login():
    Password = request.form.get("password")
    # Password = list(Password)
    Email = request.form.get("email")
    # Password = [tuple(Password)
    crsr.execute("SELECT   Password FROM DATA  WHERE  Email = ? ", (Email,))
    order = crsr.fetchall()
    try:
        for row in order:
            for column in row:
                password = column
        if (password == Password):
            return render_template("success_login.html")
        else:
            return redirect("/login")
    except:
        return redirect("/signup")
    # else:
        
@app.route("/logout")
def logout():
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)