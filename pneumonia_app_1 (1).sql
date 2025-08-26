-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1:3307
-- Thời gian đã tạo: Th8 26, 2025 lúc 08:59 PM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `pneumonia_app_1`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `activity_logs`
--

CREATE TABLE `activity_logs` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `action` varchar(255) NOT NULL,
  `details` text DEFAULT NULL,
  `ip_address` varchar(45) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `activity_logs`
--

INSERT INTO `activity_logs` (`id`, `user_id`, `action`, `details`, `ip_address`, `created_at`) VALUES
(1, 4, 'Chẩn đoán', 'File: NORMAL2-IM-1300-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 99.96%', NULL, '2025-08-21 17:23:23'),
(2, 3, 'Chẩn đoán', 'File: person151_virus_302.jpeg, KQ: Có bệnh, Độ tin cậy: 100.00%', NULL, '2025-08-22 04:21:09'),
(3, 3, 'Chẩn đoán', 'File: NORMAL2-IM-1345-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 100.00%', NULL, '2025-08-22 04:50:58'),
(4, 3, 'Chẩn đoán', 'File: NORMAL2-IM-1345-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 100.00%', NULL, '2025-08-22 04:51:53'),
(5, 3, 'Chẩn đoán', 'File: viemphoi.jpeg, KQ: Không bệnh, Độ tin cậy: 97.50%', NULL, '2025-08-22 04:51:55'),
(6, 3, 'Chẩn đoán', 'File: NORMAL2-IM-1345-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 100.00%', NULL, '2025-08-22 04:52:37'),
(7, 3, 'Chẩn đoán', 'File: viemphoi.jpeg, KQ: Không bệnh, Độ tin cậy: 97.50%', NULL, '2025-08-22 04:52:40'),
(8, 3, 'Chẩn đoán', 'File: viemphoii.jpg, KQ: Không bệnh, Độ tin cậy: 96.80%', NULL, '2025-08-22 04:52:42'),
(9, 3, 'Chẩn đoán', 'File: NORMAL2-IM-1345-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 100.00%', NULL, '2025-08-22 04:53:30'),
(10, 3, 'Chẩn đoán', 'File: viemphoi.jpeg, KQ: Không bệnh, Độ tin cậy: 97.50%', NULL, '2025-08-22 04:53:33'),
(11, 3, 'Chẩn đoán', 'File: viemphoii.jpg, KQ: Không bệnh, Độ tin cậy: 96.80%', NULL, '2025-08-22 04:53:36'),
(12, 3, 'Chẩn đoán', 'File: person9_bacteria_39.jpeg, KQ: Có bệnh, Độ tin cậy: 100.00%', NULL, '2025-08-22 04:53:36'),
(13, 4, 'Chẩn đoán', 'File: person9_bacteria_39.jpeg, KQ: Có bệnh, Độ tin cậy: 100.00%', NULL, '2025-08-22 04:57:24'),
(14, 4, 'Chẩn đoán', 'File: person896_bacteria_2821.jpeg, KQ: Có bệnh, Độ tin cậy: 100.00%', NULL, '2025-08-22 05:02:05'),
(15, 4, 'Chẩn đoán', 'File: person98_virus_182.jpeg, KQ: Có bệnh, Độ tin cậy: 100.00%', NULL, '2025-08-22 05:06:50'),
(16, 4, 'Chẩn đoán', 'File: person98_virus_182.jpeg, KQ: Có bệnh, Độ tin cậy: 100.00%', NULL, '2025-08-22 05:06:56'),
(17, 4, 'Chẩn đoán', 'File: person98_virus_182.jpeg, KQ: Có bệnh, Độ tin cậy: 100.00%', NULL, '2025-08-22 05:07:00'),
(18, 4, 'Chẩn đoán', 'File: person98_virus_182.jpeg, KQ: Có bệnh, Độ tin cậy: 100.00%', NULL, '2025-08-22 05:07:07'),
(19, 5, 'Chẩn đoán', 'File: NORMAL2-IM-1346-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 100.00%', NULL, '2025-08-22 05:17:05'),
(20, 4, 'Chẩn đoán', 'File: NORMAL2-IM-1349-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 99.93%', NULL, '2025-08-22 05:18:55'),
(21, 5, 'Chẩn đoán', 'File: NORMAL2-IM-1362-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 99.83%', NULL, '2025-08-22 05:20:12'),
(22, 5, 'Chẩn đoán', 'File: NORMAL2-IM-1333-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 99.44%', NULL, '2025-08-22 05:21:40'),
(23, 4, 'Chẩn đoán', 'File: NORMAL2-IM-1345-0001-0002.jpeg, KQ: Không bệnh, Độ tin cậy: 99.98%', NULL, '2025-08-22 05:23:06'),
(24, 5, 'Chẩn đoán', 'File: NORMAL2-IM-1333-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 99.44%', NULL, '2025-08-22 05:26:42'),
(25, 5, 'Chẩn đoán', 'File: NORMAL2-IM-1334-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 99.98%', NULL, '2025-08-22 05:28:13'),
(26, 5, 'Chẩn đoán', 'File: NORMAL2-IM-1334-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 99.98%', NULL, '2025-08-22 05:28:31'),
(27, 5, 'Chẩn đoán', 'File: NORMAL2-IM-1334-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 99.98%', NULL, '2025-08-22 05:28:33'),
(28, 5, 'Chẩn đoán', 'File: NORMAL2-IM-1334-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 99.98%', NULL, '2025-08-22 05:28:39'),
(29, 5, 'Chẩn đoán', 'File: NORMAL2-IM-1333-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 99.44%', NULL, '2025-08-22 05:31:10'),
(30, 5, 'Chẩn đoán', 'File: NORMAL2-IM-1356-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 91.21%', NULL, '2025-08-22 05:33:27'),
(31, 5, 'Chẩn đoán', 'File: NORMAL2-IM-1345-0001-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 99.93%', NULL, '2025-08-22 05:34:59'),
(32, 5, 'Chẩn đoán', 'File: NORMAL2-IM-1345-0001-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 99.93%', NULL, '2025-08-22 05:35:17'),
(33, 5, 'Chẩn đoán', 'File: NORMAL2-IM-1345-0001-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 99.93%', NULL, '2025-08-22 05:35:23'),
(34, 5, 'Chẩn đoán', 'File: NORMAL2-IM-1345-0001-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 99.93%', NULL, '2025-08-22 05:35:44'),
(35, 5, 'Chẩn đoán', 'File: NORMAL2-IM-1345-0001-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 99.93%', NULL, '2025-08-22 05:36:09'),
(36, 5, 'Chẩn đoán', 'File: NORMAL2-IM-1334-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 99.98%', NULL, '2025-08-22 05:37:06'),
(37, 5, 'Chẩn đoán', 'File: NORMAL2-IM-1376-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 97.34%', NULL, '2025-08-22 05:39:09'),
(38, 5, 'Chẩn đoán', 'File: NORMAL2-IM-1376-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 97.34%', NULL, '2025-08-22 05:39:18'),
(39, 5, 'Chẩn đoán', 'File: NORMAL2-IM-1376-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 97.34%', NULL, '2025-08-22 05:39:21'),
(40, 4, 'Chẩn đoán', 'File: NORMAL2-IM-1334-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 99.98%', NULL, '2025-08-22 05:40:18'),
(191, 3, 'Chẩn đoán', 'File: person8_bacteria_37.jpeg, KQ: Không bệnh, Độ tin cậy: 72.47%, Thuật toán: YOLO11', NULL, '2025-08-24 16:57:32'),
(192, 4, 'Chẩn đoán', 'File: person9_bacteria_38.jpeg, KQ: Có bệnh, Độ tin cậy: 100.00%, Thuật toán: YOLO11', NULL, '2025-08-24 17:02:00'),
(193, 3, 'Chẩn đoán', 'File: person9_bacteria_38.jpeg, KQ: Có bệnh, Độ tin cậy: 100.00%, Thuật toán: YOLO11', NULL, '2025-08-24 17:03:29'),
(194, 3, 'Chẩn đoán', 'File: person9_bacteria_38.jpeg, KQ: Có bệnh, Độ tin cậy: 100.00%, Thuật toán: YOLO11', NULL, '2025-08-24 17:05:09'),
(195, 3, 'Chẩn đoán', 'File: NORMAL2-IM-1332-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 100.00%, Thuật toán: YOLO11', NULL, '2025-08-24 17:05:10'),
(196, 3, 'Chẩn đoán', 'File: NORMAL2-IM-1326-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 99.79%, Thuật toán: YOLO11', NULL, '2025-08-24 17:05:39'),
(197, 3, 'Chẩn đoán', 'File: NORMAL2-IM-1326-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 99.79%, Thuật toán: YOLO11', NULL, '2025-08-24 17:06:38'),
(198, 3, 'Chẩn đoán', 'File: person9_bacteria_40.jpeg, KQ: Có bệnh, Độ tin cậy: 100.00%, Thuật toán: YOLO11', NULL, '2025-08-24 17:06:40'),
(199, 3, 'Chẩn đoán', 'File: NORMAL2-IM-1326-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 99.79%, Thuật toán: YOLO11', NULL, '2025-08-24 17:07:40'),
(200, 3, 'Chẩn đoán', 'File: person9_bacteria_40.jpeg, KQ: Có bệnh, Độ tin cậy: 100.00%, Thuật toán: YOLO11', NULL, '2025-08-24 17:07:41'),
(201, 3, 'Chẩn đoán', 'File: NORMAL2-IM-1279-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 99.94%, Thuật toán: YOLO11', NULL, '2025-08-24 17:10:10'),
(202, 3, 'Chẩn đoán', 'File: NORMAL2-IM-1279-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 99.94%, Thuật toán: YOLO11', NULL, '2025-08-24 17:10:47'),
(203, 3, 'Chẩn đoán', 'File: person92_virus_174.jpeg, KQ: Có bệnh, Độ tin cậy: 100.00%, Thuật toán: YOLO11', NULL, '2025-08-24 17:10:49'),
(204, 3, 'Chẩn đoán', 'File: NORMAL2-IM-1279-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 71.50%, Thuật toán: RF-MobileNet', NULL, '2025-08-24 17:11:36'),
(205, 3, 'Chẩn đoán', 'File: person92_virus_174.jpeg, KQ: Có bệnh, Độ tin cậy: 79.83%, Thuật toán: RF-MobileNet', NULL, '2025-08-24 17:11:38'),
(206, 3, 'Chẩn đoán', 'File: NORMAL2-IM-1279-0001.jpeg, KQ: Không bệnh, Độ tin cậy: 71.50%, Thuật toán: RF-MobileNet', NULL, '2025-08-24 17:12:56'),
(207, 3, 'Chẩn đoán', 'File: person92_virus_174.jpeg, KQ: Có bệnh, Độ tin cậy: 79.83%, Thuật toán: RF-MobileNet', NULL, '2025-08-24 17:12:58'),
(208, 3, 'Chẩn đoán', 'File: x-quang-tay.jpg, KQ: Không xác định, Độ tin cậy: 86.83%, Thuật toán: RF-MobileNet', NULL, '2025-08-24 17:13:02'),
(209, 3, 'LOCK_USER', 'Khóa tài khoản: tien', 'admin', '2025-08-25 09:47:53'),
(210, 3, 'LOCK_USER', 'Khóa tài khoản: teone', 'admin', '2025-08-25 09:48:48'),
(211, 3, 'UNLOCK_USER', 'Mở khóa tài khoản: teone', 'admin', '2025-08-25 09:48:59'),
(212, 3, 'DELETE_USER', 'Đã xóa tài khoản: minhanh - None', 'admin', '2025-08-25 09:49:16'),
(213, 3, 'LOCK_USER', 'Khóa tài khoản: user1', 'admin', '2025-08-25 09:58:39'),
(214, 3, 'UNLOCK_USER', 'Mở khóa tài khoản: user1', 'admin', '2025-08-25 09:58:49'),
(215, 3, 'UNLOCK_USER', 'Mở khóa tài khoản: tien', 'admin', '2025-08-25 10:07:04'),
(216, 3, 'LOCK_USER', 'Khóa tài khoản: tien', 'admin', '2025-08-25 10:10:14'),
(217, 3, 'UNLOCK_USER', 'Mở khóa tài khoản: tien', 'admin', '2025-08-25 10:10:17'),
(218, 3, 'LOCK_USER', 'Khóa tài khoản: teone', 'admin', '2025-08-25 11:13:02'),
(219, 3, 'UNLOCK_USER', 'Mở khóa tài khoản: teone', 'admin', '2025-08-25 11:27:39'),
(220, 3, 'LOCK_USER', 'Khóa tài khoản: teone', 'admin', '2025-08-25 11:28:59'),
(221, 3, 'UNLOCK_USER', 'Mở khóa tài khoản: teone', 'admin', '2025-08-25 11:30:00'),
(222, 4, 'Chẩn đoán', 'File: x-quang-tay.jpg, KQ: Không phải X-ray phổi, Độ tin cậy: 99.47%, Thuật toán: YOLO11', NULL, '2025-08-26 12:25:07'),
(223, 4, 'Chẩn đoán', 'File: x-quang-tay.jpg, KQ: Không xác định, Độ tin cậy: 86.83%, Thuật toán: RF-MobileNet', NULL, '2025-08-26 12:25:36'),
(224, 4, 'Chẩn đoán', 'File: x-quang-tay.jpg, KQ: Không xác định, Độ tin cậy: 86.83%, Thuật toán: RF-MobileNet', NULL, '2025-08-26 12:26:09'),
(225, 4, 'Chẩn đoán', 'File: person9_bacteria_40.jpeg, KQ: Có bệnh, Độ tin cậy: 81.67%, Thuật toán: RF-MobileNet', NULL, '2025-08-26 12:26:10'),
(226, 4, 'Chẩn đoán', 'File: x-quang-tay.jpg, KQ: Không phải X-ray phổi, Độ tin cậy: 99.47%, Thuật toán: YOLO11', NULL, '2025-08-26 12:26:21'),
(227, 4, 'Chẩn đoán', 'File: person9_bacteria_40.jpeg, KQ: Có bệnh, Độ tin cậy: 100.00%, Thuật toán: YOLO11', NULL, '2025-08-26 12:26:22'),
(228, 3, 'LOCK_USER', 'Khóa tài khoản: tien', 'admin', '2025-08-26 13:58:54'),
(229, 3, 'UNLOCK_USER', 'Mở khóa tài khoản: tien', 'admin', '2025-08-26 13:58:58'),
(230, 3, 'LOCK_USER', 'Khóa tài khoản: tien', 'admin', '2025-08-26 13:59:00'),
(231, 3, 'UNLOCK_USER', 'Mở khóa tài khoản: tien', 'admin', '2025-08-26 13:59:03'),
(232, 3, 'LOCK_USER', 'Khóa tài khoản: tien', 'admin', '2025-08-26 13:59:04'),
(233, 3, 'UNLOCK_USER', 'Mở khóa tài khoản: tien', 'admin', '2025-08-26 13:59:07'),
(234, 3, 'LOCK_USER', 'Khóa tài khoản: tien', 'admin', '2025-08-26 13:59:08'),
(235, 3, 'UNLOCK_USER', 'Mở khóa tài khoản: tien', 'admin', '2025-08-26 13:59:11'),
(236, 3, 'LOCK_USER', 'Khóa tài khoản: tien', 'admin', '2025-08-26 13:59:14'),
(237, 3, 'UNLOCK_USER', 'Mở khóa tài khoản: tien', 'admin', '2025-08-26 13:59:16'),
(238, 3, 'LOCK_USER', 'Khóa tài khoản: tien', 'admin', '2025-08-26 13:59:18'),
(239, 3, 'UNLOCK_USER', 'Mở khóa tài khoản: tien', 'admin', '2025-08-26 13:59:21'),
(240, 3, 'RESET_PASSWORD', 'Reset password cho: tien', 'admin', '2025-08-26 14:00:10'),
(241, 3, 'RESET_PASSWORD', 'Reset password cho: tien', 'admin', '2025-08-26 14:00:12'),
(242, 3, 'LOCK_USER', 'Khóa tài khoản: tien', 'admin', '2025-08-26 14:00:24'),
(243, 3, 'UNLOCK_USER', 'Mở khóa tài khoản: tien', 'admin', '2025-08-26 14:00:28'),
(244, 3, 'LOCK_USER', 'Khóa tài khoản: tien', 'admin', '2025-08-26 14:00:31'),
(245, 3, 'UNLOCK_USER', 'Mở khóa tài khoản: tien', 'admin', '2025-08-26 14:02:00'),
(246, 3, 'LOCK_USER', 'Khóa tài khoản: tien', 'admin', '2025-08-26 14:02:03'),
(247, 3, 'UNLOCK_USER', 'Mở khóa tài khoản: tien', 'admin', '2025-08-26 14:02:04'),
(248, 3, 'LOCK_USER', 'Khóa tài khoản: tien', 'admin', '2025-08-26 14:02:07'),
(249, 3, 'UNLOCK_USER', 'Mở khóa tài khoản: tien', 'admin', '2025-08-26 14:02:08'),
(250, 3, 'LOCK_USER', 'Khóa tài khoản: tien', 'admin', '2025-08-26 14:02:11'),
(251, 3, 'UNLOCK_USER', 'Mở khóa tài khoản: tien', 'admin', '2025-08-26 14:02:13'),
(252, 3, 'LOCK_USER', 'Khóa tài khoản: tien', 'admin', '2025-08-26 14:02:16'),
(253, 3, 'UNLOCK_USER', 'Mở khóa tài khoản: tien', 'admin', '2025-08-26 14:02:17'),
(254, 3, 'RESET_PASSWORD', 'Reset password cho: tien', 'admin', '2025-08-26 14:02:48'),
(255, 3, 'DELETE_USER', 'Đã xóa tài khoản: user1 - user1@example.com', 'admin', '2025-08-26 14:04:13'),
(256, 8, 'Chẩn đoán', 'File: person8_bacteria_37.jpeg, KQ: Không bệnh, Độ tin cậy: 72.47%, Thuật toán: YOLO11', NULL, '2025-08-26 14:21:26');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `admin_replies`
--

CREATE TABLE `admin_replies` (
  `id` int(11) NOT NULL,
  `feedback_id` int(11) NOT NULL,
  `admin_id` int(11) NOT NULL,
  `admin_name` varchar(50) NOT NULL,
  `reply` text NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `feedbacks`
--

CREATE TABLE `feedbacks` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `rating` int(11) DEFAULT NULL CHECK (`rating` between 1 and 5),
  `comment` text DEFAULT NULL,
  `phan_hoi_admin` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `feedbacks`
--

INSERT INTO `feedbacks` (`id`, `user_id`, `username`, `rating`, `comment`, `phan_hoi_admin`, `created_at`, `updated_at`) VALUES
(7, 4, 'teone', 5, 'Ứng dụng rất tốt', NULL, '2025-08-24 15:01:36', '2025-08-24 16:22:41'),
(8, 4, 'teone', 5, 'tốt', NULL, '2025-08-24 16:05:50', '2025-08-24 16:05:50'),
(9, 4, 'teone', 4, 'ok nha', NULL, '2025-08-26 14:32:37', '2025-08-26 14:32:37');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `lich_su_chan_doan`
--

CREATE TABLE `lich_su_chan_doan` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `filename` varchar(255) DEFAULT NULL,
  `result` varchar(255) DEFAULT NULL,
  `algorithm` varchar(50) DEFAULT 'YOLO11',
  `confidence` float DEFAULT 0,
  `severity` varchar(50) DEFAULT NULL,
  `recommendation` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `lich_su_chan_doan`
--

INSERT INTO `lich_su_chan_doan` (`id`, `user_id`, `username`, `filename`, `result`, `algorithm`, `confidence`, `severity`, `recommendation`, `created_at`) VALUES
(1, 4, 'teone', 'NORMAL2-IM-1332-0001.jpeg', 'Không bệnh', 'YOLO11', 0.999991, 'Trung bình', 'Cần xét nghiệm thêm để xác định', '2025-08-21 13:41:09'),
(2, 4, 'teone', 'NORMAL2-IM-1335-0001.jpeg', 'Không bệnh', 'YOLO11', 0.999993, 'Trung bình', 'Cần xét nghiệm thêm để xác định', '2025-05-21 13:41:51'),
(3, 4, 'teone', 'person88_virus_164.jpeg', 'Có bệnh', 'YOLO11', 0.99997, 'Nặng', 'Cần xét nghiệm thêm để xác định', '2025-08-21 13:44:03'),
(4, 4, 'teone', 'person9_bacteria_41.jpeg', 'Có bệnh', 'YOLO11', 0.999997, 'Nặng', 'Cần xét nghiệm thêm', '2025-06-21 14:03:34'),
(5, 4, 'teone', 'person9_bacteria_40.jpeg', 'Có bệnh', 'YOLO11', 100, 'Nặng', 'Cần nhập viện ngay để điều trị khẩn cấp', '2025-08-21 16:01:28'),
(6, 4, 'teone', 'NORMAL2-IM-1334-0001.jpeg', 'Không bệnh', 'YOLO11', 99.983, 'Không phát hiện', 'Tiếp tục duy trì lối sống lành mạnh, kiểm tra sức khỏe định kỳ', '2025-08-21 16:05:38'),
(7, 4, 'teone', '112.jpg', 'Có bệnh', 'YOLO11', 68.9503, 'Trung bình', 'Nên đi khám bác sĩ để được kiểm tra chi tiết', '2025-07-21 16:32:56'),
(8, 5, 'tien', '1902.jpg', 'Có bệnh', 'YOLO11', 62.7619, 'Trung bình', 'Nên đi khám bác sĩ để được kiểm tra chi tiết', '2025-08-21 16:38:55'),
(9, 5, 'tien', '1902.jpg', 'Có bệnh', 'YOLO11', 62.7619, 'Trung bình', 'Nên đi khám bác sĩ để được kiểm tra chi tiết', '2025-08-21 16:40:57'),
(10, 4, 'teone', 'NORMAL2-IM-1347-0001.jpeg', 'Không bệnh', 'YOLO11', 99.9969, 'Không phát hiện', 'Tiếp tục duy trì lối sống lành mạnh, kiểm tra sức khỏe định kỳ', '2025-06-21 16:57:31'),
(11, 3, 'admin', 'NORMAL2-IM-1335-0001.jpeg', 'Không bệnh', 'YOLO11', 99.9993, 'Không phát hiện', 'Tiếp tục duy trì lối sống lành mạnh, kiểm tra sức khỏe định kỳ', '2025-08-21 17:14:11'),
(12, 4, 'teone', 'NORMAL2-IM-1350-0001.jpeg', 'Không bệnh', 'YOLO11', 99.999, 'Không phát hiện', 'Tiếp tục duy trì lối sống lành mạnh, kiểm tra sức khỏe định kỳ', '2025-08-21 17:16:00'),
(13, 4, 'teone', 'NORMAL2-IM-1300-0001.jpeg', 'Không bệnh', 'YOLO11', 99.9629, 'Không phát hiện', 'Tiếp tục duy trì lối sống lành mạnh, kiểm tra sức khỏe định kỳ', '2025-08-21 17:23:23'),
(14, 3, 'admin', 'person151_virus_302.jpeg', 'Có bệnh', 'YOLO11', 99.9997, 'Nặng', 'Cần nhập viện ngay để điều trị khẩn cấp', '2025-08-22 04:21:09'),
(15, 3, 'admin', 'NORMAL2-IM-1345-0001.jpeg', 'Không bệnh', 'YOLO11', 100, 'Không phát hiện', 'Tiếp tục duy trì lối sống lành mạnh, kiểm tra sức khỏe định kỳ', '2025-08-22 04:50:58'),
(16, 3, 'admin', 'NORMAL2-IM-1345-0001.jpeg', 'Không bệnh', 'YOLO11', 100, 'Không phát hiện', 'Tiếp tục duy trì lối sống lành mạnh, kiểm tra sức khỏe định kỳ', '2025-08-22 04:51:53'),
(17, 3, 'admin', 'viemphoi.jpeg', 'Không bệnh', 'YOLO11', 97.5037, 'Không phát hiện', 'Tiếp tục duy trì lối sống lành mạnh, kiểm tra sức khỏe định kỳ', '2025-08-22 04:51:55'),
(18, 3, 'admin', 'NORMAL2-IM-1345-0001.jpeg', 'Không bệnh', 'YOLO11', 100, 'Không phát hiện', 'Tiếp tục duy trì lối sống lành mạnh, kiểm tra sức khỏe định kỳ', '2025-08-22 04:52:37'),
(19, 3, 'admin', 'viemphoi.jpeg', 'Không bệnh', 'YOLO11', 97.5037, 'Không phát hiện', 'Tiếp tục duy trì lối sống lành mạnh, kiểm tra sức khỏe định kỳ', '2025-08-22 04:52:40'),
(20, 3, 'admin', 'viemphoii.jpg', 'Không bệnh', 'YOLO11', 96.8036, 'Không phát hiện', 'Tiếp tục duy trì lối sống lành mạnh, kiểm tra sức khỏe định kỳ', '2025-08-22 04:52:42'),
(21, 3, 'admin', 'NORMAL2-IM-1345-0001.jpeg', 'Không bệnh', 'YOLO11', 100, 'Không phát hiện', 'Tiếp tục duy trì lối sống lành mạnh, kiểm tra sức khỏe định kỳ', '2025-08-22 04:53:30'),
(22, 3, 'admin', 'viemphoi.jpeg', 'Không bệnh', 'YOLO11', 97.5037, 'Không phát hiện', 'Tiếp tục duy trì lối sống lành mạnh, kiểm tra sức khỏe định kỳ', '2025-08-22 04:53:33'),
(23, 3, 'admin', 'viemphoii.jpg', 'Không bệnh', 'YOLO11', 96.8036, 'Không phát hiện', 'Tiếp tục duy trì lối sống lành mạnh, kiểm tra sức khỏe định kỳ', '2025-08-22 04:53:35'),
(24, 3, 'admin', 'person9_bacteria_39.jpeg', 'Có bệnh', 'YOLO11', 100, 'Nặng', 'Cần nhập viện ngay để điều trị khẩn cấp', '2025-08-22 04:53:36'),
(25, 4, 'teone', 'person9_bacteria_39.jpeg', 'Có bệnh', 'YOLO11', 100, 'Nặng', 'Cần nhập viện ngay để điều trị khẩn cấp', '2025-08-22 04:57:24'),
(26, 4, 'teone', 'person896_bacteria_2821.jpeg', 'Có bệnh', 'YOLO11', 100, 'Nặng', 'Cần nhập viện ngay để điều trị khẩn cấp', '2025-08-22 05:02:05'),
(27, 4, 'teone', 'person98_virus_182.jpeg', 'Có bệnh', 'YOLO11', 100, 'Nặng', 'Cần nhập viện ngay để điều trị khẩn cấp', '2025-08-22 05:06:50'),
(28, 4, 'teone', 'person98_virus_182.jpeg', 'Có bệnh', 'YOLO11', 100, 'Nặng', 'Cần nhập viện ngay để điều trị khẩn cấp', '2025-08-22 05:06:56'),
(29, 4, 'teone', 'person98_virus_182.jpeg', 'Có bệnh', 'YOLO11', 100, 'Nặng', 'Cần nhập viện ngay để điều trị khẩn cấp', '2025-07-22 05:07:00'),
(30, 4, 'teone', 'person98_virus_182.jpeg', 'Có bệnh', 'YOLO11', 100, 'Nặng', 'Cần nhập viện ngay để điều trị khẩn cấp', '2025-08-22 05:07:07'),
(31, 5, 'tien', 'NORMAL2-IM-1346-0001.jpeg', 'Không bệnh', 'YOLO11', 100, 'Không phát hiện', 'Tiếp tục duy trì lối sống lành mạnh, kiểm tra sức khỏe định kỳ', '2025-06-22 05:17:05'),
(32, 4, 'teone', 'NORMAL2-IM-1349-0001.jpeg', 'Không bệnh', 'YOLO11', 99.9287, 'Không phát hiện', 'Tiếp tục duy trì lối sống lành mạnh, kiểm tra sức khỏe định kỳ', '2025-06-22 05:18:55'),
(33, 5, 'tien', 'NORMAL2-IM-1362-0001.jpeg', 'Không bệnh', 'YOLO11', 99.8285, 'Không phát hiện', 'Tiếp tục duy trì lối sống lành mạnh, kiểm tra sức khỏe định kỳ', '2025-08-22 05:20:12'),
(34, 5, 'tien', 'NORMAL2-IM-1333-0001.jpeg', 'Không bệnh', 'YOLO11', 99.4399, 'Không phát hiện', 'Tiếp tục duy trì lối sống lành mạnh, kiểm tra sức khỏe định kỳ', '2025-08-22 05:21:40'),
(35, 4, 'teone', 'NORMAL2-IM-1345-0001-0002.jpeg', 'Không bệnh', 'YOLO11', 99.9757, 'Không phát hiện', 'Tiếp tục duy trì lối sống lành mạnh, kiểm tra sức khỏe định kỳ', '2025-07-22 05:23:06'),
(36, 5, 'tien', 'NORMAL2-IM-1333-0001.jpeg', 'Không bệnh', 'YOLO11', 99.4399, 'Không phát hiện', 'Tiếp tục duy trì lối sống lành mạnh, kiểm tra sức khỏe định kỳ', '2025-08-22 05:26:42'),
(37, 5, 'tien', 'NORMAL2-IM-1334-0001.jpeg', 'Không bệnh', 'YOLO11', 99.983, 'Không phát hiện', 'Tiếp tục duy trì lối sống lành mạnh, kiểm tra sức khỏe định kỳ', '2025-07-22 05:28:13'),
(38, 5, 'tien', 'NORMAL2-IM-1334-0001.jpeg', 'Không bệnh', 'YOLO11', 99.983, 'Không phát hiện', 'Tiếp tục duy trì lối sống lành mạnh, kiểm tra sức khỏe định kỳ', '2025-06-22 05:28:31'),
(39, 5, 'tien', 'NORMAL2-IM-1334-0001.jpeg', 'Không bệnh', 'YOLO11', 99.983, 'Không phát hiện', 'Tiếp tục duy trì lối sống lành mạnh, kiểm tra sức khỏe định kỳ', '2025-08-22 05:28:33'),
(40, 5, 'tien', 'NORMAL2-IM-1334-0001.jpeg', 'Không bệnh', 'YOLO11', 99.983, 'Không phát hiện', 'Tiếp tục duy trì lối sống lành mạnh, kiểm tra sức khỏe định kỳ', '2025-08-22 05:28:39'),
(203, 3, 'admin', 'person8_bacteria_37.jpeg', 'Không bệnh', 'YOLO11', 72.4665, 'Không phát hiện bệnh', 'Tiếp tục duy trì lối sống lành mạnh', '2025-08-24 16:57:32'),
(204, 4, 'teone', 'person9_bacteria_38.jpeg', 'Có bệnh', 'YOLO11', 100, 'Nặng', 'Cần nhập viện ngay để điều trị khẩn cấp', '2025-08-24 17:02:00'),
(205, 3, 'admin', 'person9_bacteria_38.jpeg', 'Có bệnh', 'YOLO11', 100, 'Nặng', 'Cần nhập viện ngay để điều trị khẩn cấp', '2025-08-24 17:03:29'),
(206, 3, 'admin', 'person9_bacteria_38.jpeg', 'Có bệnh', 'YOLO11', 100, 'Nặng', 'Cần nhập viện ngay để điều trị khẩn cấp', '2025-08-24 17:05:09'),
(207, 3, 'admin', 'NORMAL2-IM-1332-0001.jpeg', 'Không bệnh', 'YOLO11', 99.9991, 'Không phát hiện bệnh', 'Tiếp tục duy trì lối sống lành mạnh', '2025-08-24 17:05:10'),
(208, 3, 'admin', 'NORMAL2-IM-1326-0001.jpeg', 'Không bệnh', 'YOLO11', 99.7923, 'Không phát hiện bệnh', 'Tiếp tục duy trì lối sống lành mạnh', '2025-08-24 17:05:39'),
(209, 3, 'admin', 'NORMAL2-IM-1326-0001.jpeg', 'Không bệnh', 'YOLO11', 99.7923, 'Không phát hiện bệnh', 'Tiếp tục duy trì lối sống lành mạnh', '2025-08-24 17:06:38'),
(210, 3, 'admin', 'person9_bacteria_40.jpeg', 'Có bệnh', 'YOLO11', 100, 'Nặng', 'Cần nhập viện ngay để điều trị khẩn cấp', '2025-08-24 17:06:40'),
(211, 3, 'admin', 'NORMAL2-IM-1326-0001.jpeg', 'Không bệnh', 'YOLO11', 99.7923, 'Không phát hiện bệnh', 'Tiếp tục duy trì lối sống lành mạnh', '2025-08-24 17:07:40'),
(212, 3, 'admin', 'person9_bacteria_40.jpeg', 'Có bệnh', 'YOLO11', 100, 'Nặng', 'Cần nhập viện ngay để điều trị khẩn cấp', '2025-08-24 17:07:41'),
(213, 3, 'admin', 'NORMAL2-IM-1279-0001.jpeg', 'Không bệnh', 'YOLO11', 99.9421, 'Không phát hiện bệnh', 'Tiếp tục duy trì lối sống lành mạnh', '2025-08-24 17:10:10'),
(214, 3, 'admin', 'NORMAL2-IM-1279-0001.jpeg', 'Không bệnh', 'YOLO11', 99.9421, 'Không phát hiện bệnh', 'Tiếp tục duy trì lối sống lành mạnh', '2025-08-24 17:10:47'),
(215, 3, 'admin', 'person92_virus_174.jpeg', 'Có bệnh', 'YOLO11', 100, 'Nặng', 'Cần nhập viện ngay để điều trị khẩn cấp', '2025-08-24 17:10:49'),
(216, 3, 'admin', 'NORMAL2-IM-1279-0001.jpeg', 'Không bệnh', 'RF-MobileNet', 71.5, 'Không phát hiện bệnh', 'Tiếp tục duy trì lối sống lành mạnh', '2025-08-24 17:11:35'),
(217, 3, 'admin', 'person92_virus_174.jpeg', 'Có bệnh', 'RF-MobileNet', 79.8333, 'Trung bình', 'Nên đi khám bác sĩ để được kiểm tra chi tiết', '2025-08-24 17:11:38'),
(218, 3, 'admin', 'NORMAL2-IM-1279-0001.jpeg', 'Không bệnh', 'RF-MobileNet', 71.5, 'Không phát hiện bệnh', 'Tiếp tục duy trì lối sống lành mạnh', '2025-08-24 17:12:56'),
(219, 3, 'admin', 'person92_virus_174.jpeg', 'Có bệnh', 'RF-MobileNet', 79.8333, 'Trung bình', 'Nên đi khám bác sĩ để được kiểm tra chi tiết', '2025-08-24 17:12:58'),
(220, 3, 'admin', 'x-quang-tay.jpg', 'Không xác định', 'RF-MobileNet', 86.8333, 'Không xác định', 'Cần làm thêm xét nghiệm hoặc chụp lại ảnh X-quang', '2025-08-24 17:13:02'),
(221, 4, 'teone', 'x-quang-tay.jpg', 'Không phải X-ray phổi', 'YOLO11', 99.4684, 'Không xác định', 'Cần làm thêm xét nghiệm hoặc chụp lại ảnh X-quang', '2025-08-26 12:25:07'),
(222, 4, 'teone', 'x-quang-tay.jpg', 'Không xác định', 'RF-MobileNet', 86.8333, 'Không xác định', 'Cần làm thêm xét nghiệm hoặc chụp lại ảnh X-quang', '2025-08-26 12:25:36'),
(223, 4, 'teone', 'x-quang-tay.jpg', 'Không xác định', 'RF-MobileNet', 86.8333, 'Không xác định', 'Cần làm thêm xét nghiệm hoặc chụp lại ảnh X-quang', '2025-08-26 12:26:09'),
(224, 4, 'teone', 'person9_bacteria_40.jpeg', 'Có bệnh', 'RF-MobileNet', 81.6667, 'Nặng', 'Cần nhập viện ngay để điều trị khẩn cấp', '2025-08-26 12:26:10'),
(225, 4, 'teone', 'x-quang-tay.jpg', 'Không phải X-ray phổi', 'YOLO11', 99.4684, 'Không xác định', 'Cần làm thêm xét nghiệm hoặc chụp lại ảnh X-quang', '2025-08-26 12:26:21'),
(226, 4, 'teone', 'person9_bacteria_40.jpeg', 'Có bệnh', 'YOLO11', 100, 'Nặng', 'Cần nhập viện ngay để điều trị khẩn cấp', '2025-08-26 12:26:22'),
(227, 8, 'myanh', 'person8_bacteria_37.jpeg', 'Không bệnh', 'YOLO11', 72.4665, 'Không phát hiện bệnh', 'Tiếp tục duy trì lối sống lành mạnh', '2025-08-26 14:21:26');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `full_name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `avatar` varchar(255) DEFAULT NULL,
  `role` enum('admin','user') NOT NULL DEFAULT 'user',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `status` enum('active','locked') NOT NULL DEFAULT 'active'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `full_name`, `email`, `phone`, `address`, `avatar`, `role`, `created_at`, `status`) VALUES
(2, 'user2', '123456', 'Trần Thị Bình', 'user2@example.com', NULL, NULL, '4444.jpg', 'user', '2025-08-21 13:39:21', 'active'),
(3, 'admin', 'scrypt:32768:8:1$UsN2UTs4sIZ4J67F$777d5a624de12d58b0b79883662f3e34c014313db90a154fd4cd9f82f336728bba45b634486ce0c161ae006abbb8544dc85daa0de2a9d301f910248b52650373', 'Quản trị viên', 'admin@example.com', NULL, NULL, '4444.jpg', 'admin', '2025-08-21 13:40:34', 'active'),
(4, 'teone', 'scrypt:32768:8:1$DR6PiPCSxvWE3PlJ$c76ce9e3e31d859a363c7a4bd71f5c6398be55e944384ad945236ceb41efa0e44c27f4322f3d48b0f2171ea0a85232bef6556d66cb2bcd676b14946a5e43b958', 'Tèo Em là tôi', 'teo@gmail.com', '0321456987', 'Cao Lãnh', '1112.jpg', 'user', '2025-08-21 13:40:59', 'active'),
(5, 'tien', '56d37b1dea780e1c6a6d77c117c96e6e2a4a5693aaa4258e94aabb39d5c6b2c8', NULL, NULL, NULL, NULL, NULL, 'user', '2025-08-21 16:35:42', 'active'),
(8, 'myanh', 'scrypt:32768:8:1$vSRM64XocF4cegqL$0f68b0a3b756f0f9686c3df92c67666d966dfaad366f636a7c43edcd6d26d8b0591aebc68d9dc85bcd715b44bf01625404d1e6f0aea5f5524ab09e83697f13d9', NULL, NULL, NULL, NULL, NULL, 'user', '2025-08-26 14:18:56', 'active');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `activity_logs`
--
ALTER TABLE `activity_logs`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Chỉ mục cho bảng `admin_replies`
--
ALTER TABLE `admin_replies`
  ADD PRIMARY KEY (`id`),
  ADD KEY `feedback_id` (`feedback_id`),
  ADD KEY `admin_id` (`admin_id`);

--
-- Chỉ mục cho bảng `feedbacks`
--
ALTER TABLE `feedbacks`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Chỉ mục cho bảng `lich_su_chan_doan`
--
ALTER TABLE `lich_su_chan_doan`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Chỉ mục cho bảng `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `username_2` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `activity_logs`
--
ALTER TABLE `activity_logs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=257;

--
-- AUTO_INCREMENT cho bảng `admin_replies`
--
ALTER TABLE `admin_replies`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT cho bảng `feedbacks`
--
ALTER TABLE `feedbacks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT cho bảng `lich_su_chan_doan`
--
ALTER TABLE `lich_su_chan_doan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=228;

--
-- AUTO_INCREMENT cho bảng `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `activity_logs`
--
ALTER TABLE `activity_logs`
  ADD CONSTRAINT `activity_logs_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL;

--
-- Các ràng buộc cho bảng `admin_replies`
--
ALTER TABLE `admin_replies`
  ADD CONSTRAINT `admin_replies_ibfk_1` FOREIGN KEY (`feedback_id`) REFERENCES `feedbacks` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `admin_replies_ibfk_2` FOREIGN KEY (`admin_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Các ràng buộc cho bảng `feedbacks`
--
ALTER TABLE `feedbacks`
  ADD CONSTRAINT `feedbacks_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Các ràng buộc cho bảng `lich_su_chan_doan`
--
ALTER TABLE `lich_su_chan_doan`
  ADD CONSTRAINT `lich_su_chan_doan_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
