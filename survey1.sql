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
-- Table structure for table `survey1`
--

DROP TABLE IF EXISTS `survey1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `survey1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gender` varchar(255) DEFAULT NULL,
  `age` varchar(255) DEFAULT NULL,
  `education` varchar(255) DEFAULT NULL,
  `language` varchar(20) DEFAULT NULL,
  `userid` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `userid` (`userid`),
  CONSTRAINT `survey1_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `user` (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `survey1`
--

LOCK TABLES `survey1` WRITE;
/*!40000 ALTER TABLE `survey1` DISABLE KEYS */;
INSERT INTO `survey1` VALUES (1,'F','25-34','Hsg','telugu','f926ec24-7bb3-11e4-b139-f04da2ed7578'),(2,'F','18-24','Assoc','english','f11addae-7bb5-11e4-b139-f04da2ed7578'),(3,'F','25-34','Scnd','english','4a8795f8-7bb6-11e4-b139-f04da2ed7578'),(4,'O','35-44','Bach','telugu','9bd86716-7bb6-11e4-b139-f04da2ed7578'),(5,'F','45-54','Scnd','c','e746d71e-7bb6-11e4-b139-f04da2ed7578'),(6,'F','25-34','Grad','c','6eca2542-7bb7-11e4-b139-f04da2ed7578'),(7,'O','35-44','Grad','french','2c044f14-7bba-11e4-b139-f04da2ed7578'),(8,'F','45-54','Grad','dety','04324c6c-7bbe-11e4-9afb-f04da2ed7578'),(9,'O','35-44','Scnd','english','5f65a20a-7bbe-11e4-9afb-f04da2ed7578'),(10,'F','25-34','Assoc','english','ae035628-7bbe-11e4-9afb-f04da2ed7578'),(11,'F','45-54','Hsg','marathi','0943fa56-7bbf-11e4-9afb-f04da2ed7578'),(12,'F','55','Assoc','polish','bf646886-7bc2-11e4-9afb-f04da2ed7578'),(13,'F','18-24','Assoc','telugu','6b346792-7bc3-11e4-9afb-f04da2ed7578'),(14,'F','lt18','Hsg','german','d7627364-7bc3-11e4-9afb-f04da2ed7578'),(15,'O','55','Hsg','english','32ec3a08-7bc4-11e4-9afb-f04da2ed7578'),(16,'F','25-34','Hsg','german','6ec3f1ec-7bc4-11e4-9afb-f04da2ed7578'),(17,'F','25-34','Hsg','telugu','0a94f9b8-7bc5-11e4-9afb-f04da2ed7578');
/*!40000 ALTER TABLE `survey1` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-12-04  9:58:56
