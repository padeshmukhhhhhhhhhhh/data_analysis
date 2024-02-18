from mysql import connector
con=connector.connect(user="root",password="prasanna",port=3306,host="localhost")
assests=[]
assests2=[]
#print(con.is_connected())



#print(assests)
arrow=con.cursor()
arrow.execute("USE work;")
arrow.execute("SELECT exchang,tradingsymbol,symboltoken  FROM stock;")

myresult = arrow.fetchall()

for x in myresult:
  
  #print(x)
  assests.append(x)

arrow.execute("SELECT exchang,symboltoken FROM stock;")
second_result = arrow.fetchall()
for x in second_result:
  
  #print(x)
  assests2.append(x)
arrow.close()

con.close()

#print(con.is_connected())
