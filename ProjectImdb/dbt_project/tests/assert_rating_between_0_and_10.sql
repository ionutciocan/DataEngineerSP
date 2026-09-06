SELECT title_id, average_rating
FROM {{ ref('fct_title_ratings') }}
WHERE average_rating < 0 OR average_rating > 10