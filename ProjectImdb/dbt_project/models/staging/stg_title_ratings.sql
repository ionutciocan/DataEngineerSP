SELECT
tconst AS title_id,
CAST(averageRating AS DOUBLE) AS average_rating,
CAST(numVotes AS INTEGER) AS num_votes
FROM {{source('imdb_raw','title_ratings')}}