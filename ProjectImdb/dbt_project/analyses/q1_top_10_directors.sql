SELECT
    p.primary_name AS director,
    COUNT(r.title_id) AS total_movies,
    SUM(r.num_votes) AS total_votes,
    ROUND(AVG(r.average_rating), 2) AS average_rating
FROM bridge_title_crew b
JOIN dim_person p ON b.name_id = p.name_id
JOIN fct_title_ratings r ON b.title_id = r.title_id
WHERE b.role = 'director'
GROUP BY p.name_id, p.primary_name
HAVING COUNT(r.title_id) >= 5 AND SUM(r.num_votes) >= 1000
ORDER BY average_rating DESC
LIMIT 10;