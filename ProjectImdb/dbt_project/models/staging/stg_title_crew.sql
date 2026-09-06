SELECT
tconst AS title_id,
directors,
writers
FROM {{source('imdb_raw','title_crew')}}