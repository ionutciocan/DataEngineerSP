SELECT
    CAST(FLOOR(start_year / 10.0) * 10 AS INT) AS decade,
    ROUND(AVG(runtime_minutes), 2) AS average_runtime_minutes,
    COUNT(title_id) AS total_movies
FROM dim_title
WHERE start_year IS NOT NULL
  AND runtime_minutes IS NOT NULL
  AND title_type = 'movie'
GROUP BY 1
ORDER BY decade;

SELECT
    ROUND(CORR(t.runtime_minutes, r.average_rating), 4) AS runtime_rating_correlation
FROM dim_title t
JOIN fct_title_ratings r ON t.title_id = r.title_id
WHERE t.runtime_minutes IS NOT NULL
  AND r.average_rating IS NOT NULL
  AND t.title_type = 'movie';