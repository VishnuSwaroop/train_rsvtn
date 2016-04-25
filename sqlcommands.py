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
#This is for storing train no into database
statement13="UPDATE Reserves SET Train_No=(SELECT p3.Train_No AS 'Train Number' FROM (SELECT p1.Train_No,p1.Name  FROM (SELECT S1.Train_No,S1.Name FROM Stop AS S1 LEFT JOIN Stop AS S2 ON (S1.Train_No=S2.Train_No AND S1.Arrival_Time<S2.Arrival_Time) WHERE S2.Depart_Time IS NULL)AS p1 JOIN  (SELECT Stop.Train_No FROM Stop WHERE Stop.Depart_Time IN (SELECT min(Stop.Depart_Time) FROM Stop GROUP BY Stop.Train_No) AND Stop.Name='%s')AS p2  ON p1.Train_No=p2.Train_No) AS p3 WHERE p3.Name='%s') ORDER BY Reservation_ID DESC LIMIT 1"

#statement14="INSERT INTO Reservation (Username,Card_No) VALUES ('%s','0') INSERT INTO Reserves (Departs_From,DepDate,Train_No,Class,PassengerName,Arrives_At) VALUES ('%s','0000-00-00','0','Second Class','0','0')"
#The below three will be done when user presses make reservation
statement14="INSERT INTO Train_Route (Train_No) VALUES ('0')"
statement25="INSERT INTO Payment_Info (Card_No,ExpDate,Username) VALUES ('0','0000-00-00','%s')"
statement26="INSERT INTO Reservation (Username,Card_No) VALUES ('%s','0')"
#This will be done when user chooses departs from
statement15="INSERT INTO Reserves (Reservation_ID, Departs_From, DepDate, Train_No, Class, PassengerName,Arrives_At) VALUES ((SELECT MAX(Reservation_ID) FROM Reservation),'%s','0000-00-00','0','Second Class','0','0')"

statement16="UPDATE Reserves SET Arrives_At='%s', DepDate='%s' WHERE Departs_From='%s' ORDER BY Reservation_ID DESC LIMIT 1"
#To search for trains between stations
statement17="SELECT p3.Train_No AS 'Train Number',p3.Duration,p4.Class1Price AS '1st Class Price',p4.Class2Price AS '2nd Class Price' FROM (SELECT p1.Train_No, TIMEDIFF(p1.Arrival_Time,p2.Depart_Time) AS Duration,p1.Name  FROM (SELECT S1.Train_No,S1.Arrival_Time,S1.Name FROM Stop AS S1 LEFT JOIN Stop AS S2 ON (S1.Train_No=S2.Train_No AND S1.Arrival_Time<S2.Arrival_Time) WHERE S2.Depart_Time IS NULL)AS p1 JOIN  (SELECT Stop.Train_No, Stop.Depart_Time FROM Stop WHERE Stop.Depart_Time IN (SELECT min(Stop.Depart_Time) FROM Stop GROUP BY Stop.Train_No) AND Stop.Name=(SELECT Departs_From AS Name FROM Reserves ORDER BY Reservation_ID DESC LIMIT 1))AS p2  ON p1.Train_No=p2.Train_No) AS p3 JOIN (SELECT X.Class1Price,X.Class2Price,X.Train_No FROM Train_Route AS X) AS p4 ON p3.Train_No=p4.Train_No WHERE p3.Name=(SELECT Arrives_At FROM Reserves ORDER BY Reservation_ID DESC LIMIT 1) "


statement18="UPDATE Reserves SET Class='%s' WHERE Train_No='%s' ORDER BY Reservation_ID DESC LIMIT 1"

statement19="UPDATE Reserves SET PassengerName='%s', No_Bags='%s' WHERE Train_No IN (SELECT * FROM (SELECT R.Train_No FROM Reserves AS R) AS X) ORDER BY Reservation_ID DESC LIMIT 1"

statement20="SELECT Train_No FROM Reserves WHERE Reservation_ID = (SELECT R.Reservation_ID FROM Reserves AS R ORDER BY Reservation_ID DESC LIMIT 1) "

statement21="SELECT p3.Duration FROM (SELECT p1.Train_No, TIMEDIFF(p1.Arrival_Time,p2.Depart_Time) AS Duration,p1.Name  FROM (SELECT S1.Train_No,S1.Arrival_Time,S1.Name FROM Stop AS S1 LEFT JOIN Stop AS S2 ON (S1.Train_No=S2.Train_No AND S1.Arrival_Time<S2.Arrival_Time) WHERE S2.Depart_Time IS NULL)AS p1 JOIN  (SELECT Stop.Train_No, Stop.Depart_Time FROM Stop WHERE Stop.Depart_Time IN (SELECT min(Stop.Depart_Time) FROM Stop GROUP BY Stop.Train_No) AND Stop.Name=(SELECT Departs_From AS Name FROM Reserves ORDER BY Reservation_ID DESC LIMIT 1)) AS p2  ON p1.Train_No=p2.Train_No) AS p3 WHERE p3.Name=(SELECT Arrives_At FROM Reserves ORDER BY Reservation_ID DESC LIMIT 1)"
#retreiving class price
statement22="SELECT IF(R.Class='First Class',(SELECT T.Class1Price FROM Train_Route AS T WHERE T.Train_No=R.Train_No),(SELECT T.Class2Price FROM Train_Route AS T WHERE T.Train_No=R.Train_No)) AS Price FROM Reserves AS R ORDER BY R.Reservation_ID DESC LIMIT 1"

statement23="SELECT IsStudent FROM Reserves AS R JOIN Reservation AS S ON R.Reservation_ID=S.Reservation_ID JOIN Customer AS C ON C.Username=S.Username WHERE R.Reservation_ID = (SELECT R2.Reservation_ID FROM Reserves AS R2 ORDER BY R2.Reservation_ID DESC LIMIT 1) "
#placedetails
statement24="SELECT Departs_From, Arrives_At, Class FROM Reserves WHERE Reservation_ID=(SELECT R.Reservation_ID FROM Reserves AS R ORDER BY Reservation_ID DESC LIMIT 1)"

statement27="SELECT Card_No AS Card FROM Payment_Info WHERE Payment_Info.Username='%s' AND Card_No != '0' "

statement32="SELECT No_Bags, PassengerName FROM Reserves WHERE Reservation_ID=(SELECT R.Reservation_ID FROM Reserves AS R ORDER BY Reservation_ID DESC LIMIT 1)"

#Final confirmation to all changes on reservation
statement28="UPDATE Reservation SET Card_No='%s' WHERE Reservation_ID = (SELECT R2.Reservation_ID FROM Reserves AS R2 ORDER BY R2.Reservation_ID DESC LIMIT 1)"

statement29="DELETE FROM Payment_Info WHERE Card_No='0'"

statement30="DELETE FROM Train_Route WHERE Train_No='0'"

statement31="SELECT R.Reservation_ID FROM Reservation AS R LEFT JOIN Reservation S  ON (R.Username = S.Username AND R.Reservation_ID < S.Reservation_ID) WHERE S.Reservation_ID IS NULL AND R.Username='%s' "


#PAyment info stuff
#adding a card
statement33="INSERT INTO Payment_Info (Card_No, CVV, ExpDate, Name_Card, Username) VALUES ('%s','%s','%s','%s','%s') "
#showing the card for deletion

statement34="SELECT Card_No AS Card FROM Payment_Info WHERE Payment_Info.Username='%s' AND Card_No != '0'"
#check if still in use
statement35="SELECT DISTINCT R.Card_No FROM Reservation AS R JOIN Reserves AS S ON R.Reservation_ID=S.Reservation_ID WHERE R.Username='%s' AND S.DepDate<CURDATE()"

#delete the card
statement36="DELETE FROM Payment_Info WHERE Card_No='%s'"

#Update a reservation
#dropdown
statement37="SELECT R.Reservation_ID FROM Reservation AS R WHERE R.Username='%s' AND R.IsCancelled != '1'"

#to get train no
statement38="SELECT R.Train_No FROM Reserves AS R WHERE R.Reservation_ID='%s'"
#duration
statement39="SELECT p3.Duration FROM (SELECT p1.Train_No, TIMEDIFF(p1.Arrival_Time,p2.Depart_Time) AS Duration,p1.Name  FROM (SELECT S1.Train_No,S1.Arrival_Time,S1.Name FROM Stop AS S1 LEFT JOIN Stop AS S2 ON (S1.Train_No=S2.Train_No AND S1.Arrival_Time<S2.Arrival_Time) WHERE S2.Depart_Time IS NULL)AS p1 JOIN  (SELECT Stop.Train_No, Stop.Depart_Time FROM Stop WHERE Stop.Depart_Time IN (SELECT min(Stop.Depart_Time) FROM Stop GROUP BY Stop.Train_No))AS p2  ON p1.Train_No=p2.Train_No) AS p3 WHERE p3.Train_No IN (SELECT Train_No FROM Reserves WHERE Reservation_ID='%s')"
#departsfrom, arrives at, class:
statement40="SELECT Departs_From, Arrives_At, Class FROM Reserves WHERE Reservation_ID='%s' "
#price
statement41="SELECT IF(R.Class='First Class',(SELECT T.Class1Price FROM Train_Route AS T WHERE T.Train_No=R.Train_No),(SELECT T.Class2Price FROM Train_Route AS T WHERE T.Train_No=R.Train_No)) AS Price FROM Reserves AS R WHERE Reservation_ID='%s' "

#bags,psngrname
statement42="SELECT No_Bags, PassengerName FROM Reserves WHERE Reservation_ID='%s'"


#Update a reservation2
#dropdown
# statement43="SELECT R.Reservation_ID FROM Reservation AS R WHERE R.Username='%s' AND R.IsCancelled != '1'"

#to get train no-already known
#statement44="SELECT R.Train_No FROM Reserves AS R WHERE R.Reservation_ID='%s'"
#duration
statement43="SELECT p3.Duration FROM (SELECT p1.Train_No, TIMEDIFF(p1.Arrival_Time,p2.Depart_Time) AS Duration,p1.Name  FROM (SELECT S1.Train_No,S1.Arrival_Time,S1.Name FROM Stop AS S1 LEFT JOIN Stop AS S2 ON (S1.Train_No=S2.Train_No AND S1.Arrival_Time<S2.Arrival_Time) WHERE S2.Depart_Time IS NULL)AS p1 JOIN  (SELECT Stop.Train_No, Stop.Depart_Time FROM Stop WHERE Stop.Depart_Time IN (SELECT min(Stop.Depart_Time) FROM Stop GROUP BY Stop.Train_No))AS p2  ON p1.Train_No=p2.Train_No) AS p3 WHERE p3.Train_No IN (SELECT Train_No FROM Reserves WHERE Reservation_ID='%s') AND p3.Train_No='%s'  "
#departsfrom, arrives at, class:
statement44="SELECT Departs_From, Arrives_At, Class FROM Reserves WHERE Reservation_ID='%s' AND Train_No='%s' "
#price
statement45="SELECT IF(R.Class='First Class',(SELECT T.Class1Price FROM Train_Route AS T WHERE T.Train_No=R.Train_No),(SELECT T.Class2Price FROM Train_Route AS T WHERE T.Train_No=R.Train_No)) AS Price FROM Reserves AS R WHERE Reservation_ID='%s' AND Train_No='%s' "

#bags,psngrname
statement46="SELECT No_Bags, PassengerName FROM Reserves WHERE Reservation_ID='%s' AND Train_No='%s'"

#depdate to check for limmit
statement47="SELECT DATE_SUB(DepDate,INTERVAL 1 DAY) FROM Reserves WHERE Reservation_ID='%s' AND Train_No='%s' "

statement48="UPDATE Reserves SET DepDate ='%s' WHERE Reservation_ID='%s' AND Train_No='%s'"



#change fee
statement49="SELECT ChangeFee FROM System_Info"


#Cancel reservation
#dropdown
statement50="SELECT R.Reservation_ID FROM Reservation AS R WHERE R.Username='%s' AND R.IsCancelled != '1' "
#trainno
statement51="SELECT R.Train_No FROM Reserves AS R WHERE R.Reservation_ID='%s' "
#duration
statement52="SELECT p3.Duration FROM (SELECT p1.Train_No, TIMEDIFF(p1.Arrival_Time,p2.Depart_Time) AS Duration,p1.Name  FROM (SELECT S1.Train_No,S1.Arrival_Time,S1.Name FROM Stop AS S1 LEFT JOIN Stop AS S2 ON (S1.Train_No=S2.Train_No AND S1.Arrival_Time<S2.Arrival_Time) WHERE S2.Depart_Time IS NULL)AS p1 JOIN  (SELECT Stop.Train_No, Stop.Depart_Time FROM Stop WHERE Stop.Depart_Time IN (SELECT min(Stop.Depart_Time) FROM Stop GROUP BY Stop.Train_No))AS p2  ON p1.Train_No=p2.Train_No) AS p3 WHERE p3.Train_No IN (SELECT Train_No FROM Reserves WHERE Reservation_ID='%s') "

#departs from, price,
statement53="SELECT Departs_From, Arrives_At, Class FROM Reserves WHERE Reservation_ID='%s' "

#bags and passenger info
statement54="SELECT No_Bags, PassengerName FROM Reserves WHERE Reservation_ID='%s'"


#canceldifference, if NULL, no reservation

statement55="SELECT DATEDIFF((SELECT R1.DepDate FROM Reserves AS R1 LEFT JOIN Reserves R2 ON R1.Reservation_ID = R2.Reservation_ID AND R1.DepDate > R2.DepDate WHERE R2.DepDate IS NULL AND R1.Reservation_ID='%s'),CURDATE()) "


#cancel reservation
statement56="UPDATE Reservation SET IsCancelled='1'WHERE Reservation_ID='%s'"

#REVIEW
statement57="SELECT Train_No FROM Train_Route "

statement58="SELECT Rating,COUNT(Review_No) AS 'No. of Reviews',(SELECT IF(MAX(Comment)IS NULL,' ',MAX(Comment))) AS Comment FROM Review WHERE Train_No = '%s' GROUP BY Rating,Train_No"

#give review
statement59="INSERT INTO Review (Train_No,Rating,Comment,Username) VALUES ('%s','%s','%s','%s')"

statement60="INSERT INTO Review (Train_No,Rating,Comment,Username) VALUES ('%s','%s','%s','%s') "


#Manager
statement61="SELECT MONTHNAME(STR_TO_DATE((SELECT MONTH(DepDate)), '%m')) AS Month,SUM(X.Price) AS Revenue FROM ( SELECT Reservation_ID,DepDate,(SELECT IF(R.Class='First Class',(SELECT T.Class1Price FROM Train_Route AS T WHERE T.Train_No=R.Train_No),(SELECT T.Class2Price FROM Train_Route AS T WHERE T.Train_No=R.Train_No))) AS Price FROM Reserves AS R ) AS X JOIN Reservation AS S ON X.Reservation_ID=S.Reservation_ID WHERE MONTH(X.DepDate)<MONTH(CURDATE()) AND S.IsCancelled ='0' GROUP BY MONTH(X.DepDate) "


statement62="CREATE OR REPLACE VIEW X1 AS SELECT MONTHNAME(STR_TO_DATE((SELECT MONTH(R.DepDate)), '%m')) AS Month,R.Train_No,COUNT(R.Reservation_ID) AS 'No. of Reservations' FROM Reserves AS R JOIN Reservation AS S ON R.Reservation_ID=S.Reservation_ID WHERE MONTH(R.DepDate)='1' AND S.IsCancelled ='0' GROUP BY MONTH(R.DepDate),R.Train_No"

statement63="CREATE OR REPLACE VIEW X2 AS SELECT MONTHNAME(STR_TO_DATE((SELECT MONTH(R.DepDate)), '%m')) AS Month,R.Train_No,COUNT(R.Reservation_ID) AS 'No. of Reservations' FROM Reserves AS R JOIN Reservation AS S ON R.Reservation_ID=S.Reservation_ID WHERE MONTH(R.DepDate)='2' AND S.IsCancelled ='0' GROUP BY MONTH(R.DepDate),R.Train_No "

statement64="CREATE OR REPLACE VIEW X3 AS SELECT MONTHNAME(STR_TO_DATE((SELECT MONTH(R.DepDate)), '%m')) AS Month,R.Train_No,COUNT(R.Reservation_ID) AS 'No. of Reservations' FROM Reserves AS R JOIN Reservation AS S ON R.Reservation_ID=S.Reservation_ID WHERE MONTH(R.DepDate)='3' AND S.IsCancelled ='0' GROUP BY MONTH(R.DepDate),R.Train_No "

statement65="SELECT * FROM X1 ORDER BY 'No. of Reservations' DESC LIMIT 3 "

statement66="SELECT * FROM X2 ORDER BY 'No. of Reservations' DESC LIMIT 3 "

statement67="SELECT * FROM X3 ORDER BY 'No. of Reservations' DESC LIMIT 3 "