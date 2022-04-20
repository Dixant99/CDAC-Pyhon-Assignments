import cx_Oracle

try:
    con = cx_Oracle.connect("system/Cdac1234@localhost:1522/orcl")
    cursor = con.cursor()

    cursor.execute("select Description,sum(qtydisp) from PRODUCT_MASTER, SALES_ORDER_DETAILS where PRODUCT_MASTER.PRODUCTNO = SALES_ORDER_DETAILS.PRODUCTNO group by DESCRIPTION");
    cursor.execute("select c.clientno, avg(s.qtydisp) from SALES_ORDER_DETAILS s, SALES_ORDER so, CLIENT_MASTER c where c.clientno = c.clientno and so.orderno=s.orderno group by c.clientno having max(s.qtyordered*s.productrate)>15000");
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
