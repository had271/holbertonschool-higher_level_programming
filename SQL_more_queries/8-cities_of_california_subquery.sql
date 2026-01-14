-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;
-- Lists all the cities of California that can be found
SELECT `id`, `name`
  FROM `cities`
 WHERE `state_id` IN
       (SELECT `id`
	  FROM `states`
	 WHERE `name` = "California")
 ORDER BY `id`;
