# SQL for SFDC via GRAX and DuckDB

Structured Query Language (SQL) is the one of the most powerful tools for data reuse, analytics and reporting.

While the Salesforce Object Query Language (SOQL) looks like SQL, SOQL has many limitations that make it difficult or impossible to use to answer advanced analytics questions.

The [GRAX Data API](https://apidocs.grax.io/) plus the [DuckDB analytical database](https://duckdb.org/) offers the ability to run rich SQL queries.

Furthermore this can all run on your laptop replacing the need for databases, data warehouses, and Salesforce Data Extract Transform Load (ETL) jobs.

To get started

- [Get GRAX](https://grax.com), [connect to Salesforce](https://documentation.grax.com/docs/connecting-salesforce), and [start the data collector](https://documentation.grax.com/docs/auto-backup)
- Log into the web app and generate a [public API key](https://documentation.grax.com/docs/public-api)

## How it works

Write SQL queries that reference Salesforce object names plus a `.csv` extension. This module uses the GRAX API to fetch CSV data then uses DuckDB to query it.

```sql
-- Count without SOQL timeouts
SELECT COUNT(*) FROM Contact.csv;

-- Transform with SQL functions
SELECT Email, CONCAT_WS(' ', FirstName, LastName) AS Name FROM Contact.csv;

-- Use Common Table Expressions (CTE), subqueries, etc. to join and aggregate without limits
WITH Contacts AS (
    SELECT
    AccountId, Email, CONCAT_WS(' ', FirstName, LastName) AS Name
    FROM Contact.csv
),
Accounts AS (
    SELECT
    a.Id, a.Name AS AccountName,
    (SELECT Name FROM Account.csv WHERE Id = a.ParentId) AS ParentAccountName
    FROM Account.csv a
)
SELECT
c.*, a.AccountName, a.ParentAccountName
FROM Accounts a
JOIN Contacts c ON c.AccountId = a.Id
WHERE ParentAccountName IS NOT NULL
LIMIT 20;
```

## Quick Start

Set up the Python virtual env, packages and GRAX API settings:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.sample .env # and fill in GRAX_API_URL, GRAX_API_TOKEN
```

Run queries:

```bash
python main.py sql/Count.sql
Downloading Contact.csv...
   count_star()
0        106084
```
