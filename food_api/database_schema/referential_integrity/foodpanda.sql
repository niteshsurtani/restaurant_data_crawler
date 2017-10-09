CREATE TABLE IF NOT EXISTS `city` (
  `city_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `data_resource` varchar(255) NOT NULL,
  PRIMARY KEY (`city_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `locality` (
  `locality_id` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `city_id` int(11) NOT NULL,
  `data_resource` varchar(255) NOT NULL,
  PRIMARY KEY (`locality_id`),
  FOREIGN KEY (`city_id`) REFERENCES city(`city_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE IF NOT EXISTS `restaurants` (
  `restaurant_id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `rating` float DEFAULT NULL,
  `delivery_fee` float DEFAULT NULL,
  `delivery_time` varchar(16) DEFAULT NULL,
  `takeaway_time` varchar(16) DEFAULT NULL,
  `minimum_order` float DEFAULT NULL,
  `payment_methods` tinyint(1) DEFAULT NULL,
  `voucher` tinyint(1) DEFAULT NULL,
  `data_resource` varchar(255) NOT NULL,
  PRIMARY KEY (`restaurant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `cuisine` (
  `cuisine_id` int(11) NOT NULL,
  `cuisine_name` varchar(255) NOT NULL,
  PRIMARY KEY (`cuisine_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `dish` (
  `dish_id` int(11) NOT NULL,
  `dish_name` varchar(255) NOT NULL,
  PRIMARY KEY (`dish_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `locality_restaurant` (
  `locality_id` int(11) NOT NULL,
  `restaurant_id` varchar(255) NOT NULL,
   PRIMARY KEY (`locality_id`,`restaurant_id`),
   CONSTRAINT fk_rest FOREIGN KEY (`restaurant_id`) REFERENCES restaurants(`restaurant_id`) ON DELETE CASCADE ON UPDATE CASCADE,
   CONSTRAINT fk_loc FOREIGN KEY (`locality_id`) REFERENCES locality(`locality_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE IF NOT EXISTS `cuisine_restaurant` (
  `cuisine_id` int(11) NOT NULL,
  `restaurant_id` varchar(255) NOT NULL,
  PRIMARY KEY (`cuisine_id`,`restaurant_id`),
  FOREIGN KEY (`restaurant_id`) REFERENCES restaurants(`restaurant_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`cuisine_id`) REFERENCES `cuisine`(`cuisine_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `menu` (
  `menu_id` int(11) NOT NULL,
  `restaurant_id` varchar(255) NOT NULL,
  `dish_id` int(11) NOT NULL,
  `cost` float NOT NULL,
  `type` varchar(255),
  `data_resource` varchar(255),
  PRIMARY KEY (`menu_id`),
  FOREIGN KEY (`restaurant_id`) REFERENCES restaurants(`restaurant_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`dish_id`) REFERENCES `dish`(`dish_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;
