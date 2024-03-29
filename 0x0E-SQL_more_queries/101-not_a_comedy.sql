-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 100-not_my_genres.sql)
--
-- Write a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
--
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT DISTINCT `title`
  FROM `tv_shows` AS ts
       LEFT JOIN `tv_show_genres` AS tsg
       ON tsg.`show_id` = ts.`id`

       LEFT JOIN `tv_genres` AS tg
       ON tg.`id` = tsg.`genre_id`
       WHERE ts.`title` NOT IN
             (SELECT `title`
                FROM `tv_shows` AS ts
	             INNER JOIN `tv_show_genres` AS tsg
		     ON tsg.`show_id` = ts.`id`

		     INNER JOIN `tv_genres` AS tg
		     ON tg.`id` = tsg.`genre_id`
		     WHERE tg.`name` = "Comedy")
 ORDER BY `title`;
