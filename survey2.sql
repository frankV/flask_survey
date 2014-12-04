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
-- Table structure for table `survey2`
--

DROP TABLE IF EXISTS `survey2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `survey2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `major` varchar(255) DEFAULT NULL,
  `department` varchar(30) DEFAULT NULL,
  `count` varchar(255) DEFAULT NULL,
  `unique` varchar(255) DEFAULT NULL,
  `userid` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `userid` (`userid`),
  CONSTRAINT `survey2_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `user` (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `survey2`
--

LOCK TABLES `survey2` WRITE;
/*!40000 ALTER TABLE `survey2` DISABLE KEYS */;
INSERT INTO `survey2` VALUES (1,'Y','computer science','lt5','N','f926ec24-7bb3-11e4-b139-f04da2ed7578'),(2,'N','computer science','lt5','N','f11addae-7bb5-11e4-b139-f04da2ed7578'),(3,'N','x','5-10','N','4a8795f8-7bb6-11e4-b139-f04da2ed7578'),(4,'N','computer science','lt5','Y','9bd86716-7bb6-11e4-b139-f04da2ed7578'),(5,'N','computer science','lt5','N','e746d71e-7bb6-11e4-b139-f04da2ed7578'),(6,'O','computer science','lt5','N','6eca2542-7bb7-11e4-b139-f04da2ed7578'),(7,'N','arts','5-10','N','2c044f14-7bba-11e4-b139-f04da2ed7578'),(8,'O','mechanical engineering','5-10','N','04324c6c-7bbe-11e4-9afb-f04da2ed7578'),(9,'O','computer science','gt20','N','5f65a20a-7bbe-11e4-9afb-f04da2ed7578'),(10,'O','mechanical engineering','5-10','N','ae035628-7bbe-11e4-9afb-f04da2ed7578'),(11,'N','arts','5-10','N','0943fa56-7bbf-11e4-9afb-f04da2ed7578'),(12,'N','music','11-20','Y','bf646886-7bc2-11e4-9afb-f04da2ed7578'),(13,'O','finr arts','lt5','Y','6b346792-7bc3-11e4-9afb-f04da2ed7578'),(14,'N','computer science','lt5','N','d7627364-7bc3-11e4-9afb-f04da2ed7578'),(15,'N','computer science','lt5','N','0a94f9b8-7bc5-11e4-9afb-f04da2ed7578');
/*!40000 ALTER TABLE `survey2` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-12-04  9:59:01
