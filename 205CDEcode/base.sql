-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 10, 2019 at 11:33 PM
-- Server version: 5.7.25-0ubuntu0.18.04.2
-- PHP Version: 7.2.15-0ubuntu0.18.04.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `base`
--

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `id` int(100) DEFAULT NULL,
  `name` char(100) DEFAULT NULL,
  `price` char(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ordered`
--

CREATE TABLE `ordered` (
  `product_id` int(100) NOT NULL,
  `product` varchar(225) NOT NULL,
  `price` int(100) NOT NULL,
  `order_id` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `order_queue`
--

CREATE TABLE `order_queue` (
  `username` varchar(300) NOT NULL,
  `order_id` int(10) NOT NULL,
  `credit` int(100) NOT NULL,
  `pin` int(5) NOT NULL,
  `totalprice` int(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `id` int(100) NOT NULL,
  `name` varchar(300) DEFAULT NULL,
  `price` char(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`id`, `name`, `price`) VALUES
(1, 'Genuine Lining Badminton Sport T Shirt and Short', '300'),
(2, 'Badminton Sleeveless T shirts', '180'),
(3, 'Sport Dress with Safe Shorts', '320'),
(4, 'YONEX Aeroclub 03', '120'),
(5, 'Li Ning Champs Shuttlecock', '145'),
(6, 'Dunlop Evo Carbon Badminton Racket', '120'),
(7, 'Wilson Badminton Racket', '190'),
(8, 'YONEX Pro Racquet Bag', '250'),
(9, 'YONEX Team Racket Bag', '310'),
(10, 'YONEX Pro Stand Bag', '600');

-- --------------------------------------------------------

--
-- Table structure for table `signup`
--

CREATE TABLE `signup` (
  `usrname` char(30) DEFAULT NULL,
  `home` varchar(500) DEFAULT NULL,
  `email` char(100) DEFAULT NULL,
  `pwd` char(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `string`
--

CREATE TABLE `string` (
  `customer` varchar(100) DEFAULT NULL,
  `string` varchar(225) DEFAULT NULL,
  `date1` char(100) DEFAULT NULL,
  `time1` char(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `order_queue`
--
ALTER TABLE `order_queue`
  ADD UNIQUE KEY `order_id` (`order_id`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD UNIQUE KEY `id` (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `order_queue`
--
ALTER TABLE `order_queue`
  MODIFY `order_id` int(10) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
