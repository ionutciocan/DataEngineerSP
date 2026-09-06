SELECT
nconst AS name_id,
primaryName AS primary_name,
CAST(birthYear AS INTEGER) AS birth_year,
CAST(deathYear AS INTEGER) AS death_year,
primaryProfession AS primary_profession,
knownForTitles AS known_for_titles
FROM {{source('imdb_raw','name_basics')}}
