-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 05, 2022 at 01:09 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.0.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pes1ug20cs081_lab10`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `allocated_beds` (IN `hid` VARCHAR(20))   BEGIN
DECLARE booked_normalbed int ;
DECLARE available_normalbed int ;

select count(*) INTO booked_normalbed from bookingpatient where bedtype='normal bed';

select number_of_beds('hid') - count(*) INTO available_normalbed from bookingpatient where bedtype='normal bed';

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `hospital_name` (IN `userid` INT(25))   select hospitaldata.hname, user.id from hospitaldata inner join user on hospitaldata.id = user.id where user.id=userid$$

--
-- Functions
--
CREATE DEFINER=`root`@`localhost` FUNCTION `ALOC_BEDS` (`hid1` VARCHAR(20)) RETURNS INT(10)  BEGIN
DECLARE booked_normalbed int ;

select count(*) INTO booked_normalbed from bookingpatient where bedtype='normal bed';

return booked_normalbed;

END$$

CREATE DEFINER=`root`@`localhost` FUNCTION `AVAILABLE_BEDS` (`hid2` VARCHAR(20)) RETURNS VARCHAR(10) CHARSET utf8mb4  BEGIN
DECLARE available_normalbed int ;

select number_of_beds(hid2) - count(*) INTO available_normalbed from bookingpatient where bedtype='normal bed';
return available_normalbed;

END$$

CREATE DEFINER=`root`@`localhost` FUNCTION `number_of_beds` (`hcode_1` VARCHAR(25)) RETURNS INT(11)  BEGIN
DECLARE temp int;
select sum(normalbed) into temp from hospitaldata where hcode = hcode_1 group by hcode;
return temp;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `bookingpatient`
--

CREATE TABLE `bookingpatient` (
  `id` int(11) NOT NULL,
  `srfid` varchar(50) NOT NULL,
  `bedtype` varchar(50) NOT NULL,
  `hcode` varchar(50) NOT NULL,
  `spo2` int(11) NOT NULL,
  `pname` varchar(50) NOT NULL,
  `pphone` varchar(12) NOT NULL,
  `paddress` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bookingpatient`
--

INSERT INTO `bookingpatient` (`id`, `srfid`, `bedtype`, `hcode`, `spo2`, `pname`, `pphone`, `paddress`) VALUES
(3, 'KA20210011', 'Normal Bed', 'MAT123', 85, 'ARK', '9986786453', 'bangalore'),
(4, 'KA20210022', 'ICU Bed', 'BBH01', 92, 'kartik', '8088131784', 'bangalore'),
(5, 'KA20210033', 'Normal Bed', 'MAT123', 81, 'amogh', '8088828292', 'Mangalore'),
(6, 'KA20210044', 'ICU Bed', 'BBH01', 95, 'chinmay', '9987728913', 'bangalore'),
(7, 'KA20210055', 'ICU Bed', 'BBH01', 88, 'Rida', '7348991204', 'mangalore'),
(8, 'KA20210066', 'Normal Bed', 'MAT123', 87, 'Anuj', '7348993574', 'bangalore'),
(8, 'KA129031', 'Normal Bed', 'MAT123', 88, 'Ram', '83942239481', 'STREET 1234');

-- --------------------------------------------------------

--
-- Table structure for table `hospitaldata`
--

CREATE TABLE `hospitaldata` (
  `id` int(11) NOT NULL,
  `hcode` varchar(200) NOT NULL,
  `hname` varchar(200) NOT NULL,
  `normalbed` int(11) NOT NULL,
  `hicubed` int(11) NOT NULL,
  `icubed` int(11) NOT NULL,
  `vbed` int(11) NOT NULL,
  `add_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hospitaldata`
--

INSERT INTO `hospitaldata` (`id`, `hcode`, `hname`, `normalbed`, `hicubed`, `icubed`, `vbed`, `add_date`) VALUES
(4, 'BBH01', 'Apollo Hospital', 30, 3, 3, 1, NULL),
(5, 'MAT123', 'Matha Hospital', 50, 2, 4, 1, NULL),
(6, 'BBH01', 'Apollo Hospital', 60, 4, 3, 1, NULL),
(7, 'MAT123', 'Matha Hospital', 20, 5, 4, 2, NULL),
(3, 'MAT123', 'Matha Hospital', 40, 4, 4, 1, '2022-11-23 00:02:28');

--
-- Triggers `hospitaldata`
--
DELIMITER $$
CREATE TRIGGER `t1` BEFORE INSERT ON `hospitaldata` FOR EACH ROW begin
declare dt datetime;
select now() into dt;
set new.add_date=dt;
end
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `hospitaluser`
--

CREATE TABLE `hospitaluser` (
  `id` int(11) NOT NULL,
  `hcode` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hospitaluser`
--

INSERT INTO `hospitaluser` (`id`, `hcode`, `email`, `password`) VALUES
(3, 'MAT123', 'aryanpuranik@gmail.com', 'abcd'),
(4, 'BBH01', 'arkprocoder@gmail.com', 'mnop'),
(5, 'MAT123', 'bdbdbb@gmail.com', 'qwerty'),
(6, 'BBH01', 'dbmsdbms@gmail.com', 'asdfg'),
(7, 'MAT123', 'aryanpuar@gmail.com', 'zxcvc');

-- --------------------------------------------------------

--
-- Table structure for table `pes1ug20cs081_train`
--

CREATE TABLE `pes1ug20cs081_train` (
  `Train_No` int(11) DEFAULT NULL,
  `Name` varchar(30) DEFAULT NULL,
  `Train_Type` varchar(20) DEFAULT NULL,
  `Source` varchar(20) DEFAULT NULL,
  `Destination` varchar(20) DEFAULT NULL,
  `Availability` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pes1ug20cs081_train`
--

INSERT INTO `pes1ug20cs081_train` (`Train_No`, `Name`, `Train_Type`, `Source`, `Destination`, `Availability`) VALUES
(62621, 'BEN-CHE Shatabdi', 'Superfast', 'Bangalore', 'Chennai', 'Yes'),
(62620, 'CHE-BEN Shatabdi', 'Superfast', 'Chennai', 'Bangalore', 'yes');

-- --------------------------------------------------------

--
-- Table structure for table `test`
--

CREATE TABLE `test` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `test`
--

INSERT INTO `test` (`id`, `name`) VALUES
(3, 'ARK'),
(4, 'kartik'),
(5, 'amogh'),
(6, 'chinmay'),
(7, 'Rida');

-- --------------------------------------------------------

--
-- Table structure for table `trig`
--

CREATE TABLE `trig` (
  `id` int(11) NOT NULL,
  `hcode` varchar(50) NOT NULL,
  `normalbed` int(11) NOT NULL,
  `hicubed` int(11) NOT NULL,
  `icubed` int(11) NOT NULL,
  `vbed` int(11) NOT NULL,
  `querys` varchar(50) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `srfid` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `dob` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `srfid`, `email`, `dob`) VALUES
(4, 'KA20210022', 'arkprocoder@gmail.com', '2021-10-23'),
(5, 'KA20210033', 'bdbdbb@gmail.com', '2021-10-12'),
(6, 'KA20210044', 'dbmsdbms@gmail.com', '2021-09-18'),
(7, 'KA20210055', 'aryanpuar@gmail.com', '2021-11-12'),
(3, 'KA20210011', 'aryanpuranik@gmail.com', '2021-11-26');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
