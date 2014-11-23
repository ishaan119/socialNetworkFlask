'''
Created on Nov 21, 2014

@author: ishaansutaria
'''


from flask import Flask, jsonify,request,Response

import model1


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/apiv1/feeds")
def getFeeds():
    print model1.getFeed()
    
    return jsonify(model1.getFeed())

@app.route('/apiv1/sign_up', methods=['POST'])
def createUser():
    print request.headers
    userData = request.get_json()
    print userData
    resp = jsonify(userData)
    resp.status_code = 201

    return resp

@app.route('/apiv1/sign_in', methods=['POST'])
def signinUser():
    pass

@app.route('/apiv1/create_feed', methods=['POST'])
def createFeed():
    pass

@app.route('/apiv1/create_connection', methods=['POST'])
def createConnection():
    pass

@app.route('/apiv1/login', methods=['POST'])
def loginUser():
    pass

@app.route('/apiv1/logout', methods=['POST'])
def logoutUser():
    pass

@app.route('/apiv1/followers', methods=['GET','POST'])
def followers():
    pass

if __name__ == "__main__":
    print model1.getFeed() 
    app.run()