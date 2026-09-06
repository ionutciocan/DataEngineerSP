{% snapshot snp_dim_title %}

{{
    config(
      target_schema='snapshots',
      unique_key='title_id',
      strategy='check',
      check_cols=['primary_title', 'genres', 'runtime_minutes']
    )
}}

SELECT
    title_id,
    title_type,
    primary_title,
    original_title,
    is_adult,
    start_year,
    end_year,
    runtime_minutes,
    genres
FROM {{ ref('stg_title_basics') }}

{% endsnapshot %}