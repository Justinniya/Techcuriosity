-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 11, 2024 at 03:00 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `techcuriosity`
--

-- --------------------------------------------------------

--
-- Table structure for table `courses`
--

CREATE TABLE `courses` (
  `tech_id` varchar(255) NOT NULL,
  `introduction_to_it` varchar(20) NOT NULL DEFAULT 'False',
  `html` varchar(20) NOT NULL DEFAULT 'False',
  `python_subs` varchar(20) NOT NULL DEFAULT 'False',
  `computing_fund` varchar(20) NOT NULL DEFAULT 'False',
  `database_subs` varchar(20) NOT NULL DEFAULT 'False',
  `networking_subs` varchar(20) NOT NULL DEFAULT 'False',
  `computer_graphics` varchar(20) NOT NULL DEFAULT 'False',
  `cloud_computing` varchar(20) NOT NULL DEFAULT 'False'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `courses`
--

INSERT INTO `courses` (`tech_id`, `introduction_to_it`, `html`, `python_subs`, `computing_fund`, `database_subs`, `networking_subs`, `computer_graphics`, `cloud_computing`) VALUES
('380918152704', 'TRUE', 'TRUE', 'TRUE', 'TRUE', 'TRUE', 'TRUE', 'TRUE', 'TRUE'),
('431899358452', 'TRUE', 'TRUE', 'TRUE', 'False', 'TRUE', 'False', 'False', 'False');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `tech_id` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `money` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`tech_id`, `email`, `name`, `password`, `money`) VALUES
('1', 'justindelavega00@gmail.com', 'Justin De La Vega', 'a', 0),
('2', 'a@gmail.com', 'justin', 'a', 0),
('3', 'd@gmail.com', 'd', '1', 0),
('380918152704', 'natalie@gmail.com', 'natalie', '123', 0),
('4', 'd@gmail.com', 'd', '1', 0),
('431899358452', 'e@gmail.com', 'justin', '1', 0),
('5', 'd@gmail.com', 'd', '1', 0),
('6', 'justindelavega00@gmail.com', 'Justin De La Vega', 'a', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `courses`
--
ALTER TABLE `courses`
  ADD PRIMARY KEY (`tech_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`tech_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
