from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users/', methods=['GET', 'POST'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')
      print(not search_job)
      if search_username and not search_job: # get by username only 
         return get_by_username(search_username)
      elif search_username and search_job: # get by username and job 
         return get_by_username_and_job(search_username, search_job)
      return users # return json of users
   elif request.method == 'POST':
      print("Here")
      userToAdd = request.get_json()
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True)
      resp.status_code = 200 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp
         
def get_by_username_and_job(username, job): 
   subdict = {'users_list' : []}
   users = get_by_username(username)['users_list']
   for user in users: 
      if user['job'] == job: 
         subdict['users_list'].append(user)
   return subdict

def get_by_username(username): 
   subdict = {'users_list' : []}
   for user in users['users_list']:
      if user['name'] == username:
         subdict['users_list'].append(user)
   return subdict

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id=None):
   resp = jsonify()
   resp.status_code = 404
   if request.method == 'DELETE' and id:
      for user in users['users_list']: 
         if user['id'] == id: 
            users['users_list'].remove(user)
            resp.status_code = 204 #optionally, you can always set a response code. 
   return resp 