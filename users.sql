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
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `oldPassword` varchar(20) DEFAULT NULL,
  `changedPass` tinyint(1) DEFAULT NULL,
  `role` smallint(6) DEFAULT NULL,
  `s1` tinyint(1) DEFAULT NULL,
  `s2` tinyint(1) DEFAULT NULL,
  `s3` tinyint(1) DEFAULT NULL,
  `s4` tinyint(1) DEFAULT NULL,
  `lastSeen` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `userid` (`userid`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,NULL,'admin@surveys.ecit.fsu.edu','unconquered',NULL,0,1,0,0,0,0,NULL),(2,'f926ec24-7bb3-11e4-b139-f04da2ed7578','ss14ak@my.fsu.edu','ertertert','qweqweqwe',1,0,1,1,1,1,'2014-12-04'),(3,'f11addae-7bb5-11e4-b139-f04da2ed7578','ss14ak1@my.fsu.edu','dsadsadsa','asdasdasd',1,0,1,1,1,1,'2014-12-04'),(4,'4a8795f8-7bb6-11e4-b139-f04da2ed7578','ss14ak2@my.fsu.edu','qweqweqwe','asdasdasd',1,0,1,1,1,1,'2014-12-04'),(5,'9bd86716-7bb6-11e4-b139-f04da2ed7578','ss14ak3@my.fsu.edu','bnmbnmbnm','asdasdasd',1,0,1,1,1,1,'2014-12-04'),(6,'e746d71e-7bb6-11e4-b139-f04da2ed7578','ss14ak4@my.fsu.edu','qazqazqaz','asdasdasd',1,0,1,1,1,1,'2014-12-04'),(7,'6eca2542-7bb7-11e4-b139-f04da2ed7578','ss14ak5@my.fsu.edu','wsxwsxwsx','asdasdasd',1,0,1,1,1,1,'2014-12-04'),(8,'2c044f14-7bba-11e4-b139-f04da2ed7578','ss14ak6@my.fsu.edu','987987987','789789789',1,0,1,1,1,1,'2014-12-04'),(9,'04324c6c-7bbe-11e4-9afb-f04da2ed7578','s1@my.fsu.edu','poiuytrewq','qwertyuiop',1,0,1,1,1,1,'2014-12-04'),(10,'5f65a20a-7bbe-11e4-9afb-f04da2ed7578','s2@my.fsu.edu','lkjhgfdsa','asdfghjkl',1,0,1,1,1,1,'2014-12-04'),(11,'ae035628-7bbe-11e4-9afb-f04da2ed7578','s3@my.fsu.edu','cdecdecde','edcedcedc',1,0,1,1,1,1,'2014-12-04'),(12,'0943fa56-7bbf-11e4-9afb-f04da2ed7578','s4@my.fsu.edu','vfrvfrvfr','rfvrfvrfv',1,0,1,1,1,1,'2014-12-04'),(13,'bf646886-7bc2-11e4-9afb-f04da2ed7578','s6@my.fsu.edu','redredred','derderder',1,0,1,1,1,1,'2014-12-04'),(14,'6b346792-7bc3-11e4-9afb-f04da2ed7578','s7@my.fsu.edu','puypuypuy','yupyupyup',1,0,1,1,1,1,'2014-12-04'),(15,'d7627364-7bc3-11e4-9afb-f04da2ed7578','s8@my.fsu.edu','147147147','741741741',1,0,1,1,1,1,'2014-12-04'),(16,'32ec3a08-7bc4-11e4-9afb-f04da2ed7578','s9@my.fsu.edu','852852852','852852852',0,0,1,0,0,0,'2014-12-04'),(17,'6ec3f1ec-7bc4-11e4-9afb-f04da2ed7578','s19@my.fsu.edu','963963963','963963963',0,0,1,0,0,0,'2014-12-04'),(18,'0a94f9b8-7bc5-11e4-9afb-f04da2ed7578','a@fsu.edu','45454545','12121212',1,0,1,1,1,1,'2014-12-04'),(19,'98d9f0fc-7bc5-11e4-9afb-f04da2ed7578','a2@fsu.edu','edueduedu','edueduedu',0,0,0,0,0,0,NULL),(20,'d38dfe6e-7bc5-11e4-9afb-f04da2ed7578','a3@fsu.edu','qwerqwer','qwerqwer',0,0,0,0,0,0,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-12-04  9:59:18
