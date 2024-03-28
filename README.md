# SFDC DuckDB via GRAX

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.sample .env # and fill in GRAX_API_URL, GRAX_API_TOKEN
python main.py
python test.py
python -m black .
```

Once you have data in CSVs you can also query directly with `duckdb`:

```bash
brew install duckdb
duckdb -cmd '.maxrows 500' -line < sql/AccountTree.sql
```
