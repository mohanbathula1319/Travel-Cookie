from flask import Flask, session
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from flask import flash
import sqlite3
app = Flask(__name__)
app.secret_key = 'my_secret_key'


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/BANGKOK")
def BANGKOK():
    return render_template("BANGKOK.html")

@app.route("/grandpalace")
def grandpalace():
    return render_template("grandpalace.html")

@app.route("/watpho")
def watpho():
    return render_template("watpho.html")

@app.route("/chayuchak")
def chayuchak():
    return render_template("chayuchak.html")

@app.route("/Rome")
def Rome():
    return render_template("Rome.html")

@app.route("/colosseum")
def colosseum():
    return render_template("colosseum.html")

@app.route("/THE PANTHEON")
def PANTHEON():
    return render_template("THE PANTHEON.html")

@app.route("/TREVI FOUNTAIN")
def TREVIFOUNTAIN():
    return render_template("TREVI FOUNTAIN.html")

@app.route("/Venice")
def Venice():
    return render_template("Venice.html")

@app.route("/RIALTO")
def RIALTO():
    return render_template("RIALTO BRIDGE.html")

@app.route("/DOGE")
def DOGE():
    return render_template("DOGE'S PALACE.html")

@app.route("/BASILICA")
def BASILICA():
    return render_template("BASILICA.html")

@app.route("/Italy")
def Italy():
    return render_template("Italy.html")

@app.route("/Milan")
def Milan():
    return render_template("Milan.html")

@app.route("/switzerland")
def switzerland():
    return render_template("switzerland.html")

@app.route("/Geneva")
def Geneva():
    return render_template("Geneva.html")

@app.route("/old_town")
def old_town():
    return render_template("old_town.html")

@app.route("/jetedau")
def jetedau():
    return render_template("jetedau.html")

@app.route("/CHOCOLATERIE")
def CHOCOLATERIE():
    return render_template("CHOCOLATERIE STETTLER.html")

@app.route("/intrerlaken")
def intrerlaken():
    return render_template("intrerlaken.html")

@app.route("/Thailand")
def Thailand():
    return render_template("Thailand.html")

@app.route("/PHUKET")
def PHUKET():
    return render_template("PHUKET.html")

@app.route("/CHAING_MAI")
def CHAING_MAI():
    return render_template("CHAING_MAI.html")


@app.route("/zurich")
def zurich():
    return render_template("zurich.html")

@app.route("/Grossmunster")
def Grossmunster():
    return render_template("Grossmunster.html")

@app.route("/lake_zurich")
def lake_zurich():
    return render_template("lake_zurich.html")

@app.route("/BAHNHOFSTRASSE")
def BAHNHOFSTRASSE():
    return render_template("BAHNHOFSTRASSE.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/traveltips")
def traveltips():
    return render_template("traveltips.html")

conn = sqlite3.connect('database.db')
conn = sqlite3.connect('database.db')
"""conn.execute('DROP TABLE IF EXISTS user_details')
conn.commit()
conn.execute('''CREATE TABLE user_details 
             (Name TEXT,
             Email TEXT PRIMARY KEY,
             Password TEXT
             );''')
print("Table created successfully")
c = conn.cursor()
c.execute('DELETE FROM user_details')
conn.commit()
conn.close()"""

@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        try:
            Name = request.form['signup-name']
            Email = request.form['signup-email']
            Password = request.form['signup-password']

            # Connect to SQLite3 database and execute the INSERT
            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute('INSERT INTO user_details (Name, Email, Password) VALUES (?, ?, ?)',
                 (Name, Email, Password))

                con.commit()
                msg = "Account Created"
        except:
            con.rollback()
            msg = "Account Creation error"

        finally:
            con.close()
            # Send the transaction message to result.html
            return render_template('login.html',msg=msg)


        
@app.route('/userlogin', methods=['POST'])
def userlogin():
        Email = request.form['login-email']
        Password = request.form['login-password']
    
    
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM user_details WHERE Email=? AND Password=?", (Email, Password))
        user = cur.fetchone()
        conn.close()
        if user:
            session['Email'] = Email
            session['user'] = user
            msg = user[0]
            return render_template('index.html', msg=msg)
        else:
            msg = 'Invalid email or password. Please try again.'
        return render_template('login.html', msg=msg)

@app.route('/logout')
def logout():
    session.pop('Email', None)
    return redirect(url_for('index'))

