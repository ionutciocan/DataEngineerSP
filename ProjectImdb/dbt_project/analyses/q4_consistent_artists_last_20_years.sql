WITH combined_data AS (
    SELECT
        p.primary_name AS artist_name,
        b.role,
        t.title_id,
        r.average_rating,
        g.genre
    FROM bridge_title_crew b
    JOIN dim_person p ON b.name_id = p.name_id
    JOIN dim_title t ON b.title_id = t.title_id
    JOIN fct_title_ratings r ON b.title_id = r.title_id
    JOIN stg_title_genres g ON t.title_id = g.title_id
    WHERE t.start_year >= EXTRACT(YEAR FROM CURRENT_DATE) - 20
      AND b.role IN ('director', 'actor', 'actress')
),

aggregated_stats AS (
    SELECT
        artist_name,
        role AS primary_role,
        COUNT(DISTINCT title_id) AS total_movies,
        ROUND(AVG(average_rating), 2) AS consistent_average_rating,
        MODE(genre) AS predominant_genre
    FROM combined_data
    GROUP BY artist_name, role
)

SELECT *
FROM aggregated_stats
WHERE total_movies >= 5
ORDER BY consistent_average_rating DESC, total_movies DESC
LIMIT 20;