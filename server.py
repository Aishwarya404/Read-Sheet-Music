# Contributors : Aishwarya Sivakumar, Roshan Babu, Nidhi Sunil Kumar, Yina Jian
# UNI : as6418, rbk2145, ns3566, yj2713

from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import json
app = Flask(__name__, static_url_path='/static')

# ROUTES

@app.route('/')
def welcome():
   return render_template('welcome.html')

@app.route('/quiz')
def quiz():
   return render_template('quiz.html')

@app.route('/learn')
def learn():
   return render_template('learn.html')

if __name__ == '__main__':
   app.run(debug = True)




