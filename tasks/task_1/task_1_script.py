import json
import re
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "task1_d.json"
DB_PATH = BASE_DIR / "task1.db"

to_usd = 1.2


def load_raw_records(path: Path) -> list[tuple[str, str, int, float]]:
    
    raw = path.read_text(encoding="utf-8")

    fixed_json_text = re.sub(
        r':(\w+)=>',              
        lambda m: f'"{m.group(1)}": ',
        raw,
    )

    data = json.loads(fixed_json_text)
   

    rows: list[tuple[str, str, int, float]] = []

    for item in data:
        book_id = str(item["id"])       
        title = item["title"]
        year = int(item["year"])

        price_str: str = item["price"]   
        m = re.search(r'(\d+(?:\.\d+)?)', price_str)
        if not m:
            raise ValueError(f"Cannot parse price from: {price_str!r}")
        price_eur = float(m.group(1))    

        rows.append((book_id, title, year, price_eur))

    return rows


def load_to_db(db_path: Path, rows: list[tuple[str, str, int, float]]) -> None:
    """
    Create an SQLite database, a books_raw table, and a summary table books_summary.
    Transformation (year, count, average price in USD) is done INSIDE the database (SQL).
    """
    conn = sqlite3.connect(db_path)
    try:
        cur = conn.cursor()

        # raw table
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS books_raw (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                publication_year INTEGER NOT NULL,
                price_eur REAL NOT NULL
            )
            """
        )


        cur.execute("DELETE FROM books_raw")

        cur.executemany(
            """
            INSERT INTO books_raw (id, title, publication_year, price_eur)
            VALUES (?, ?, ?, ?)
            """,
            rows,
        )

        # 2. summary table

        cur.execute("DROP TABLE IF EXISTS books_summary")

        cur.execute(
            """
            CREATE TABLE books_summary AS
            SELECT
                publication_year,
                COUNT(*) AS book_count,
                ROUND(AVG(price_eur * ?), 2) AS average_price_usd
            FROM books_raw
            GROUP BY publication_year
            ORDER BY publication_year
            """,
            (to_usd,),
        )

        conn.commit()

        # counting rows
        cur.execute("SELECT COUNT(*) FROM books_raw")
        raw_count = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM books_summary")
        summary_count = cur.fetchone()[0]

        print(f"books_raw rows: {raw_count}")
        print(f"books_summary rows: {summary_count}")

    finally:
        conn.close()


def main() -> None:
    rows = load_raw_records(DATA_PATH)
    load_to_db(DB_PATH, rows)


if __name__ == "__main__":
    main()
