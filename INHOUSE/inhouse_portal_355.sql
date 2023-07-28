-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 26, 2022 at 03:27 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `inhouse`
--

-- --------------------------------------------------------

--
-- Table structure for table `departments`
--

CREATE TABLE `departments` (
  `dept_id` int(225) NOT NULL,
  `department_name` varchar(225) NOT NULL,
  `location` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `departments`
--

INSERT INTO `departments` (`dept_id`, `department_name`, `location`) VALUES
(1, 'IT', 'Bangalore'),
(2, 'Finances', 'Bangalore'),
(3, 'Accounting', 'Delhi');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `EMP_ID` int(11) DEFAULT NULL,
  `FIRST_NAME` varchar(30) DEFAULT NULL,
  `LAST_NAME` varchar(30) DEFAULT NULL,
  `ROLE_ID` int(11) DEFAULT NULL,
  `MANAGER_ID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `employees`
--

CREATE TABLE `employees` (
  `emp_id` int(11) NOT NULL,
  `first_name` varchar(14) NOT NULL,
  `last_name` varchar(16) NOT NULL,
  `ROLE_ID` int(11) NOT NULL,
  `manager_id` int(11) NOT NULL,
  `dept_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employees`
--

INSERT INTO `employees` (`emp_id`, `first_name`, `last_name`, `ROLE_ID`, `manager_id`, `dept_id`) VALUES
(1, 'ROHIT', 'ROSHAN', 1, 0, 1),
(2, 'RAHUL', 'ROSHAN', 2, 1, 1),
(3, 'HRITHIK', 'ROSHAN', 3, 1, 1),
(4, 'RAKESH', 'ROSHAN', 4, 1, 1),
(5, 'ANANYA', 'PANDEY', 1, 0, 2),
(6, 'MONIKA', 'AGRAWAL', 2, 5, 2),
(7, 'DISHA', 'PANDEY', 3, 5, 2),
(8, 'PRIYANKA', 'PANDEY', 4, 5, 2),
(9, 'MANJUNATH', 'BARIS', 1, 0, 3),
(10, 'ABDUL', 'BARI', 2, 9, 3);

-- --------------------------------------------------------

--
-- Table structure for table `manager`
--

CREATE TABLE `manager` (
  `manager_id` int(11) DEFAULT NULL,
  `department_id` int(225) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `manager`
--

INSERT INTO `manager` (`manager_id`, `department_id`) VALUES
(1, 1),
(5, 2),
(9, 3);

-- --------------------------------------------------------

--
-- Table structure for table `project`
--

CREATE TABLE `project` (
  `project_id` int(11) NOT NULL,
  `no_of_employee` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  `project_manager_id` int(11) DEFAULT NULL,
  `emp_id` int(225) NOT NULL,
  `Title` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `project`
--

INSERT INTO `project` (`project_id`, `no_of_employee`, `role_id`, `project_manager_id`, `emp_id`, `Title`) VALUES
(1, 4, 1, 2, 0, 'Crowdsourcings'),
(2, 4, 2, 6, 0, 'Predicting stocks value'),
(3, 4, 3, 10, 0, 'Automating Health Care');

-- --------------------------------------------------------

--
-- Table structure for table `project_manager`
--

CREATE TABLE `project_manager` (
  `project_id` int(11) DEFAULT NULL,
  `employee_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `project_manager`
--

INSERT INTO `project_manager` (`project_id`, `employee_id`) VALUES
(1, 2),
(2, 6),
(3, 10);

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

CREATE TABLE `role` (
  `Role_id` int(225) NOT NULL,
  `Salary` int(225) NOT NULL,
  `Title` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `role`
--

INSERT INTO `role` (`Role_id`, `Salary`, `Title`) VALUES
(1, 100000, 'Software'),
(2, 500000, 'cloud'),
(3, 50000, 'DBA'),
(4, 200000, 'Data Scientist');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `departments`
--
ALTER TABLE `departments`
  ADD PRIMARY KEY (`dept_id`);

--
-- Indexes for table `employees`
--
ALTER TABLE `employees`
  ADD PRIMARY KEY (`emp_id`),
  ADD KEY `ROLE_ID` (`ROLE_ID`),
  ADD KEY `dept_id` (`dept_id`);

--
-- Indexes for table `manager`
--
ALTER TABLE `manager`
  ADD KEY `manager_id` (`manager_id`),
  ADD KEY `department_id` (`department_id`);

--
-- Indexes for table `project`
--
ALTER TABLE `project`
  ADD PRIMARY KEY (`project_id`),
  ADD KEY `project_manager_id` (`project_manager_id`),
  ADD KEY `role_id` (`role_id`);

--
-- Indexes for table `project_manager`
--
ALTER TABLE `project_manager`
  ADD KEY `employee_id` (`employee_id`),
  ADD KEY `project_id` (`project_id`);

--
-- Indexes for table `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`Role_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `employees`
--
ALTER TABLE `employees`
  ADD CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`ROLE_ID`) REFERENCES `role` (`Role_id`),
  ADD CONSTRAINT `employees_ibfk_2` FOREIGN KEY (`dept_id`) REFERENCES `departments` (`dept_id`);

--
-- Constraints for table `manager`
--
ALTER TABLE `manager`
  ADD CONSTRAINT `manager_ibfk_1` FOREIGN KEY (`manager_id`) REFERENCES `employees` (`emp_id`),
  ADD CONSTRAINT `manager_ibfk_2` FOREIGN KEY (`department_id`) REFERENCES `departments` (`dept_id`);

--
-- Constraints for table `project`
--
ALTER TABLE `project`
  ADD CONSTRAINT `project_ibfk_1` FOREIGN KEY (`project_manager_id`) REFERENCES `employees` (`emp_id`),
  ADD CONSTRAINT `project_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `role` (`Role_id`);

--
-- Constraints for table `project_manager`
--
ALTER TABLE `project_manager`
  ADD CONSTRAINT `project_manager_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`emp_id`),
  ADD CONSTRAINT `project_manager_ibfk_2` FOREIGN KEY (`project_id`) REFERENCES `project` (`project_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
