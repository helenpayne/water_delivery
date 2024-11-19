/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 90100
 Source Host           : localhost:3306
 Source Schema         : water_delivery

 Target Server Type    : MySQL
 Target Server Version : 90100
 File Encoding         : 65001

 Date: 20/11/2024 01:10:21
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '自增ID',
  `wechat_openid` varchar(191) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '微信openid',
  `nickname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '昵称',
  `avatar_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '头像URL',
  `phone_number` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '电话号码',
  `level` int NOT NULL COMMENT '等级',
  `balance` float NOT NULL COMMENT '余额',
  `deposit` float NOT NULL COMMENT '押金',
  `points` int NOT NULL COMMENT '积分',
  `is_new_user` tinyint(1) NOT NULL COMMENT '是否新用户',
  `created_at` datetime NOT NULL DEFAULT 'now()' COMMENT '创建时间',
  `registered_ip` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '注册IP',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `wechat_openid`(`wechat_openid` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (1, 'string', 'string', 'string', 'string', 0, 0, 0, 0, 1, '2024-11-19 16:57:47', 'string');
INSERT INTO `users` VALUES (2, 'stri88ng', 'string222', 'string', 'string', 0, 0, 0, 0, 1, '2024-11-19 16:58:41', 'string');
INSERT INTO `users` VALUES (3, 'openid_example', 'nickname_example', 'https://example.com/avatar.png', '1234567890', 1, 100, 50, 10, 1, '2024-11-19 17:09:14', '127.0.0.1');
INSERT INTO `users` VALUES (4, 'o5555555penid_example', 'nick888name_example', 'https://example.com/avatar.png', '1234567890', 1, 100, 50, 10, 1, '2024-11-19 17:09:49', '127.0.0.1');

SET FOREIGN_KEY_CHECKS = 1;
