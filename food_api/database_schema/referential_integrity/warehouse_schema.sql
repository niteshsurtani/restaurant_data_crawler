CREATE TABLE IF NOT EXISTS `city` (
  `city_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`city_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `locality` (
  `locality_id` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `city_id` int(11) NOT NULL,
  PRIMARY KEY (`locality_id`),
  FOREIGN KEY (`city_id`) REFERENCES city(`city_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;


CREATE TABLE IF NOT EXISTS `restaurants` (
  `restaurant_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `latitude` float NOT NULL,
  `longitude` float NOT NULL,
  `rating` float NOT NULL,
  `country_id` int(11) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `timings` varchar(255) NOT NULL,
  `average_cost_for_two` float NOT NULL,
  `is_pure_veg` varchar(255) NOT NULL,
  `sports_bar_flag` varchar(255) NOT NULL,
  `has_bar` varchar(255) NOT NULL,
  `has_ac` varchar(255) NOT NULL,
  `has_dine_in` varchar(255) NOT NULL,
  `has_delivery` varchar(255) NOT NULL,
  `takeaway_flag` varchar(255) NOT NULL,
  `accepts_credit_cards` varchar(255) NOT NULL,
  `accepts_debit_cards` varchar(255) NOT NULL,
  `sheesha_flag` varchar(255) NOT NULL,
  `halal_flag` varchar(255) NOT NULL,
  `has_wifi` varchar(255) NOT NULL,
  `has_live_music` varchar(255) NOT NULL,
  `nightlife_flag` varchar(255) NOT NULL,
  `stag_entry_flag` varchar(255) NOT NULL,
  `entry_fee` varchar(255) NOT NULL,
  `has_online_delivery` varchar(255) NOT NULL,
  `min_order` varchar(255) NOT NULL,
  `average_delivery_time` varchar(255) NOT NULL,
  `delivery_charge` varchar(255) NOT NULL,
  `accepts_online_payment` varchar(255) NOT NULL,
  PRIMARY KEY (`restaurant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `cuisine` (
  `cuisine_id` int(11) NOT NULL,
  `cuisine_name` varchar(255) NOT NULL,
  PRIMARY KEY (`cuisine_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `dish` (
  `dish_id` int(11) NOT NULL,
  `dish_name` varchar(255) NOT NULL,
  PRIMARY KEY (`dish_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `locality_restaurant` (
  `locality_id` int(11) NOT NULL,
  `restaurant_id` int(11) NOT NULL,
   PRIMARY KEY (`locality_id`,`restaurant_id`),
   CONSTRAINT fk_rest FOREIGN KEY (`restaurant_id`) REFERENCES restaurants(`restaurant_id`) ON DELETE CASCADE ON UPDATE CASCADE,
   CONSTRAINT fk_loc FOREIGN KEY (`locality_id`) REFERENCES locality(`locality_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE IF NOT EXISTS `cuisine_restaurant` (
  `cuisine_id` int(11) NOT NULL,
  `restaurant_id` int(11) NOT NULL,
  PRIMARY KEY (`cuisine_id`,`restaurant_id`),
  FOREIGN KEY (`restaurant_id`) REFERENCES restaurants(`restaurant_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`cuisine_id`) REFERENCES `cuisine`(`cuisine_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `menu` (
  `menu_id` int(11) NOT NULL,
  `restaurant_id` int(11) NOT NULL,
  `dish_id` int(11) NOT NULL,
  `cost` float NOT NULL,
  `type` varchar(255),
  `data_resource` varchar(255),
  PRIMARY KEY (`menu_id`),
  FOREIGN KEY (`restaurant_id`) REFERENCES restaurants(`restaurant_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`dish_id`) REFERENCES `dish`(`dish_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;
