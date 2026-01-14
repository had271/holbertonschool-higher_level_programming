-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT g.genre_id, t.title
FROM tv_shows AS t
INNER JOIN tv_show_genres AS g ON g.genre_id = t.show_id
ORDER BY t.title, g.genre_id;
