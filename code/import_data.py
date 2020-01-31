
from datetime import datetime

# Load the Pandas libraries with alias 'pd' 
import pandas as pd 

'''
	Function to read CSV file and return pandas dataframe
'''
def import_data(path="../incident_event_log.csv"):
	# Read data from file
	data = pd.read_csv(path) 
	
	# Preview the first 5 lines of the loaded data 
	print("Data imported with pandas:")
	print(data.head())
	
	return data

'''
	Function to filter and tranform current data to make it more interesting in ou case
'''

def transform_data(df):
	return df


'''
	This section is about testing all current functions
'''

data = import_data()

# example of dates transformations into datetime
data_transformed = pd.DataFrame({
	"opened_at_datetime": [datetime.strptime(x, "%d/%m/%Y %H:%M") for x in data["opened_at"]],
	"opened_at": data["opened_at"]
})

print(data_transformed.head(100))

# Now transforming all dates








