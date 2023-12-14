import pandas as pd
from flask_ngrok import run_with_ngrok
from flask import request, jsonify, Flask
import  random as rk

app = Flask(__name__)
run_with_ngrok(app)

lista = [{
    "name": "Erickson",
    "city": "(33)998645727",
    "age": 23,
    "country":"india"
    },
    {
    "name": "Mahesh",
    "city": "Bangalore",
    "age": 25,
    "country":"india"
    },
    {"name": "Alex",
    "city": "London",
    "age": 26,
    "country":"UK"
    },
    {"name": "David",
    "city": "San Francisco",
    "age": 27,
    "country":"USA"
    },
    {"name": "John",
    "city": "Toronto",
    "age": 28,
    "country":"Canada"
    },
    {"name": "Chris",
    "city": "Paris",
    "age": 29,
    "country":"France"
    }
]

@app.route("/") #code to assign HomePage URL in our app to function home.

def home():
  '''
  The entire line below must be written in a single line.
  '''
  print("Hello World")
  return "<marquee><h3> TO CHECK IN PUT ADD '/input' TO THE URL AND TO CHECK OUT PUT ADD '/output' TO THE URL.</h3></marquee>"

@app.route("/input") #code to assign Input URL in our app to function input.

def input():
  return jsonify(lista) # "d" is the dictionary we defined

@app.route('/output', methods=['GET','POST']) #output page

def predJson():
 pred = r.choice(["positive","negative"])
 nd = lista # our input
 nd["prediction"]=pred
 return jsonify(nd)

app.run()
