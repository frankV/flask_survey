-- MySQL dump 10.13  Distrib 5.5.40, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: survey
-- ------------------------------------------------------
-- Server version	5.5.40-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `survey3`
--

DROP TABLE IF EXISTS `survey3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `survey3` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `choose_names` tinyint(1) DEFAULT NULL,
  `choose_numbers` tinyint(1) DEFAULT NULL,
  `choose_songs` tinyint(1) DEFAULT NULL,
  `choose_mnemonic` tinyint(1) DEFAULT NULL,
  `choose_sports` tinyint(1) DEFAULT NULL,
  `choose_famous` tinyint(1) DEFAULT NULL,
  `choose_words` tinyint(1) DEFAULT NULL,
  `choose_other` tinyint(1) DEFAULT NULL,
  `specify` varchar(255) DEFAULT NULL,
  `secure_numbers` tinyint(1) DEFAULT NULL,
  `secure_upper_case` tinyint(1) DEFAULT NULL,
  `secure_symbols` tinyint(1) DEFAULT NULL,
  `secure_eight_chars` tinyint(1) DEFAULT NULL,
  `secure_no_dict` tinyint(1) DEFAULT NULL,
  `secure_adjacent` tinyint(1) DEFAULT NULL,
  `secure_nothing` tinyint(1) DEFAULT NULL,
  `secure_other` tinyint(1) DEFAULT NULL,
  `specify1` varchar(255) DEFAULT NULL,
  `modify` varchar(255) DEFAULT NULL,
  `usedPassword` varchar(255) DEFAULT NULL,
  `number_N` tinyint(1) DEFAULT NULL,
  `number_changed_slightly` tinyint(1) DEFAULT NULL,
  `number_changed_completely` tinyint(1) DEFAULT NULL,
  `number_added_digits` tinyint(1) DEFAULT NULL,
  `number_deleted_digits` tinyint(1) DEFAULT NULL,
  `number_substituted_digits` tinyint(1) DEFAULT NULL,
  `number_O` varchar(255) DEFAULT NULL,
  `char_N` tinyint(1) DEFAULT NULL,
  `char_changed_slightly` tinyint(1) DEFAULT NULL,
  `char_changed_completly` tinyint(1) DEFAULT NULL,
  `char_added_symbols` tinyint(1) DEFAULT NULL,
  `char_deleted_symbols` tinyint(1) DEFAULT NULL,
  `char_substituted_symbols` tinyint(1) DEFAULT NULL,
  `not_changed1` tinyint(1) DEFAULT NULL,
  `changed_slightly1` tinyint(1) DEFAULT NULL,
  `changed_completly1` tinyint(1) DEFAULT NULL,
  `capatalized1` tinyint(1) DEFAULT NULL,
  `addedwords` tinyint(1) DEFAULT NULL,
  `deletedwords` tinyint(1) DEFAULT NULL,
  `char_O` varchar(255) DEFAULT NULL,
  `userid` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `userid` (`userid`),
  CONSTRAINT `survey3_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `user` (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `survey3`
--

LOCK TABLES `survey3` WRITE;
/*!40000 ALTER TABLE `survey3` DISABLE KEYS */;
INSERT INTO `survey3` VALUES (1,0,1,0,0,0,0,0,0,'',0,1,0,0,0,0,0,0,'','Y','N',0,0,NULL,1,0,NULL,NULL,0,0,1,0,0,NULL,0,0,0,0,1,0,NULL,'f926ec24-7bb3-11e4-b139-f04da2ed7578'),(2,0,1,0,0,0,0,0,0,'',1,0,0,0,0,1,0,0,'','Y','Y',0,0,NULL,0,0,NULL,NULL,0,0,1,0,0,NULL,0,1,0,1,0,0,NULL,'f11addae-7bb5-11e4-b139-f04da2ed7578'),(3,0,1,0,0,0,0,0,0,'',1,0,0,0,0,0,1,0,'','Y','Y',0,1,NULL,0,0,NULL,NULL,0,1,0,0,0,NULL,0,1,0,0,0,0,NULL,'4a8795f8-7bb6-11e4-b139-f04da2ed7578'),(4,0,1,0,0,0,0,0,1,'',0,1,0,0,0,0,0,1,'','Y','Y',0,0,NULL,1,0,NULL,NULL,0,1,1,0,0,NULL,0,0,0,1,0,0,NULL,'9bd86716-7bb6-11e4-b139-f04da2ed7578'),(5,0,1,0,1,0,0,1,0,'',0,1,0,1,0,0,0,0,'','Y','N',1,0,NULL,0,0,NULL,NULL,0,0,1,0,0,NULL,1,0,0,0,1,0,NULL,'e746d71e-7bb6-11e4-b139-f04da2ed7578'),(6,0,1,0,0,0,0,0,0,'',0,0,0,1,0,0,0,0,'','Y','N',0,0,NULL,0,0,NULL,NULL,0,0,1,0,0,NULL,0,0,0,1,0,0,NULL,'6eca2542-7bb7-11e4-b139-f04da2ed7578'),(7,0,1,0,0,0,1,0,0,'',1,0,0,0,1,0,0,0,'','Y','N',0,0,NULL,0,0,NULL,NULL,1,0,0,0,1,NULL,0,1,1,0,1,0,NULL,'2c044f14-7bba-11e4-b139-f04da2ed7578'),(8,0,1,0,0,0,0,1,0,'',1,0,0,1,0,0,0,0,'','Y','N',1,0,NULL,0,0,NULL,NULL,0,0,1,0,1,NULL,0,1,0,0,1,0,NULL,'04324c6c-7bbe-11e4-9afb-f04da2ed7578'),(9,0,1,0,0,1,0,0,0,'',0,1,0,0,1,0,0,0,'','N','Y',0,1,NULL,1,0,NULL,NULL,0,1,0,1,0,NULL,0,0,1,0,0,1,NULL,'5f65a20a-7bbe-11e4-9afb-f04da2ed7578'),(10,0,1,0,0,0,1,0,0,'no',0,1,0,0,1,0,0,0,'no','N','Y',1,1,NULL,0,1,NULL,NULL,1,1,0,1,0,NULL,1,0,1,0,0,1,NULL,'ae035628-7bbe-11e4-9afb-f04da2ed7578'),(11,1,0,0,1,0,0,0,1,'',0,1,0,0,0,1,0,0,'','N','N',0,1,NULL,1,0,NULL,NULL,0,1,0,1,0,NULL,0,1,0,0,1,0,NULL,'0943fa56-7bbf-11e4-9afb-f04da2ed7578'),(12,0,1,0,0,1,0,0,0,'',1,0,0,0,1,0,0,0,'','Y','N',0,1,NULL,1,0,NULL,NULL,1,0,1,0,0,NULL,0,1,0,0,0,1,NULL,'bf646886-7bc2-11e4-9afb-f04da2ed7578'),(13,1,0,1,1,0,0,0,1,'',0,1,0,1,0,0,0,1,'','N','Y',1,0,NULL,0,0,NULL,NULL,1,0,0,1,0,NULL,1,0,0,1,0,0,NULL,'6b346792-7bc3-11e4-9afb-f04da2ed7578'),(14,1,0,0,1,0,0,0,0,'',0,1,0,0,1,0,1,0,'','N','Y',0,1,NULL,1,0,NULL,NULL,1,0,0,1,0,NULL,0,1,0,0,0,1,NULL,'d7627364-7bc3-11e4-9afb-f04da2ed7578'),(15,0,1,0,0,0,1,0,0,'',0,1,0,0,0,0,0,1,'','N','N',0,0,NULL,0,0,NULL,NULL,1,0,0,1,0,NULL,0,0,1,0,0,0,NULL,'0a94f9b8-7bc5-11e4-9afb-f04da2ed7578');
/*!40000 ALTER TABLE `survey3` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-12-04  9:59:04
