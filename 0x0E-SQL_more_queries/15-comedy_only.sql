-- Lists all comedy shows
SELECT s.`title` FROM `tv_shows` AS s
INNER JOIN `tv_show_genres` AS g
ON s.`id` = g.`show_id`
INNER JOIN `tv_genres` AS t
ON g.`genre_id` = t.`id`
WHERE t.`name` = 'Comedy'
ORDER BY s.`title` ASC;