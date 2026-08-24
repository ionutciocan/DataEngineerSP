SELECT
    title_id,
    average_rating,
    num_votes
FROM {{ ref('stg_title_ratings') }}