"""
Create volcano.db then load data from CSV files
"""
import csv
from pathlib import Path
import sqlite3

import etlhelper as etl  # pip install etlhelper~=1.0

DB_FILE = Path("volcano.db")
VOLCANO_CSV = Path("GVP_Volcano_List_Holocene_202408261410.csv")
COUNTRIES_CSV = Path("cia_world_factbook_population.csv")
CREATE_VOLCANO_SQL = """
    CREATE TABLE volcano (
        volcano_number INTEGER PRIMARY KEY,
        volcano_name TEXT,
        country TEXT,
        volcanic_region TEXT,
        volcanic_province TEXT,
        volcano_landform TEXT,
        primary_volcano_type TEXT,
        activity_evidence TEXT,
        last_known_eruption TEXT,
        latitude FLOAT,
        longitude FLOAT,
        elevation FLOAT,
        tectonic_setting TEXT,
        dominant_rock_type TEXT
    )"""

CREATE_COUNTRY_SQL = """
    CREATE TABLE country (
        name TEXT,
        slug TEXT PRIMARY KEY,
        population INTEGER,
        ranking INTEGER,
        region TEXT
    );"""

CREATE_VIEW_SQL = """
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
      LIMIT 10;"""

def create_volcano_db():
    with sqlite3.connect(DB_FILE) as conn:
        # Create tables
        etl.execute(CREATE_VOLCANO_SQL, conn)
        etl.execute(CREATE_COUNTRY_SQL, conn)
        etl.execute(CREATE_VIEW_SQL, conn)

        with open(VOLCANO_CSV, "rt") as f:
            next(f)  # Skip header
            next(f)  # Skip header
            reader = csv.DictReader(f)
            etl.load('volcano', conn, reader, transform=_transform_volcano)

        with open(COUNTRIES_CSV, "rt") as f:
            next(f)  # Skip header
            reader = csv.DictReader(f)
            etl.load('country', conn, reader, transform=_transform_country)


def _transform_volcano(chunk):
    """Rename elevation column."""
    for row in chunk:
        row["elevation"] = row.pop("elevation_(m)")
        yield row


def _transform_country(chunk):
    """
    Drop empty data_of_information column, rename population and cast to int.
    """
    for row in chunk:
        row['population'] = int(row.pop('value').replace(',', ''))
        row.pop("date_of_information")
        yield row


if __name__ == "__main__":
    DB_FILE.unlink(missing_ok=True)
    create_volcano_db()
