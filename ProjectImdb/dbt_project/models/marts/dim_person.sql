SELECT
    name_id,
    primary_name,
    birth_year,
    death_year,
    primary_profession,
    UNNEST(STRING_SPLIT(known_for_titles, ',')) AS known_for_title
FROM {{ ref('stg_name_basics') }}