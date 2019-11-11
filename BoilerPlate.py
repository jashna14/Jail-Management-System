import subprocess as sp
import pymysql
import pymysql.cursors

def prisoner(jid):
	print("1. Insert a tuple")
	print("2. Delete a tuple")
	print("3. Insert a tuple")
	print("4. Calculate the age of the prisoner")
	print("5. Calculate the period of captivity left for a prisoner")
	val = input("Choose the query you want to execute> ")
	if val == 1:
		try:
			row = {}
	        print("Enter new prisoner's details: ")
	        name = (input("Name (Fname Lname): ")).split(' ')
	        row["Fname"] = name[0]
	        row["Lname"] = name[1]
	        row["Ssn"] = input("SSN: ")
	        row["Bdate"] = input("Birth Date (YYYY-MM-DD): ")
	        row["Address"] = input("Address: ")
	        row["Sex"] = input("Sex: ")
	        row["Salary"] = float(input("Salary: "))
	        row["Dno"] = int(input("Dno: "))



def access(ch , Id):
	cur = con.cursor()
	if ch == 1:
		query = "SELECT POJailId FROM POLICEOFFICER WHERE (POId = %d)" %(Id)
		cur.execute(query)
		result = cur.fetchall()
		jid = result[0]['POJailId']
		print("You have access only to the tuples that are related to your Jail with JailId %d in the database" %(jid))
		while(1):
			print("1. PRISONER")
			print("2. CRIME")
			print("3. DEPARTMENT")
			print("4. VISITOR")
			print("5. VISITORCONTACT")
			print("6. Exit")
			val = int(input("Choose the Table you want to edit> "))
			if val == 1:
				prisoner(jid)
			if val == 2:
				crime(jid)	
			if val == 3:
				department(jid)
			if val == 4:
				visitor(jid)
			if val == 5:
				visitorconact(jid)
			if val == 6:
				break
			else:
				print("Please Enter a valid input")
	
	elif ch == 2:
		while(1):
			print("1. JAIL")
			print("2. POLICEOFFICER")
			print("3. POLICEOFFICERCONTACT")
			print("4. POLICEOFFICEREMAIL")
			print("5. Exit")
			val = int(input("Choose the Table you want to edit"))
			if val == 1:
				jail()
			if val == 2:
				policeofficer()	
			if val == 3:
				policeofficercontact()
			if val == 4:
				policeofficeremail()
			if val ==5:
				break
			else:
				print("Please Enter a valid input")				

				
							



def formulate(ch):
	cur = con.cursor()

	if ch == 1:
		Id = int(input("Please enter your Id>> "))
		query = "SELECT COUNT(*) FROM POLICEOFFICER WHERE (POId = %d AND JobType = 'Jailer')" %(Id)
		cur.execute(query)
		result = cur.fetchall()
		if result[0]["COUNT(*)"] == 1:
			passw = input("Please enter the Password>> ")
			if passw == 'p':
				print("Access granted")
				access(ch,Id)
			else:
				print("Wrong Password")
		else:
			print("Id not found or the Id does not corresponds to a Jailer")

	if ch == 2:
		passw = input("Please enter the Password>> ")
		if passw == 'p':
			print("Access granted")
			access(ch , -1)
		else:
			print("Wrong Password")




while(1):
	# temp = sp.call('clear',shell=True)
	username = 'root'
	password = '16061999'
	# username = input("Username:")
	# password = input("Password:")

	try:
		con = pymysql.connect(host = 'localhost',
			user=username,
			password=password,
			db='JAILDB',
			cursorclass=pymysql.cursors.DictCursor
			)
		# temp = sp.call('clear',shell=True)

		if(con.open):
			print("Connected")
		else:
			print("Failed to connect")
		
		with con:
			cur = con.cursor()
			while(1):
				# temp = sp.call('clear',shell=True)
				print("1.Enter as a Jailer")
				print("2.Enter as a Government Official")
				print("3.Logout")
				ch = int(input("Enter choice> "))
				# temp = sp.call('clear',shell=True)

				if ch == 1 or ch == 2:
					formulate(ch)
				elif ch == 3:
					break	
				else:
					print("Please Enter a valid input")	



	except:
		# temp = sp.call('clear',shell=True)
		print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")



