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

