statement1="SELECT * FROM User WHERE Username='%s' AND Password='%s'"

statement2="SELECT * FROM Customer WHERE Username='%s'"

statement3="SELECT * FROM Manager WHERE Username='%s'"

statement4="INSERT INTO User (Username,Password) VALUES ('%s','%s')"

statement5="INSERT INTO Customer (Username,Email) VALUES ('%s','%s')"

statement6="INSERT INTO Customer (Username,Email,IsStudent) VALUES ('%s','%s','%d')"

statement7="SELECT * FROM Customer WHERE Username='%s'"

statement8="SELECT * FROM Customer WHERE Email='%s'"

statement9="UPDATE Customer SET IsStudent = 1 WHERE Username='%s'"

