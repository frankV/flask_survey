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

-- Dump completed on 2014-12-04  9:58:52
