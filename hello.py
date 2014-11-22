'''
Created on Nov 21, 2014

@author: ishaansutaria
'''
import model
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/feeds")
def getFeeds():
    return model.getUserUpdates('theJoker')
        

if __name__ == "__main__":
    app.run()