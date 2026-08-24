{{ config(severity = 'warn') }}

SELECT title_id, start_year
FROM {{ ref('dim_title') }}
WHERE start_year > EXTRACT(YEAR FROM CURRENT_DATE)