SELECT
tconst AS title_id,
titleType AS title_type,
primaryTitle AS primary_title,
originalTitle AS original_title,
CAST(isAdult AS INTEGER) AS is_adult,
CAST(startYear AS INTEGER) AS start_year,
CAST(endYear AS INTEGER) AS end_year,
CAST(runtimeMinutes AS INTEGER) AS runtime_minutes,
genres
FROM {{source('imdb_raw','title_basics')}}