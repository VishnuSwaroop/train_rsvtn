-- phpMyAdmin SQL Dump
-- version 2.11.11.3
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 21, 2016 at 10:55 PM
-- Server version: 5.1.73
-- PHP Version: 5.3.3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

--
-- Database: `cs4400_Team`
--

-- --------------------------------------------------------

--
-- Table structure for table `Customer`
--

CREATE TABLE IF NOT EXISTS `Customer` (
  `Username` varchar(20) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `IsStudent` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`Username`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Customer`
--

INSERT INTO `Customer` (`Username`, `Email`, `IsStudent`) VALUES
('Alannah', 'alannah88@gmail.com', 0),
('Chung', 'chung007@gmail.com', 0),
('Doris', 'doris93@yahoo.com', 0),
('Dustin', 'dustin3@gatech.edu', 1),
('Emmeline', 'emma@gmail.com', 0),
('Felipe', 'felipe7@gatech.edu', 1),
('Harold', 'harry@yahoo.com', 0),
('Imelda', 'imelda01@gatech.edu', 1),
('Jamie', 'jamie_123@gmail.com', 0),
('Kerstin', 'kerstin21@ncsu.edu', 1),
('Louie', 'louie3@gatech.edu', 1),
('Louise', 'louise@gmail.com', 0),
('Martha', 'martha555@cmu.edu', 1),
('Mickey', 'mkey@gatech.edu', 1),
('Nadin', 'nadin33@asu.edu', 1),
('Rong', 'rong@gmail.com', 0),
('Suresh', 'suresh123@nyu.edu', 1),
('Vasilisa', 'vasilisa92@gmail.com', 0),
('Vesa', 'vesa3@gatech.edu', 1),
('Wolfgang', 'wolf_90@gmail.com', 0);

-- --------------------------------------------------------

--
-- Table structure for table `Manager`
--

CREATE TABLE IF NOT EXISTS `Manager` (
  `Username` varchar(20) NOT NULL,
  PRIMARY KEY (`Username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Manager`
--

INSERT INTO `Manager` (`Username`) VALUES
('Augustyn'),
('Carl'),
('Ramesh'),
('Sylvie'),
('Zhen');

-- --------------------------------------------------------

--
-- Table structure for table `Payment_Info`
--

CREATE TABLE IF NOT EXISTS `Payment_Info` (
  `Card_No` char(16) NOT NULL,
  `CVV` char(3) DEFAULT NULL,
  `ExpDate` date NOT NULL,
  `Name_Card` varchar(100) DEFAULT NULL,
  `Username` varchar(20) NOT NULL,
  PRIMARY KEY (`Card_No`),
  KEY `Username` (`Username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Payment_Info`
--

INSERT INTO `Payment_Info` (`Card_No`, `CVV`, `ExpDate`, `Name_Card`, `Username`) VALUES
('1263997188578870', '599', '2022-03-15', 'Jamie Mcguire', 'Jamie'),
('2730698685928800', '969', '2019-10-22', 'Alannah Weber', 'Alannah'),
('2811463231780330', '707', '2018-10-07', 'Louise Best', 'Louise'),
('3886017692852170', '961', '2017-09-15', 'Martha Vargas', 'Martha'),
('4410916087403730', '156', '2022-01-31', 'Dustin Archer', 'Dustin'),
('4549361095792230', '437', '2018-04-11', 'Doris Bailey', 'Doris'),
('4623740075165310', '171', '2022-09-05', 'Mickey Sloan', 'Mickey'),
('4658779934904600', '411', '2018-04-28', 'Imelda Wagner', 'Imelda'),
('5009951809336630', '640', '2019-09-04', 'Kerstin Ortiz', 'Kerstin'),
('6783694124394940', '377', '2019-02-06', 'Chung Huang', 'Chung'),
('7374280413791990', '465', '2023-08-29', 'Rong Chang', 'Rong'),
('7461015428154830', '568', '2021-08-01', 'Suresh Narayan', 'Suresh'),
('7924278168702150', '357', '2017-01-07', 'Jamie Mcguire', 'Jamie'),
('8128612635023660', '740', '2021-06-09', 'Vesa Mason', 'Vesa'),
('8368026918401670', '676', '2026-03-12', 'Martha Vargas', 'Martha'),
('8733917799497230', '525', '2018-12-08', 'Nadin Williams', 'Nadin'),
('9149851928254390', '489', '2017-05-20', 'Mickey Sloan', 'Mickey'),
('9211229940665930', '318', '2017-09-07', 'Rong Chang', 'Rong'),
('9522096293978700', '801', '2021-06-25', 'Harold Stone', 'Harold'),
('9855122229378550', '384', '2016-12-18', 'Dustin Archer', 'Dustin ');

-- --------------------------------------------------------

--
-- Table structure for table `Reservation`
--

CREATE TABLE IF NOT EXISTS `Reservation` (
  `Reservation_ID` char(20) NOT NULL,
  `IsCancelled` tinyint(1) NOT NULL DEFAULT '0',
  `Username` varchar(20) NOT NULL,
  `Card_No` varchar(16) NOT NULL,
  PRIMARY KEY (`Reservation_ID`),
  KEY `Username` (`Username`),
  KEY `Card_No` (`Card_No`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Reservation`
--

INSERT INTO `Reservation` (`Reservation_ID`, `IsCancelled`, `Username`, `Card_No`) VALUES
('1', 0, 'Dustin', '9855122229378550'),
('10', 0, 'Chung', '6783694124394940'),
('11', 0, 'Kerstin', '5009951809336630'),
('12', 0, 'Alannah', '2730698685928800'),
('13', 0, 'Vesa', '8128612635023660'),
('14', 0, 'Harold', '9522096293978700'),
('15', 1, 'Suresh', '7461015428154830'),
('16', 0, 'Dustin', '4410916087403730'),
('17', 0, 'Jamie', '1263997188578870'),
('18', 1, 'Mickey', '4623740075165310'),
('19', 0, 'Rong', '7374280413791990'),
('2', 0, 'Jamie', '7924278168702150'),
('20', 0, 'Martha', '8368026918401670'),
('21', 0, 'Dustin', '9855122229378550'),
('22', 1, 'Jamie', '7924278168702150'),
('23', 0, 'Mickey', '9149851928254390'),
('24', 0, 'Rong', '9211229940665930'),
('25', 0, 'Martha', '3886017692852170'),
('26', 0, 'Doris', '4549361095792230'),
('27', 0, 'Imelda', '4658779934904600'),
('28', 0, 'Louise', '2811463231780330'),
('29', 1, 'Nadin', '8733917799497230'),
('3', 0, 'Mickey', '9149851928254390'),
('30', 0, 'Chung', '6783694124394940'),
('31', 1, 'Kerstin', '5009951809336630'),
('32', 0, 'Alannah', '2730698685928800'),
('33', 0, 'Vesa', '8128612635023660'),
('34', 0, 'Harold', '9522096293978700'),
('35', 0, 'Suresh', '7461015428154830'),
('36', 0, 'Dustin', '4410916087403730'),
('37', 1, 'Jamie', '1263997188578870'),
('38', 0, 'Mickey', '4623740075165310'),
('39', 0, 'Rong', '7374280413791990'),
('4', 1, 'Rong', '9211229940665930'),
('40', 1, 'Martha', '8368026918401670'),
('5', 0, 'Martha', '3886017692852170'),
('6', 1, 'Doris', '4549361095792230'),
('7', 0, 'Imelda', '4658779934904600'),
('8', 0, 'Louise', '2811463231780330'),
('9', 1, 'Nadin', '8733917799497230');

-- --------------------------------------------------------

--
-- Table structure for table `Reserves`
--

CREATE TABLE IF NOT EXISTS `Reserves` (
  `Reservation_ID` varchar(20) NOT NULL,
  `Train_No` varchar(10) NOT NULL,
  `Class` enum('First Class','Second Class') NOT NULL,
  `DepDate` date NOT NULL,
  `PassengerName` varchar(100) NOT NULL,
  `No_Bags` int(11) DEFAULT NULL,
  `Departs_From` varchar(20) NOT NULL,
  `Arrives_At` varchar(20) NOT NULL,
  PRIMARY KEY (`Reservation_ID`,`Train_No`),
  KEY `Train_No` (`Train_No`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Reserves`
--

INSERT INTO `Reserves` (`Reservation_ID`, `Train_No`, `Class`, `DepDate`, `PassengerName`, `No_Bags`, `Departs_From`, `Arrives_At`) VALUES
('1', '114885', 'First Class', '2016-01-06', 'Dustin Archer', 1, 'Big Four Depot', 'Chicago Union Statio'),
('10', '397782', 'Second Class', '2016-03-09', 'Chung Huang', 3, 'Fremont Station', 'Boston Back Bay'),
('11', '958273', 'Second Class', '2016-03-16', 'Kerstin Ortiz', 0, 'Chicago Union Statio', 'Penn Station'),
('12', '671373', 'First Class', '2016-03-24', 'Alannah Weber', 1, 'Fremont Station', 'Big Four Depot'),
('13', '631289', 'Second Class', '2016-03-28', 'Vesa Mason', 2, 'Penn Station', 'Fremont Station'),
('14', '114885', 'Second Class', '2016-03-29', 'Harold Stone', 1, 'Big Four Depot', 'Chicago Union Statio'),
('15', '114885', 'First Class', '2016-03-29', 'Suresh Narayan', 0, 'Big Four Depot', 'Chicago Union Statio'),
('15', '743603', 'Second Class', '2016-04-04', 'Suresh Narayan', 2, 'Boston Back Bay', 'Chicago Union Statio'),
('16', '423054', 'Second Class', '2016-04-14', 'Dustin Archer', 3, 'Big Four Depot', 'Peachtree Station'),
('17', '720418', 'Second Class', '2016-04-16', 'Jamie Mcguire', 4, 'Peachtree Station', 'Chicago Union Statio'),
('18', '958273', 'Second Class', '2016-04-18', 'Mickey Sloan', 0, 'Chicago Union Statio', 'Penn Station'),
('19', '631289', 'First Class', '2016-04-19', 'Rong Chang', 2, 'Penn Station', 'Fremont Station'),
('2', '631289', 'Second Class', '2016-01-08', 'Jamie Mcguire', 2, 'Penn Station', 'Fremont Station'),
('20', '743603', 'Second Class', '2016-04-23', 'Martha Vargas', 1, 'Boston Back Bay', 'Chicago Union Statio'),
('21', '114885', 'First Class', '2016-04-27', 'Dustin Archer', 4, 'Big Four Depot', 'Chicago Union Statio'),
('21', '958273', 'Second Class', '2016-03-27', 'Dustin Archer', 3, 'Chicago Union Statio', 'Penn Station'),
('22', '671373', 'Second Class', '2016-04-29', 'Jamie Mcguire', 0, 'Fremont Station', 'Big Four Depot'),
('23', '958273', 'Second Class', '2016-05-02', 'Mickey Sloan', 3, 'Chicago Union Statio', 'Penn Station'),
('24', '423054', 'Second Class', '2016-05-03', 'Rong Chang', 1, 'Big Four Depot', 'Peachtree Station'),
('25', '397782', 'Second Class', '2016-05-24', 'Martha Vargas', 2, 'Fremont Station', 'Boston Back Bay'),
('25', '720418', 'First Class', '2016-05-04', 'Martha Vargas', 0, 'Peachtree Station', 'Chicago Union Statio'),
('26', '720418', 'Second Class', '2016-05-07', 'Doris Bailey', 3, 'Peachtree Station', 'Chicago Union Statio'),
('27', '631289', 'Second Class', '2016-05-08', 'Imelda Wagner', 4, 'Penn Station', 'Fremont Station'),
('28', '743603', 'Second Class', '2016-05-11', 'Louise Best', 2, 'Boston Back Bay', 'Chicago Union Statio'),
('29', '397782', 'Second Class', '2016-05-12', 'Nadin Williams', 1, 'Fremont Station', 'Boston Back Bay'),
('3', '397782', 'Second Class', '2016-01-27', 'Mickey Sloan', 3, 'Fremont Station', 'Boston Back Bay'),
('30', '958273', 'First Class', '2016-05-14', 'Chung Huang', 3, 'Chicago Union Statio', 'Penn Station'),
('31', '114885', 'Second Class', '2016-02-20', 'Kerstin Ortiz', 0, 'Big Four Depot', 'Chicago Union Statio'),
('31', '720418', 'Second Class', '2016-05-15', 'Kerstin Ortiz', 2, 'Peachtree Station', 'Chicago Union Statio'),
('32', '397782', 'Second Class', '2016-05-16', 'Alannah Weber', 4, 'Fremont Station', 'Boston Back Bay'),
('33', '720418', 'Second Class', '2016-05-19', 'Vesa Mason', 3, 'Peachtree Station', 'Chicago Union Statio'),
('34', '743603', 'Second Class', '2016-05-20', 'Harold Stone', 0, 'Boston Back Bay', 'Chicago Union Statio'),
('35', '114885', 'First Class', '2016-05-24', 'Suresh Narayan', 4, 'Big Four Depot', 'Chicago Union Statio'),
('36', '743603', 'Second Class', '2016-05-25', 'Dustin Archer', 1, 'Boston Back Bay', 'Chicago Union Statio'),
('37', '720418', 'Second Class', '2016-05-26', 'Jamie Mcguire', 2, 'Peachtree Station', 'Chicago Union Statio'),
('38', '631289', 'Second Class', '2016-05-27', 'Mickey Sloan', 0, 'Penn Station', 'Fremont Station'),
('39', '397782', 'Second Class', '2016-05-29', 'Rong Chang', 3, 'Fremont Station', 'Boston Back Bay'),
('4', '743603', 'Second Class', '2016-02-04', 'Rong Chang', 2, 'Boston Back Bay', 'Chicago Union Statio'),
('4', '958273', 'First Class', '2016-01-28', 'Rong Chang', 4, 'Chicago Union Statio', 'Penn Station'),
('40', '423054', 'Second Class', '2016-05-31', 'Martha Vargas', 1, 'Big Four Depot', 'Peachtree Station'),
('40', '631289', 'Second Class', '2016-04-01', 'Martha Vargas', 2, 'Penn Station', 'Fremont Station'),
('5', '671373', 'Second Class', '2016-02-10', 'Martha Vargas', 3, 'Fremont Station', 'Big Four Depot'),
('6', '114885', 'Second Class', '2016-02-23', 'Doris Bailey', 4, 'Big Four Depot', 'Chicago Union Statio'),
('7', '423054', 'First Class', '2016-03-03', 'Imelda Wagner', 0, 'Big Four Depot', 'Peachtree Station'),
('8', '423054', 'Second Class', '2016-03-04', 'Louise Best', 2, 'Big Four Depot', 'Peachtree Station'),
('9', '631289', 'Second Class', '2016-03-06', 'Nadin Williams', 1, 'Penn Station', 'Fremont Station'),
('9', '720418', 'Second Class', '2016-03-08', 'Nadin Williams', 4, 'Peachtree Station', 'Chicago Union Statio');

-- --------------------------------------------------------

--
-- Table structure for table `Review`
--

CREATE TABLE IF NOT EXISTS `Review` (
  `Review_No` varchar(10) NOT NULL,
  `Comment` varchar(500) DEFAULT NULL,
  `Rating` enum('Very Good','Good','Neutral','Bad','Very Bad') NOT NULL,
  `Username` varchar(20) DEFAULT NULL,
  `Train_No` varchar(10) NOT NULL,
  PRIMARY KEY (`Review_No`),
  KEY `Username` (`Username`),
  KEY `Train_No` (`Train_No`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Review`
--

INSERT INTO `Review` (`Review_No`, `Comment`, `Rating`, `Username`, `Train_No`) VALUES
('1', 'Good food', 'Very Good', 'Dustin', '114885'),
('10', NULL, 'Neutral', NULL, '958273'),
('11', NULL, 'Very Good', NULL, '423054'),
('12', NULL, 'Good', 'Suresh', '114885'),
('13', NULL, 'Bad', 'Martha', '743603'),
('14', NULL, 'Good', 'Dustin', '958273'),
('15', 'Bad service', 'Very Bad', 'Nadin', '631289'),
('16', 'Excellent hospitality', 'Very Good', NULL, '397782'),
('17', NULL, 'Good', NULL, '720418'),
('18', NULL, 'Neutral', NULL, '423054'),
('19', NULL, 'Bad', NULL, '631289'),
('2', NULL, 'Good', 'Mickey', '397782'),
('20', NULL, 'Good', 'Martha', '671373'),
('3', NULL, 'Neutral', NULL, '423054'),
('4', NULL, 'Bad', NULL, '631289'),
('5', 'Train was delayed', 'Very Bad', 'Alannah', '671373'),
('6', NULL, 'Good', NULL, '720418'),
('7', NULL, 'Neutral', NULL, '743603'),
('8', NULL, 'Good', 'Rong', '958273'),
('9', 'Train was dirty', 'Bad', 'Jamie', '631289');

-- --------------------------------------------------------

--
-- Table structure for table `Station`
--

CREATE TABLE IF NOT EXISTS `Station` (
  `Name` varchar(20) NOT NULL,
  `Location` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Station`
--

INSERT INTO `Station` (`Name`, `Location`) VALUES
('Big Four Depot', 'Lafayette'),
('Boston Back Bay', 'Boston'),
('Chicago Union Statio', 'Chicago'),
('Fremont Station', 'Fremont'),
('Peachtree Station', 'Atlanta'),
('Penn Station', 'Baltimore');

-- --------------------------------------------------------

--
-- Table structure for table `Stop`
--

CREATE TABLE IF NOT EXISTS `Stop` (
  `Train_No` varchar(10) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Arrival_Time` time NOT NULL,
  `Depart_Time` time NOT NULL,
  PRIMARY KEY (`Train_No`,`Name`),
  KEY `Name` (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Stop`
--

INSERT INTO `Stop` (`Train_No`, `Name`, `Arrival_Time`, `Depart_Time`) VALUES
('114885', 'Big Four Depot', '14:05:00', '14:30:00'),
('114885', 'Boston Back Bay', '18:15:00', '18:30:00'),
('114885', 'Chicago Union Statio', '20:05:00', '21:00:00'),
('397782', 'Big Four Depot', '14:25:00', '14:45:00'),
('397782', 'Boston Back Bay', '17:40:00', '18:00:00'),
('397782', 'Fremont Station', '08:05:00', '09:00:00'),
('423054', 'Big Four Depot', '12:40:00', '13:05:00'),
('423054', 'Peachtree Station', '18:40:00', '18:55:00'),
('423054', 'Penn Station', '14:50:00', '15:00:00'),
('631289', 'Chicago Union Statio', '13:30:00', '13:40:00'),
('631289', 'Fremont Station', '16:00:00', '16:30:00'),
('631289', 'Penn Station', '08:45:00', '09:00:00'),
('671373', 'Big Four Depot', '21:35:00', '22:00:00'),
('671373', 'Fremont Station', '10:15:00', '10:30:00'),
('671373', 'Penn Station', '20:05:00', '20:25:00'),
('720418', 'Big Four Depot', '07:00:00', '08:00:00'),
('720418', 'Chicago Union Statio', '13:30:00', '13:50:00'),
('720418', 'Peachtree Station', '06:20:00', '06:45:00'),
('743603', 'Boston Back Bay', '06:10:00', '06:30:00'),
('743603', 'Chicago Union Statio', '22:25:00', '23:00:00'),
('743603', 'Peachtree Station', '10:05:00', '10:20:00'),
('958273', 'Big Four Depot', '18:50:00', '19:15:00'),
('958273', 'Chicago Union Statio', '11:10:00', '11:30:00'),
('958273', 'Penn Station', '21:10:00', '22:05:00');

-- --------------------------------------------------------

--
-- Table structure for table `System_Info`
--

CREATE TABLE IF NOT EXISTS `System_Info` (
  `Max_Bags` int(11) NOT NULL,
  `No_Free_Bags` int(11) DEFAULT NULL,
  `StudentDiscount` decimal(15,2) DEFAULT NULL,
  `ChangeFee` decimal(15,2) DEFAULT NULL,
  PRIMARY KEY (`Max_Bags`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `System_Info`
--


-- --------------------------------------------------------

--
-- Table structure for table `Train_Route`
--

CREATE TABLE IF NOT EXISTS `Train_Route` (
  `Class1Price` decimal(15,2) DEFAULT NULL,
  `Class2Price` decimal(15,2) DEFAULT NULL,
  `Train_No` varchar(10) NOT NULL,
  PRIMARY KEY (`Train_No`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Train_Route`
--

INSERT INTO `Train_Route` (`Class1Price`, `Class2Price`, `Train_No`) VALUES
(120.00, 60.00, '114885'),
(30.00, 20.00, '397782'),
(25.00, 15.00, '423054'),
(40.00, 25.00, '631289'),
(55.00, 30.00, '671373'),
(60.00, 40.00, '720418'),
(85.00, 50.00, '743603'),
(100.00, 75.00, '958273');

-- --------------------------------------------------------

--
-- Table structure for table `User`
--

CREATE TABLE IF NOT EXISTS `User` (
  `Username` varchar(20) NOT NULL,
  `Password` varchar(20) NOT NULL,
  PRIMARY KEY (`Username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `User`
--

INSERT INTO `User` (`Username`, `Password`) VALUES
('Alannah', 'r5j9bju2JVjN8Ldw'),
('Augustyn', '7DckXez9QHGvcspz'),
('Carl', '8QRdV4be2542NvPR'),
('Chung', 'EnfQY5ZFFMVDbTs8'),
('Doris', 'GvLaH2NcGyxehDhT'),
('Dustin', '6DQng82R6hjAxUTS'),
('Emmeline', 'UvvDfFEjt5xbgpLY'),
('Felipe', 'gzGbRmenS5RDGF76'),
('Harold', 'Z9ZEAhjC5j22bp2U'),
('Imelda', 'mJMf4csVpD9Xe9Tq'),
('Jamie', 'PGgjGFUZ5HgZcz5S'),
('Kerstin', 'GKm3XpyydLEutXgS'),
('Louie', 'asZQXHas5cTPVkGN'),
('Louise', '2Ab9CDBeYu4shjkc'),
('Martha', 'v44qZXENqr5QjQmw'),
('Mickey', '3KF3FSVb2ZEDdCub'),
('Nadin', 'AcwW3m2AYWxw4X5F'),
('Ramesh', 'XPrCuTz7Vk9xNxxr'),
('Rong', '6D5mgCjj8hmw4qWG'),
('Suresh', 'hny3xUh2Tm2eX44m'),
('Sylvie', '32yYsazAg9FkEYUj'),
('Vasilisa', 'fLs2NNubVgKmQJaw'),
('Vesa', '4cV56BpfKffSuvKE'),
('Wolfgang', 'bqYhE5gT2KFgwqm9'),
('Zhen', 'bUBsvB4vwBT49Fv9');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Customer`
--
ALTER TABLE `Customer`
  ADD CONSTRAINT `Customer_ibfk_1` FOREIGN KEY (`Username`) REFERENCES `User` (`Username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Manager`
--
ALTER TABLE `Manager`
  ADD CONSTRAINT `Manager_ibfk_1` FOREIGN KEY (`Username`) REFERENCES `User` (`Username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Payment_Info`
--
ALTER TABLE `Payment_Info`
  ADD CONSTRAINT `Payment_Info_ibfk_1` FOREIGN KEY (`Username`) REFERENCES `Customer` (`Username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Reservation`
--
ALTER TABLE `Reservation`
  ADD CONSTRAINT `Reservation_ibfk_2` FOREIGN KEY (`Card_No`) REFERENCES `Payment_Info` (`Card_No`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `Reservation_ibfk_1` FOREIGN KEY (`Username`) REFERENCES `Customer` (`Username`) ON DELETE NO ACTION ON UPDATE CASCADE;

--
-- Constraints for table `Reserves`
--
ALTER TABLE `Reserves`
  ADD CONSTRAINT `Reserves_ibfk_2` FOREIGN KEY (`Train_No`) REFERENCES `Train_Route` (`Train_No`) ON UPDATE CASCADE,
  ADD CONSTRAINT `Reserves_ibfk_1` FOREIGN KEY (`Reservation_ID`) REFERENCES `Reservation` (`Reservation_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Review`
--
ALTER TABLE `Review`
  ADD CONSTRAINT `Review_ibfk_2` FOREIGN KEY (`Train_No`) REFERENCES `Train_Route` (`Train_No`) ON DELETE NO ACTION ON UPDATE CASCADE,
  ADD CONSTRAINT `Review_ibfk_1` FOREIGN KEY (`Username`) REFERENCES `Customer` (`Username`) ON DELETE NO ACTION ON UPDATE CASCADE;

--
-- Constraints for table `Stop`
--
ALTER TABLE `Stop`
  ADD CONSTRAINT `Stop_ibfk_2` FOREIGN KEY (`Name`) REFERENCES `Station` (`Name`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Stop_ibfk_1` FOREIGN KEY (`Train_No`) REFERENCES `Train_Route` (`Train_No`) ON DELETE CASCADE ON UPDATE CASCADE;
