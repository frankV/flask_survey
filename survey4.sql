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
-- Table structure for table `survey4`
--

DROP TABLE IF EXISTS `survey4`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `survey4` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `computerTime` varchar(255) DEFAULT NULL,
  `pass_random` tinyint(1) DEFAULT NULL,
  `pass_reuse` tinyint(1) DEFAULT NULL,
  `pass_modify` tinyint(1) DEFAULT NULL,
  `pass_new` tinyint(1) DEFAULT NULL,
  `pass_substitute` tinyint(1) DEFAULT NULL,
  `pass_multiword` tinyint(1) DEFAULT NULL,
  `pass_phrase` tinyint(1) DEFAULT NULL,
  `pass_O` varchar(255) DEFAULT NULL,
  `how_regular_file` tinyint(1) DEFAULT NULL,
  `how_encrypted` tinyint(1) DEFAULT NULL,
  `how_software` tinyint(1) DEFAULT NULL,
  `how_cellphone` tinyint(1) DEFAULT NULL,
  `how_browser` tinyint(1) DEFAULT NULL,
  `how_write_down` tinyint(1) DEFAULT NULL,
  `how_no` tinyint(1) DEFAULT NULL,
  `comments` varchar(255) DEFAULT NULL,
  `userid` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `userid` (`userid`),
  CONSTRAINT `survey4_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `user` (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `survey4`
--

LOCK TABLES `survey4` WRITE;
/*!40000 ALTER TABLE `survey4` DISABLE KEYS */;
INSERT INTO `survey4` VALUES (1,'3-5',0,0,0,0,0,1,0,'',0,0,1,0,0,0,0,'working fine','f926ec24-7bb3-11e4-b139-f04da2ed7578'),(2,'6-10',0,0,0,1,0,0,0,'',0,1,0,0,0,0,1,'','f11addae-7bb5-11e4-b139-f04da2ed7578'),(3,'6-10',0,1,1,0,0,0,0,'',0,1,0,1,0,0,0,'','4a8795f8-7bb6-11e4-b139-f04da2ed7578'),(4,'3-5',0,0,1,0,1,0,0,'',0,0,1,0,1,0,0,'','9bd86716-7bb6-11e4-b139-f04da2ed7578'),(5,'6-10',0,0,0,1,0,1,0,'',0,0,1,0,0,1,0,'nice survey','e746d71e-7bb6-11e4-b139-f04da2ed7578'),(6,'6-10',0,1,0,0,0,1,0,'',0,0,0,0,1,0,0,'good job','6eca2542-7bb7-11e4-b139-f04da2ed7578'),(7,'6-10',0,1,0,1,0,0,0,'ntng',0,1,0,0,1,0,0,'ntng','2c044f14-7bba-11e4-b139-f04da2ed7578'),(8,'mt10',0,0,1,0,0,1,0,'',1,0,0,0,0,0,1,'','04324c6c-7bbe-11e4-9afb-f04da2ed7578'),(9,'6-10',0,0,1,0,0,0,1,'',1,0,0,0,0,0,1,'','5f65a20a-7bbe-11e4-9afb-f04da2ed7578'),(10,'6-10',0,1,0,0,0,1,0,'',1,0,0,0,1,0,0,'','ae035628-7bbe-11e4-9afb-f04da2ed7578'),(11,'3-5',0,1,0,0,1,0,0,'',0,1,0,0,0,1,0,'','0943fa56-7bbf-11e4-9afb-f04da2ed7578'),(12,'6-10',0,1,0,0,0,1,0,'no',1,0,0,1,0,0,0,'no','bf646886-7bc2-11e4-9afb-f04da2ed7578'),(13,'6-10',0,0,1,0,1,0,0,'no',0,1,0,0,0,0,0,'no','6b346792-7bc3-11e4-9afb-f04da2ed7578'),(14,'6-10',0,0,1,0,0,0,1,'nhtng',1,0,0,1,0,0,0,'mhty','d7627364-7bc3-11e4-9afb-f04da2ed7578'),(15,'6-10',1,0,0,0,1,0,0,'d!',0,0,0,0,1,0,0,'der','0a94f9b8-7bc5-11e4-9afb-f04da2ed7578');
/*!40000 ALTER TABLE `survey4` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-12-04  9:59:09
