from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

# custom imports
from userverify import verify
import GetData

# set the required parameters for rest app
app = Flask(__name__)
app.secret_key = "1!qQ2@wW"
api = Api(app)

# authentication using JWT
jwt = JWT(app, verify)


# Books class as a resource to be used for rest operations
class Book(Resource):
	# @jwt_required()
	def get(self):
		request_data = request.get_json()
		if ("rows" in request_data.keys()) and (type(request_data["rows"])==int):
			books = GetData.getRows("books-2.csv",request_data["rows"])
			return {"books":books}
		else:
			data = GetData.getFilteredData('././books-2.csv',request_data)
			if type(data)==str:
				return {"message":data}, 404
			else:
				return {"books":data}, 200

if __name__=="__main__":
	# add the resource to the api and run the app
	api.add_resource(Book, "/books")
	app.run(host="0.0.0.0",port=5000, debug=True)
