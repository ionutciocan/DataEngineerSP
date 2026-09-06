SELECT
titleID AS title_id,
CAST(ordering AS INTEGER) AS ordering,
title,
region,
language,
types,
attributes,
isOriginalTitle AS is_original_title
FROM {{source('imdb_raw','title_akas')}}