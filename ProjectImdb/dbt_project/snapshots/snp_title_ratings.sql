{% snapshot snp_title_ratings %}

{{
    config(
      target_schema='snapshots',
      unique_key='title_id',
      strategy='check',
      check_cols=['average_rating', 'num_votes']
    )
}}

SELECT * FROM {{ ref('stg_title_ratings') }}

{% endsnapshot %}