# from random import randint
# from flask import Flask,render_template,request,url_for,redirect
# from flask_mail import *
# import ibm_db
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)