import duckdb
import os

print("RAW DATA: Title.basics")
query = "SELECT * FROM 'ProjectImdb/raw/title.basics.parquet' LIMIT 5"
duckdb.sql(query).show()

print("RAW DATA: Name.basics")
query = "SELECT * FROM 'ProjectImdb/raw/name.basics.parquet' LIMIT 5"
duckdb.sql(query).show()

print("RAW DATA: Title.akas")
query = "SELECT * FROM 'ProjectImdb/raw/title.akas.parquet' LIMIT 5"
duckdb.sql(query).show()

print("RAW DATA: Title.crew")
query = "SELECT * FROM 'ProjectImdb/raw/title.crew.parquet' LIMIT 5"
duckdb.sql(query).show()

print("RAW DATA: Title.principals")
query = "SELECT * FROM 'ProjectImdb/raw/title.principals.parquet' LIMIT 5"
duckdb.sql(query).show()

print("RAW DATA: Title.ratings")
query = "SELECT * FROM 'ProjectImdb/raw/title.ratings.parquet' LIMIT 5"
duckdb.sql(query).show()


os.chdir('ProjectImdb/dbt_project')
con = duckdb.connect('../warehouse.duckdb', read_only=True)

print("TEST STAGING: stg_title_genres")
query = """
    SELECT * 
    FROM stg_title_genres 
    WHERE title_id = 'tt0000003'
"""
con.sql(query).show()

print("Q1: Top 10 Directors (Highest Avg Rating)")
q1 = con.sql("""
SELECT
    p.primary_name AS director,
    COUNT(r.title_id) AS total_movies,
    SUM(r.num_votes) AS total_votes,
    ROUND(AVG(r.average_rating), 2) AS average_rating
FROM bridge_title_crew b
JOIN dim_person p ON b.name_id = p.name_id
JOIN fct_title_ratings r ON b.title_id = r.title_id
WHERE b.role = 'director'
GROUP BY p.name_id, p.primary_name
HAVING COUNT(r.title_id) >= 5 AND SUM(r.num_votes) >= 1000
ORDER BY average_rating DESC
LIMIT 10;
""")
q1.show()

print("Q2: Runtime vs Average Rating Correlation")
q2 = con.sql("""
SELECT
    CASE
        WHEN t.runtime_minutes < 90 THEN '1. Short (< 90 min)'
        WHEN t.runtime_minutes BETWEEN 90 AND 120 THEN '2. Standard (90-120 min)'
        WHEN t.runtime_minutes > 120 THEN '3. Long (> 120 min)'
        ELSE 'Unknown'
    END AS runtime_category,
    COUNT(t.title_id) AS total_movies,
    ROUND(AVG(r.average_rating), 2) AS category_avg_rating
FROM dim_title t
JOIN fct_title_ratings r ON t.title_id = r.title_id
WHERE t.runtime_minutes IS NOT NULL 
  AND t.title_type = 'movie'
GROUP BY 1
ORDER BY 1;
""")
q2.show()

print("Q3: Hidden Gems (>8.5 rating, <10k votes)")
q3 = con.sql("""
SELECT
    t.primary_title AS movie_title,
    t.start_year AS release_year,
    r.average_rating,
    r.num_votes
FROM dim_title t
JOIN fct_title_ratings r ON t.title_id = r.title_id
WHERE t.title_type = 'movie'
  AND r.average_rating >= 8.5
  AND r.num_votes BETWEEN 50 AND 10000
ORDER BY r.average_rating DESC, r.num_votes DESC
LIMIT 10;
""")
q3.show()

print("Q4: Consistent Artists (Last 20 Years) & Main Genres")
q4 = con.sql("""
SELECT
    p.primary_name AS artist,
    tg.genre AS main_genre,
    COUNT(DISTINCT r.title_id) AS total_movies,
    ROUND(AVG(r.average_rating), 2) AS average_rating
FROM bridge_title_crew b
JOIN dim_person p ON b.name_id = p.name_id
JOIN fct_title_ratings r ON b.title_id = r.title_id
JOIN dim_title t ON b.title_id = t.title_id
JOIN stg_title_genres tg ON t.title_id = tg.title_id
WHERE t.start_year >= 2006
  AND t.title_type = 'movie'
GROUP BY p.name_id, p.primary_name, tg.genre
HAVING COUNT(DISTINCT r.title_id) >= 5
ORDER BY average_rating DESC, total_movies DESC
LIMIT 10;
""")
q4.show()