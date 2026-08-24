WITH principals AS (
    SELECT
        title_id,
        name_id,
        category AS role
    FROM {{ ref('stg_title_principals') }}
),

directors AS (
    SELECT
        title_id,
        UNNEST(STRING_SPLIT(directors, ',')) AS name_id,
        'director' AS role
    FROM {{ ref('stg_title_crew') }}
    WHERE directors IS NOT NULL
),

writers AS (
    SELECT
        title_id,
        UNNEST(STRING_SPLIT(writers, ',')) AS name_id,
        'writer' AS role
    FROM {{ ref('stg_title_crew') }}
    WHERE writers IS NOT NULL
)

SELECT * FROM principals
UNION
SELECT * FROM directors
UNION
SELECT * FROM writers