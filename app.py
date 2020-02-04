# Importing the flask module
from flask import Flask, render_template
import pymysql
# Create a flask object named app
app = Flask(__name__)


class Database:
    def __init__(self):
        self.con = pymysql.connect(host='mrbartucz.com',
                                   user='xg6856vd',
                                   password='*******',
                                   db='xg6856vd_University',
                                   charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def list_students(self):
        self.cur.execute("SELECT * FROM Students")
        result = self.cur.fetchall()
        return result


@app.route('/')
def students():
    def db_query():
        db = Database()
        students = db.list_students()
        return students

    res = db_query()
    print(res)
    return render_template('index.html', result=res, content_type='application/json')


# if code is run from terminal
if __name__ == "__main__":
    # Server will listen to port 80 and will report any errors.
    app.run(host='127.0.0.1', port=6586, debug=True)
