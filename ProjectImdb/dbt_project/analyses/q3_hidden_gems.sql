WITH title_categories AS (
    SELECT
        title_id,
        CASE WHEN average_rating >= 8.0 AND num_votes BETWEEN 100 AND 5000 THEN 1 ELSE 0 END AS is_hidden_gem,
        CASE WHEN average_rating <= 5.5 AND num_votes > 25000 THEN 1 ELSE 0 END AS is_overrated
    FROM fct_title_ratings
),

genre_statistics AS (
    SELECT
        g.genre,
        SUM(c.is_hidden_gem) AS total_hidden_gems,
        SUM(c.is_overrated) AS total_overrated
    FROM stg_title_genres g
    JOIN title_categories c ON g.title_id = c.title_id
    GROUP BY g.genre
)

SELECT
    genre,
    total_hidden_gems,
    total_overrated,
    ROUND(CAST(total_hidden_gems AS FLOAT) / NULLIF(total_overrated, 0), 2) AS gems_vs_overrated_ratio
FROM genre_statistics
WHERE total_hidden_gems > 0 OR total_overrated > 0
ORDER BY gems_vs_overrated_ratio DESC NULLS LAST;