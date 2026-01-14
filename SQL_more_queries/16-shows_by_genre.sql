-- Liists all shows, and all genres linked to that show
SELECT s.title AS title,
  g.name AS name
FROM tv_shows AS s
  LEFT JOIN tv_show_genres AS t ON t.show_id = s.id
  LEFT JOIN tv_genres AS g ON g.id = t.genre_id 
ORDER BY s.title, g.name ASC;
