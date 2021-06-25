import pandas as pd

# Method to get number of rows from the dataframe
def getRows(file_path,rows):
	data = pd.read_csv(file_path)
	if rows > data.shape[0]:
		rows = data.shape[0]
	# return data.head(rows).to_json(orient='records')
	return data.head(rows).to_dict(orient='records')

# Method to get filtered rows from the dataframe
def getFilteredData(file_path,json_in):
	data = pd.read_csv(file_path)

	for item in json_in.items():
		if item[0] in data.columns:
			# print('Column is available.')
			if data.isin([item[1]]).any().any():
				# print("Yes the book is available.")
				return data[data[item[0]]==item[1]].to_dict(orient="records")
			else:
				return "No books are available"	
		
	return "Please change the filtering criteria."	

	

# print(getRows('././books-2.csv',3))
# json_in = {"authors":"Jesse Grant"}						# everything is available
# json_in = {"title" : "Not available title"}				# column is available but not the value
# json_in = {"NA Column":"Friction, Volume 7: Best Gay Erotic Fiction"}			# column itself is not available
# print(getFilteredData('././books-2.csv',json_in))
