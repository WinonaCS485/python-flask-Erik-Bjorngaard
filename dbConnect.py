import pymysql

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='xg6856vd',
                             password='*******',
                             db='xg6856vd_University',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        
        #Get user input
        user_input = input("Enter a name to search: ")

        #Select user input from Students
        sql = "SELECT * FROM Students WHERE firstName = '" + user_input + "'"
        
        # execute the SQL command
        cursor.execute(sql)
        
        # get the results
        for result in cursor:
            print (result)
        
      
        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes. 
        # connection.commit()
        

finally:
    connection.close()