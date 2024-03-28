import duckdb
import os
from zipfile import ZipFile
import re
import requests
from io import BytesIO
import time
from dotenv import load_dotenv

load_dotenv()


def queryFile(path):
    with open(path) as f:
        return query(f.read())


def query(q):
    cursor = duckdb.connect()
    try:
        return cursor.execute(q)
    except duckdb.duckdb.IOException as e:
        if "No files found" in str(e):
            matches = re.compile(r'"([^"]+).csv"').findall(str(e))
            if matches:
                download(matches[0])
                return query(q)


def csvname(object):
    return f"{object}.csv"


def download(object):
    name = csvname(object)

    if exists(object):
        print(f"Using {name}...")
        return

    print(f"Downloading {name}...")
    res = requests.get(
        f"{os.environ['GRAX_API_URL']}/api/v1/salesforce/fromAuth/objects/{object}/records/download",
        headers={
            "Authorization": "Bearer " + os.environ["GRAX_API_TOKEN"],
        },
    )

    with open("out.zip", "wb") as file:
        file.write(res.content)

    zf = ZipFile(BytesIO(res.content))
    data = zf.read(f"{object}.csv").decode("utf-8")
    with open(name, "w") as file:
        file.write(data)

    os.remove("out.zip")


def exists(object):
    name = csvname(object)

    if not os.path.exists(name):
        return False

    if os.path.getmtime(name) < time.time() - (24 * 60 * 60):
        return False

    return True
