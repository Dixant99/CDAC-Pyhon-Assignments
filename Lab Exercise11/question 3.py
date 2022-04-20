import cx_Oracle

try:
    con = cx_Oracle.connect("system/Cdac1234@localhost:1522/orcl")
    cursor = con.cursor()

    cursor.execute("select city from CLIENT_MASTER where name LIKE '_a%'");
    cursor.execute("select name from CLIENT_MASTER where city LIKE 'm%'");
    cursor.execute("select name from CLIENT_MASTER where city = 'manglore' OR city = 'banglore");
    cursor.execute("select Baldue from CLIENT_MASTER where Baldue>10000");
    cursor.execute("select * from SALE_ORDER where orderdate Between '01-JUN-01' and '30-JUN-02'");
    cursor.execute("select orderno,TO_CHAR(orderdate,'day')from sale_order");
    cursor.execute("select name,city,state from CLIENT_MASTER where not state ='maharashtra'");
    records =cursor.fetchall()
    print(records)

    con.commit()
    print("Successful")

except cx_Oracle.DatabaseError as e:
    print("There is some error",e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
