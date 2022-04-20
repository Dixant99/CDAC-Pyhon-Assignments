CREATE TABLE SALESMAN_MASTER ( 
SALESMANNO varchar(6) CHECK ('SALESMANNO' like 'S%') PRIMARY KEY, 
SALESMANNAME varchar(20) NOT NULL, 
ADDRESS1 varchar(30) NOT NULL, 
ADDRESS2 varchar(30) , 
CITY varchar(20) , 
PINCODE Number(8), 
STATE varchar(20) , 
SALAMT Number(8,2) Check (SALAMT != 0) NOT NULL, 
TGTTOGET Number(6,2) Check (TGTTOGET != 0) NOT NULL, 
YTDSALES Number(6,2) NOT NULL, 
REMARKS varchar(60)  
);

INSERT ALL  
  INTO SALESMAN_MASTER values ('S00001','Aman','A/14','Worli','Mumbai',400002,'Maharatsra',3000.00,100.00,50.00,'Good') 
  INTO SALESMAN_MASTER values ('S00002','Omkar','65','Nariman','Mumbai',400001,'Maharatsra',3000.00,200.00,100.00,'Good') 
  INTO SALESMAN_MASTER values ('S00003','Raj','P-7','Bandra','Mumbai',400032,'Maharatsra',3000.00,200.00,100.00,'Good') 
  INTO SALESMAN_MASTER values ('S00004','Ashish','A/5','Juhu','Bombay',400044,'Maharatsra',3500.00,200.00,150.00,'Good') 
  SELECT 1 FROM DUAL;

Select * from SALESMAN_MASTER;

