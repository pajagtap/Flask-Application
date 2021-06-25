from flask import Flask, request
from flask_restful import Resource, Api

# custom modules
import GetData

# set the required parameters for rest app
app = Flask(__name__)

# Books class as a resource to be used for rest operations
class Book(Resource):
	def get(self):
		request_data = request.get_json()
		if ("rows" in request_data.keys()) and (type(request_data["rows"])==int):
			books = GetData.getRows("/books-2.csv",request_data["rows"])
			return {"books":books}
		else:
			data = GetData.getFilteredData('././books-2.csv',request_data)
			if type(data)==str:
				return {"message":data},404	# 404-Not Found response when books are not found
			else:
				return {"books":data},200	# 200 Successful response

if __name__=="__main__":
	# add the resource to the api and run the app
	api.add_resource(Book, "/books")
	app.run(host="0.0.0.0",port=5000, debug=True)
