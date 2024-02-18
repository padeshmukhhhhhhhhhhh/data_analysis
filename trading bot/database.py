from mysql import connector
con=connector.connect(user="root",password="prasanna",port=3306,host="localhost")
assests=[]
#print(con.is_connected())



#print(assests)
arrow=con.cursor()
arrow.execute("USE work;")
arrow.execute("SELECT exchang,tradingsymbol,symboltoken  FROM stock;")

myresult = arrow.fetchall()

for x in myresult:
  
  #print(x)
  assests.append(x)
arrow.close()
con.close()

#print(con.is_connected())
