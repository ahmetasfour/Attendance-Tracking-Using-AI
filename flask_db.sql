-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 12, 2024 at 11:59 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flask_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts`
--

CREATE TABLE `accounts` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `accounts`
--

INSERT INTO `accounts` (`id`, `username`, `password`, `email`) VALUES
(1, 'test', '0ef15de6149819f2d10fc25b8c994b574245f193', 'test@test.com');

-- --------------------------------------------------------

--
-- Table structure for table `accs_hist`
--

CREATE TABLE `accs_hist` (
  `accs_id` int(11) NOT NULL,
  `accs_date` date NOT NULL,
  `accs_student` varchar(3) NOT NULL,
  `accs_added` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `accs_hist`
--

INSERT INTO `accs_hist` (`accs_id`, `accs_date`, `accs_student`, `accs_added`) VALUES
(453, '2024-01-10', '101', '2024-01-10 22:22:40'),
(517, '2024-01-11', '102', '2024-01-11 21:02:08'),
(519, '2024-01-11', '102', '2024-01-11 21:02:27'),
(562, '2024-01-11', '102', '2024-01-11 21:55:23'),
(565, '2024-01-12', '104', '2024-01-12 00:26:37'),
(567, '2024-01-12', '102', '2024-01-12 16:40:32'),
(568, '2024-01-12', '102', '2024-01-12 16:40:40'),
(569, '2024-01-12', '102', '2024-01-12 16:40:47'),
(570, '2024-01-12', '102', '2024-01-12 16:40:55'),
(571, '2024-01-12', '102', '2024-01-12 16:41:03'),
(572, '2024-01-12', '102', '2024-01-12 16:41:12'),
(573, '2024-01-12', '105', '2024-01-12 16:41:19'),
(574, '2024-01-12', '104', '2024-01-12 16:41:28'),
(575, '2024-01-12', '102', '2024-01-12 16:41:36'),
(576, '2024-01-12', '102', '2024-01-12 16:43:18'),
(577, '2024-01-12', '102', '2024-01-12 16:43:26'),
(578, '2024-01-12', '102', '2024-01-12 16:43:34'),
(579, '2024-01-12', '102', '2024-01-12 16:43:43'),
(580, '2024-01-12', '102', '2024-01-12 16:43:51'),
(581, '2024-01-12', '102', '2024-01-12 16:44:00'),
(582, '2024-01-12', '102', '2024-01-12 16:44:08'),
(583, '2024-01-12', '102', '2024-01-12 16:44:17'),
(584, '2024-01-12', '102', '2024-01-12 16:44:24'),
(585, '2024-01-12', '102', '2024-01-12 16:44:32'),
(586, '2024-01-12', '104', '2024-01-12 16:44:41'),
(587, '2024-01-12', '104', '2024-01-12 16:45:19');

-- --------------------------------------------------------

--
-- Table structure for table `img_dataset`
--

CREATE TABLE `img_dataset` (
  `img_id` int(11) NOT NULL,
  `img_person` varchar(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `img_dataset`
--

INSERT INTO `img_dataset` (`img_id`, `img_person`) VALUES
(1, '101'),
(2, '101'),
(3, '101'),
(4, '101'),
(5, '101'),
(6, '101'),
(7, '101'),
(8, '101'),
(9, '101'),
(10, '101'),
(11, '101'),
(12, '101'),
(13, '101'),
(14, '101'),
(15, '101'),
(16, '101'),
(17, '101'),
(18, '101'),
(19, '101'),
(20, '101'),
(21, '101'),
(22, '101'),
(23, '101'),
(24, '101'),
(25, '101'),
(26, '101'),
(27, '101'),
(28, '101'),
(29, '101'),
(30, '101'),
(31, '101'),
(32, '101'),
(33, '101'),
(34, '101'),
(35, '101'),
(36, '101'),
(37, '101'),
(38, '101'),
(39, '101'),
(40, '101'),
(41, '102'),
(42, '102'),
(43, '102'),
(44, '102'),
(45, '102'),
(46, '102'),
(47, '102'),
(48, '102'),
(49, '102'),
(50, '102'),
(51, '102'),
(52, '102'),
(53, '102'),
(54, '102'),
(55, '102'),
(56, '102'),
(57, '102'),
(58, '102'),
(59, '102'),
(60, '102'),
(61, '102'),
(62, '102'),
(63, '102'),
(64, '102'),
(65, '102'),
(66, '102'),
(67, '102'),
(68, '102'),
(69, '102'),
(70, '102'),
(71, '102'),
(72, '102'),
(73, '102'),
(74, '102'),
(75, '102'),
(76, '102'),
(77, '102'),
(78, '102'),
(79, '102'),
(80, '102'),
(81, '103'),
(82, '103'),
(83, '103'),
(84, '103'),
(85, '103'),
(86, '103'),
(87, '103'),
(88, '103'),
(89, '103'),
(90, '103'),
(91, '103'),
(92, '103'),
(93, '103'),
(94, '103'),
(95, '103'),
(96, '103'),
(97, '103'),
(98, '103'),
(99, '103'),
(100, '103'),
(101, '103'),
(102, '103'),
(103, '103'),
(104, '103'),
(105, '103'),
(106, '103'),
(107, '103'),
(108, '103'),
(109, '103'),
(110, '103'),
(111, '103'),
(112, '103'),
(113, '103'),
(114, '103'),
(115, '103'),
(116, '103'),
(117, '103'),
(118, '103'),
(119, '103'),
(120, '103'),
(121, '104'),
(122, '104'),
(123, '104'),
(124, '104'),
(125, '104'),
(126, '104'),
(127, '104'),
(128, '104'),
(129, '104'),
(130, '104'),
(131, '104'),
(132, '104'),
(133, '104'),
(134, '104'),
(135, '104'),
(136, '104'),
(137, '104'),
(138, '104'),
(139, '104'),
(140, '104'),
(141, '104'),
(142, '104'),
(143, '104'),
(144, '104'),
(145, '104'),
(146, '104'),
(147, '104'),
(148, '104'),
(149, '104'),
(150, '104'),
(151, '104'),
(152, '104'),
(153, '104'),
(154, '104'),
(155, '104'),
(156, '104'),
(157, '104'),
(158, '104'),
(159, '104'),
(160, '104'),
(161, '105'),
(162, '105'),
(163, '105'),
(164, '105'),
(165, '105'),
(166, '105'),
(167, '105'),
(168, '105'),
(169, '105'),
(170, '105'),
(171, '105'),
(172, '105'),
(173, '105'),
(174, '105'),
(175, '105'),
(176, '105'),
(177, '105'),
(178, '105'),
(179, '105'),
(180, '105'),
(181, '105'),
(182, '105'),
(183, '105'),
(184, '105'),
(185, '105'),
(186, '105'),
(187, '105'),
(188, '105'),
(189, '105'),
(190, '105'),
(191, '105'),
(192, '105'),
(193, '105'),
(194, '105'),
(195, '105'),
(196, '105'),
(197, '105'),
(198, '105'),
(199, '105'),
(200, '105');

-- --------------------------------------------------------

--
-- Table structure for table `std_mnst`
--

CREATE TABLE `std_mnst` (
  `std_nbr` varchar(9) NOT NULL,
  `std_name` varchar(50) NOT NULL,
  `std_active` varchar(1) NOT NULL DEFAULT 'Y',
  `std_lesson` varchar(200) NOT NULL,
  `std_added` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `std_mnst`
--

INSERT INTO `std_mnst` (`std_nbr`, `std_name`, `std_active`, `std_lesson`, `std_added`) VALUES
('101', 'mert', 'Y', 'HARDWARE', '2024-01-10 22:21:44'),
('102', 'ahmed asfour', 'Y', 'HARDWARE', '2024-01-10 22:22:20'),
('103', 'nf', 'Y', 'SOFTWARE', '2024-01-11 01:51:41'),
('104', 'kadir bey', 'Y', 'ELECTRICAL', '2024-01-12 00:26:22'),
('105', 'asf', 'Y', 'SOFTWARE', '2024-01-12 13:12:13');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `accs_hist`
--
ALTER TABLE `accs_hist`
  ADD PRIMARY KEY (`accs_id`),
  ADD KEY `accs_date` (`accs_date`);

--
-- Indexes for table `img_dataset`
--
ALTER TABLE `img_dataset`
  ADD PRIMARY KEY (`img_id`);

--
-- Indexes for table `std_mnst`
--
ALTER TABLE `std_mnst`
  ADD PRIMARY KEY (`std_nbr`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts`
--
ALTER TABLE `accounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `accs_hist`
--
ALTER TABLE `accs_hist`
  MODIFY `accs_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=588;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
