SELECT
tconst AS title_id,
CAST(ordering AS INTEGER) AS ordering,
nconst AS name_id,
category,
job,
characters
FROM {{source('imdb_raw','title_principals')}}