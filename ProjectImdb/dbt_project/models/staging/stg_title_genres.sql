SELECT title_id,
UNNEST(STRING_SPLIT(genres,',')) AS genre
FROM {{ ref('stg_title_basics')}}
WHERE genres IS NOT NULL