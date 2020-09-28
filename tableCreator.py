
import mysql.connector as sql
from mysql.connector import errorcode
import json
import sys



database = 'STASTISTICAL_DATA_ANALYSIS'
user = 'user_name'  # <<<<--- Change here
password = 'your_password' # <<<<--- Change here
branchName = "Chemical_2019" # Table Name  # <<<<--- Change here

path_of_json_file = "path/to/json/file"  # <<<<--- Change here


# creating table
def tableCreation():
	try:
		cursor.execute(f"Create table {branchName}(Rank_No int, RollNo int, Name varchar(30), Cgpa float, Sgpa float, Points int)")

	except sql.Error as e:
		if e.errno == 1050:
			cursor.execute(f"Drop Table {branchName};")
			print(f"Existing table {branchName} removed")
			cursor.execute(f"Create table {branchName}(Rank_No int, RollNo int, Name varchar(30), Cgpa float, Sgpa float, Points int)")


def valueAdder():
	
	for i, item in enumerate(data):

		Rank = item.get("Rank", None)
		RollNo = item.get("Rollno", None)
		Name = item.get("Name", None)
		Cgpa= item.get("Cgpa", None)
		Sgpa= item.get("Sgpa", None)
		Points = item.get("Points", None)
		cursor.execute(f"INSERT INTO {branchName} (Rank_No, RollNo, Name, Cgpa, Sgpa, Points) VALUES (%s, %s, %s, %s, %s, %s)", (Rank, RollNo, Name, Cgpa, Sgpa, Points))



# Removing Duplicates Items
def duplicteValueRemover():

	cursor.execute(f"CREATE TABLE copy_of_{branchName} SELECT DISTINCT Rank_no, RollNo, Name, Cgpa, Sgpa, Points FROM {branchName}")
	cursor.execute(f"Drop Table {branchName};")
	cursor.execute(f"Alter Table copy_of_{branchName} rename to {branchName}")

	print("Duplite Value Removed.")



if __name__ == "__main__": 
	try:
		conn = sql.connect(host='localhost',database=database,user=user,password=password)

		if conn.is_connected():
			print("Connected to MySql Server\n\n")

		cursor = conn.cursor()

	except Exception as e:
		sys.exit("Sorry, Couldn't Connect to Server. Please try again later.")

	with open (path_of_json_file, "r") as file:
		data = json.load(file)

	tableCreation()
	valueAdder()
	duplicteValueRemover()

	conn.commit()
	conn.close()

	print(f"{branchName} table created.")
