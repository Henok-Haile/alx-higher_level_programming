-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 14-my_genres.sql)
-- Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT ts.`title`
  FROM `tv_shows` AS ts
       INNER JOIN `tv_show_genres` AS tsg
       ON ts.`id` = tsg.`show_id`

       INNER JOIN `tv_genres` AS tg
       ON tg.`id` = tsg.`genre_id`
       WHERE tg.`name` = "Comedy"
 ORDER BY ts.`title`;
