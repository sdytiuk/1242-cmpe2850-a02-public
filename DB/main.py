import mysql.connector
#you need mysql-connector-python package

mydb = None
pw = "demo_password"

try:
    mydb = mysql.connector.connect(
        host="thor.cnt.sast.ca",
        user="demo_user",
        password=pw,
        database="demo_project"
    )
except mysql.connector.Error as err:
    print(f'Something went wrong: {err}')

#check that you have a connection
if mydb != None and mydb.is_connected():
    print(f'Connected : {mydb.get_server_info()}')

try:
    #1st method - NO DICTIONARY
    cursor = mydb.cursor(buffered=True)
    query = f"select * from authors where state like %s" #Single Parameter to substitute
    filter = "CA"
    params = (filter,) #params need to be in a tuple!!
    cursor.execute(query, params)

    #column names
    column_names = cursor.column_names

    resultset = cursor.fetchall()

except mysql.connector.Error as err:
    print(f'Something went wrong: {err}')
    resultset = None
finally:
    cursor.close()

print(column_names)
print(resultset)

row = dict(zip(column_names, resultset[0])) #make dict of first row
print(row)

#now with more params and DICTIONARY!!
try:
    #2nd method: DICTIONARY
    cursor = mydb.cursor(buffered=True, dictionary=True)
    query = f"select * from authors where state like %s or state like %s"
    #2 Parameters to substitute
    filter = "%"
    filter2 = 'IN'
    params = (filter,filter2) #params need to be in a tuple!!
    cursor.execute(query, params)

    #column names
    column_names = cursor.column_names

    resultset = cursor.fetchall()

except mysql.connector.Error as err:
    print(f'Something went wrong: {err}')
    resultset = None
finally:
    cursor.close()

print(resultset)

for row in resultset:
    print(row)

test_data = [{'name':'Cole','Grade':100},{'name':'Jacob','Grade':1}]

iterable = map(lambda x: x['Grade'],test_data)
print(sum(iterable)) #the sum exhausts the iterable



#if you exhaust the iterable, the items are gone!!
for i in iterable:
    print(i)

iter_to_list = list(iterable)

print(iter_to_list)

