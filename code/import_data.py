
from datetime import datetime
import json

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
	print("Columns and Count:")
	print(data.count())
	
	return data

'''
	Function to filter and tranform current data to make it more interesting in ou case
'''

def transform_data(df):
	
	# We will mainly keep only quantitative values because they are more useful for Regression
	
	# format to transform dates into datetimes
	dates_format = "%d/%m/%Y %H:%M"
	
	# dict to numerise incident states
	dict_states_int = {
	   "New": 1,
	   "Resolved": 7,
	   "Closed": 8,
	   "Active": 2,
	   "Awaiting User Info": 3,
	   "Awaiting Problem": 4,
	   "Awaiting Vendor": 5,
	   "Awaiting Evidence": 6,
	   "-100": 0
	}
	
	ndf = pd.DataFrame({
		"opened_at_datetime": [datetime.strptime(x, dates_format) for x in df["opened_at"]],
		#"closed_at_datetime": [datetime.strptime(x, dates_format) for x in df["closed_at"]], # may not interest us, because closing tickets are automatic
		"resolved_at_datetime": [datetime.strptime(x, dates_format) if x != '?' else "" for x in df["resolved_at"]],
		"made_sla": df["made_sla"],
		"active": df["active"],
		"incident_state_num": [ dict_states_int[x] for x in df["incident_state"]],
		"reassignment_count": df["reassignment_count"],
		"reopen_count": df["reopen_count"],
		"sys_mod_count": df["sys_mod_count"],
		"sys_updated_at_datetime": [datetime.strptime(x, dates_format) for x in df["sys_updated_at"]],
		"priority": df["priority"], # used instead of urgency and impact because this is a "summary" of both
		"knowledge": df["knowledge"], # might be interesting because if knowledge document isn't used, it may take more time
		"problem_id": df["problem_id"] # might be interesting, because a problem can be more or less long to correct, so the incidents too
	})
	
	
	
	return ndf

'''
	function to print all values of a column in dataframe
'''
def print_values(df, column_name):
	print([x for x in df[column_name].values])

'''
	Function to print grouped values for a column of dataframe, with their counts
'''

def get_grouped_values(df, column_name, verbose=False):
	dic = {}
	
	for val in df[column_name].values:
		if val in dic:
			dic[val] += 1
		else:
			dic[val] = 0
	
	if verbose: print(json.dumps(dic, indent=3))
	return dic

'''
	This section is about testing all current functions
'''

data = import_data()

# example of dates transformations into datetime
'''data_transformed = pd.DataFrame({
	"opened_at_datetime": [datetime.strptime(x, "%d/%m/%Y %H:%M") for x in data["opened_at"]],
	"opened_at": data["opened_at"]
})

print(data_transformed.head(100))'''

# Now transforming all dates
# new functions created to import and transform data

print("transformed and filtered dataframe:")
print(transform_data(data).head(10))


# Printing states different values
get_grouped_values(data, "incident_state")
'''
	This printed
{
   "New": 36406,
   "Resolved": 25750,
   "Closed": 24984,
   "Active": 38715,
   "Awaiting User Info": 14641,
   "Awaiting Problem": 460,
   "Awaiting Vendor": 706,
   "Awaiting Evidence": 37,
   "-100": 4
}

	So we have the eight values as in the documentation, but with an additional '-100' value !
	
	We will create a dictionnary to have fo keys, these different values and for values an integer
	Because for regression we need quantitive information, so, numbers are easier
	
	# tried to get the best indexes to interpret the process going from New (1) to Closed (8)
	dict_states_int = {
	   "New": 1,
	   "Resolved": 7,
	   "Closed": 8,
	   "Active": 2,
	   "Awaiting User Info": 3,
	   "Awaiting Problem": 4,
	   "Awaiting Vendor": 5,
	   "Awaiting Evidence": 6,
	   "-100": 0
	}
	
	So i put it into transformation function
'''





