'''
Created on Nov 21, 2014

@author: ishaansutaria
'''


from flask import Flask, jsonify,request,Response
import json
import model1


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/apiv1/sign_up', methods=['POST'])
def createUser():
    print request.headers
    userData = request.get_json()
    resp = jsonify(model1.createUser(userData))
    resp.status_code = 201

    return resp

@app.route('/apiv1/sign_in', methods=['POST'])
def signinUser():
    loginData = request.get_json()
    
    #model1.loginUser(**loginData)
    resp = jsonify(model1.loginUser(**loginData))
    resp.status_code = 201

    return resp


@app.route('/apiv1/sign_out', methods=['POST'])
def signOut():
    logoutData = request.get_json()
    print logoutData 
    resp = jsonify(model1.logoutUser(**logoutData))
    resp.status_code = 201
    return resp

@app.route('/apiv1/create_connection', methods=['POST'])
def createConnection():
    usernames = request.get_json()
    print usernames
    result = model1.createConnection(**usernames)
    print result
    if result == 1:
        resp = Response(status=201)
        return resp
    else:
        return not_found()

@app.route('/apiv1/friend_list', methods=['GET'])
def getFreindList():
    username = request.args['username']  
    result =  model1.getFreindList(username)
    print json.dumps(result)
    return Response(json.dumps(result),  mimetype='application/json')

@app.route("/apiv1/feeds",methods=['GET','POST'])
def getFeeds():
    if request.method == 'GET':
        print model1.getFeed()
        return jsonify(model1.getFeed())
    if request.method == 'POST':
        pass



@app.route('/apiv1/followers', methods=['GET','POST'])
def followers():
    pass


@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == "__main__":
    app.run()