/*
 Navicat Premium Data Transfer

 Source Server         : 本地
 Source Server Type    : MySQL
 Source Server Version : 80029
 Source Host           : 192.168.51.200:3306
 Source Schema         : tigerdata

 Target Server Type    : MySQL
 Target Server Version : 80029
 File Encoding         : 65001

 Date: 30/06/2022 22:43:34
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for config_column_type
-- ----------------------------
DROP TABLE IF EXISTS `config_column_type`;
CREATE TABLE `config_column_type`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `code` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `para` json NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 41 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of config_column_type
-- ----------------------------
INSERT INTO `config_column_type` VALUES (15, 'tinyint', 'tinyint', NULL);
INSERT INTO `config_column_type` VALUES (16, 'smallint', 'smallint', NULL);
INSERT INTO `config_column_type` VALUES (17, 'mediumint', 'mediumint', NULL);
INSERT INTO `config_column_type` VALUES (18, 'int', 'int', NULL);
INSERT INTO `config_column_type` VALUES (19, 'integer', 'integer', NULL);
INSERT INTO `config_column_type` VALUES (20, 'bigint', 'bigint', NULL);
INSERT INTO `config_column_type` VALUES (21, 'float', 'float', NULL);
INSERT INTO `config_column_type` VALUES (22, 'double', 'double', NULL);
INSERT INTO `config_column_type` VALUES (23, 'decimal', 'decimal', NULL);
INSERT INTO `config_column_type` VALUES (24, 'date', 'date', NULL);
INSERT INTO `config_column_type` VALUES (25, 'datetime_between', 'datetime_between', NULL);
INSERT INTO `config_column_type` VALUES (26, 'date_between', 'date_between', NULL);
INSERT INTO `config_column_type` VALUES (27, 'time', 'time', NULL);
INSERT INTO `config_column_type` VALUES (28, 'year', 'year', NULL);
INSERT INTO `config_column_type` VALUES (29, 'datetime', 'datetime', NULL);
INSERT INTO `config_column_type` VALUES (30, 'timestamp', 'timestamp', NULL);
INSERT INTO `config_column_type` VALUES (31, 'char', 'char', NULL);
INSERT INTO `config_column_type` VALUES (32, 'varchar', 'varchar', NULL);
INSERT INTO `config_column_type` VALUES (33, 'tinytext', 'tinytext', NULL);
INSERT INTO `config_column_type` VALUES (34, 'text', 'text', NULL);
INSERT INTO `config_column_type` VALUES (35, 'longtext', 'longtext', NULL);
INSERT INTO `config_column_type` VALUES (36, 'tinyblob', 'tinyblob', NULL);
INSERT INTO `config_column_type` VALUES (37, 'longblob', 'longblob', NULL);
INSERT INTO `config_column_type` VALUES (38, 'mediumblob', 'mediumblob', NULL);
INSERT INTO `config_column_type` VALUES (39, 'enum', 'enum', NULL);
INSERT INTO `config_column_type` VALUES (40, 'set', 'set', NULL);

SET FOREIGN_KEY_CHECKS = 1;
