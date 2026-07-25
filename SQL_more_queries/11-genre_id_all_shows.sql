-- Lists all shows and displays NULL when a show has no genre.

-- Uses a left join to keep shows that have no linked genre.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
