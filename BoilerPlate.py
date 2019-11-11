import subprocess as sp
import pymysql
import pymysql.cursors

def access(ch , Id):
	cur = con.cursor()
	if ch == 1:
		query = "SELECT POJailId FROM POLICEOFFICER WHERE (POId = %d)" %(Id)
		cur.execute(query)
		result = cur.fetchall()
		jid = result[0]['POJailId']
		print("You have access only to the tuples that are related to your Jail with JailId %d in the database" %(jid))


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
					print('********')
					formulate(ch)
				elif ch == 3:
					break	
				else:
					print("Please Enter a valid input")	



	except:
		# temp = sp.call('clear',shell=True)
		print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")



