statement1="SELECT * FROM User WHERE Username='%s' AND Password='%s'"

statement2="SELECT * FROM Customer WHERE Username='%s'"

statement3="SELECT * FROM Manager WHERE Username='%s'"

statement4="INSERT INTO User (Username,Password) VALUES ('%s','%s')"

statement5="INSERT INTO Customer (Username,Email) VALUES ('%s','%s')"

statement6="INSERT INTO Customer (Username,Email,IsStudent) VALUES ('%s','%s','%d')"

statement7="SELECT * FROM Customer WHERE Username='%s'"

statement8="SELECT * FROM Customer WHERE Email='%s'"

statement9="UPDATE Customer SET IsStudent = 1 WHERE Username='%s'"

statement10="SELECT Stop.Train_No,Stop.Arrival_Time,Stop.Depart_Time,Stop.Name,Station.Location FROM Stop JOIN Station ON Stop.Name=Station.Name WHERE Train_No='%s' ORDER BY Arrival_time"

statement11="SELECT DISTINCT Stop.Name FROM Stop WHERE Stop.Depart_Time IN (SELECT min( Stop.Depart_Time )      FROM Stop      GROUP BY Stop.Train_No)"

statement12="SELECT p1.Name, p1.Train_No FROM (SELECT S1.Train_No, S1.Name FROM Stop AS S1 LEFT JOIN Stop AS S2 ON (S1.Train_No=S2.Train_No AND S1.Arrival_Time<S2.Arrival_Time) WHERE S2.Depart_Time IS NULL)AS p1 JOIN (SELECT Stop.Name,Stop.Train_No FROM Stop WHERE Stop.Depart_Time IN (SELECT min(Stop.Depart_Time) FROM Stop GROUP BY Stop.Train_No) AND Stop.Name='%s')AS p2 ON p1.Train_No=p2.Train_No"

statement13="SELECT p3.Train_No AS 'Train Number',p3.Duration,p4.Class1Price AS '1st Class Price',p4.Class2Price AS '2nd Class Price' FROM (SELECT p1.Train_No, TIMEDIFF(p1.Arrival_Time,p2.Depart_Time) AS Duration   	FROM (SELECT S1.Train_No,S1.Arrival_Time FROM Stop AS S1 LEFT JOIN Stop AS S2 ON (S1.Train_No=S2.Train_No AND S1.Arrival_Time<S2.Arrival_Time) WHERE S2.Depart_Time IS NULL)AS p1   	JOIN   	(SELECT Stop.Train_No, Stop.Depart_Time FROM Stop WHERE Stop.Depart_Time IN (SELECT min(Stop.Depart_Time) FROM Stop GROUP BY Stop.Train_No) AND Stop.Name='%s')AS p2   	ON p1.Train_No=p2.Train_No) AS p3 JOIN (SELECT X.Class1Price,X.Class2Price,X.Train_No FROM Train_Route AS X) AS p4 ON p3.Train_No=p4.Train_No"

statement14="INSERT INTO Reservation (Username,Card_No) VALUES (‘%s’,’0’) INSERT INTO Reserves (Departs_From,DepDate,Train_No,Class,PassengerName,Arrives_At) VALUES (‘%s’,’0000-00-00’,’0’,’Second Class’,’0’,’0’)"
