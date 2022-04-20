CREATE TABLE CLIENT_MASTER (   
  CLIENTNO varchar(6) Check (CLIENTNO LIKE 'C%') Primary Key,   
  NAME varchar(20) NOT NULL,   
  CITY varchar(15),   
  PINCODE Number(8),   
  STATE varchar(15),   
  BALDUE Number(10,2));

INSERT ALL   
  INTO CLIENT_MASTER values ('C00001','Ivan Bayross','Mumbai',400054,'Maharastra',15000)   
  INTO CLIENT_MASTER values ('C00003','Chhaya Bankar','Mumbai',400057,'Maharastra',5000)   
  INTO CLIENT_MASTER values ('C00004','Ashwini Joshi','Banglore',560001,'karnataka',0)   
  INTO CLIENT_MASTER values ('C00005','hansel Colaco','Mumbai',400060,'Maharastra',2000)   
  INTO CLIENT_MASTER values ('C00006','Deepak Sharma','Mangalore',560050,'Karnataka',0)   
  SELECT 1 FROM DUAL;

select * from CLIENT_MASTER;

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

CREATE TABLE SALES_ORDER (  
ORDERNO varchar(6)  CHECK ('ORDERNO' like 'O%') PRIMARY KEY ,  
CLIENTNO varchar(6) ,  
ORDERDATE date NOT NULL,  
DELYADDR varchar(25) ,  
SALESMANNO varchar(6) ,  
DELYTYPE char(1) ,  
BILLYN char(1) ,  
DELYDATE date ,  
ORDERSTATUS varchar(15) ,  
CONSTRAINT sales_order_fk_1 FOREIGN KEY (CLIENTNO) REFERENCES CLIENT_MASTER (CLIENTNO),  
CONSTRAINT sales_order_fk_2 FOREIGN KEY (SALESMANNO) REFERENCES SALESMAN_MASTER (SALESMANNO)  
) ;

INSERT ALL   
  INTO SALES_ORDER values ('O19001','C00001',DATE'2002-06-12','Delhi','S00001','F','N',DATE'2002-07-20','In Process')  
  INTO SALES_ORDER values ('O19003','C00001',DATE'2002-04-03','Delhi','S00001','F','Y',DATE'2002-04-07','Fulfilled')  
  INTO SALES_ORDER values ('O19008','C00005',DATE'2002-05-24','Delhi','S00004','F','N',DATE'1996-06-26','In Process')  
  INTO SALES_ORDER values ('O46866','C00004',DATE'2002-05-20','Delhi','S00002','P','N',DATE'2002-05-22','Cancelled')  
  INTO SALES_ORDER values ('O19002','C00003',DATE'2002-06-25','Delhi','S00002','P','N',DATE'2002-07-27','Cancelled')  
  SELECT 1 FROM DUAL;

select * from SALES_ORDER;

