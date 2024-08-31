-- query
SELECT * FROM volcano;

-- query, order, filter, limit
SELECT volcano_name, country, elevation
FROM volcano
WHERE country IS "Iceland"
ORDER BY elevation DESC
LIMIT 10;

-- join
SELECT
 v.*,
 c.*
FROM volcano v
  JOIN country c
  ON v.country = c.name;

-- group by and sums
SELECT
 v.country,
 COUNT(1) as volcano_count,
 c.population as total_population,
 c.population / COUNT(1) as people_per_volcano,
 ROUND(AVG(v.elevation)) as mean_elevation
FROM volcano v
  JOIN country c
  ON v.country = c.name
GROUP BY v.country
ORDER BY people_per_volcano ASC
LIMIT 10;

-- create view
CREATE VIEW people_per_volcano AS
  SELECT
   v.country,
   COUNT(1) as volcano_count,
   c.population as total_population,
   c.population / COUNT(1) as people_per_volcano,
   ROUND(AVG(v.elevation)) as mean_elevation
  FROM volcano v
    JOIN country c
    ON v.country = c.name
  GROUP BY v.country
  ORDER BY people_per_volcano ASC
  LIMIT 10;