import argparse
import csv
import json
import os
import time
from pathlib import Path

import requests

CACHE_DIR = Path("cache")
CACHE_DIR.mkdir(exist_ok=True)

HEADERS = {
    "User-Agent": "CountriesParser/1.0 (https://example.com)"
}


def sanitize(name: str) -> str:
    return name.replace(" ", "_")


def fetch_country_data(country: str) -> str | None:
    """Search country in Wikidata and fetch full entity JSON."""
    cache_file = CACHE_DIR / f"{sanitize(country)}.json"

    if cache_file.exists():
        return cache_file.read_text(encoding="utf-8")

    # Search entity
    search_url = "https://www.wikidata.org/w/api.php"
    params = {
        "action": "wbsearchentities",
        "search": country,
        "language": "en",
        "format": "json",
        "limit": 1
    }

    r = requests.get(search_url, params=params, headers=HEADERS, timeout=15)
    r.raise_for_status()
    result = r.json()

    if not result.get("search"):
        return None

    qid = result["search"][0]["id"]

    # Fetch entity data
    entity_url = f"https://www.wikidata.org/wiki/Special:EntityData/{qid}.json"
    r = requests.get(entity_url, headers=HEADERS, timeout=15)
    r.raise_for_status()

    cache_file.write_text(r.text, encoding="utf-8")
    time.sleep(1)
    return r.text


def parse_wikidata(json_text: str) -> dict:
    """Extract capital, area and population from Wikidata entity."""
    data = json.loads(json_text)
    entity = next(iter(data["entities"].values()))
    claims = entity.get("claims", {})

    result = {"city": "", "area": "", "population": ""}

    # ---- Capital (P36) ----
    try:
        cap = claims["P36"][0]["mainsnak"]["datavalue"]["value"]
        result["city"] = cap.get("id", "")
    except Exception:
        pass

    # ---- Area (P2046) ----
    areas = []
    for c in claims.get("P2046", []):
        try:
            val = float(c["mainsnak"]["datavalue"]["value"]["amount"])
            areas.append(val)
        except Exception:
            pass
    if areas:
        result["area"] = str(int(max(areas)))

    # ---- Population (P1082) ----
    pops = []
    for c in claims.get("P1082", []):
        try:
            val = float(c["mainsnak"]["datavalue"]["value"]["amount"])
            if val > 1_000_000:   # ignore strange small values
                pops.append(val)
        except Exception:
            pass
    if pops:
        result["population"] = str(int(max(pops)))

    return result


def resolve_city_name(qid: str) -> str:
    """Get English label of a city by its QID."""
    if not qid:
        return ""

    url = f"https://www.wikidata.org/wiki/Special:EntityData/{qid}.json"
    r = requests.get(url, headers=HEADERS, timeout=15)
    r.raise_for_status()

    data = r.json()
    entity = next(iter(data["entities"].values()))
    return entity.get("labels", {}).get("en", {}).get("value", "")


def main():
    parser = argparse.ArgumentParser(description="Parse countries data from Wikidata")
    parser.add_argument("-i", "--input", default="countries.txt",
                        help="Input file with country names")
    parser.add_argument("-o", "--output", default="countries_data.csv",
                        help="Output CSV file")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print("Input file not found:", args.input)
        return

    with open(args.input, encoding="utf-8") as f:
        countries = [line.strip() for line in f if line.strip()]

    results = []

    for country in countries:
        try:
            print(f"Processing: {country}")
            json_text = fetch_country_data(country)
            if not json_text:
                print(f"  Not found in Wikidata: {country}")
                continue

            parsed = parse_wikidata(json_text)
            city_name = resolve_city_name(parsed.get("city", ""))

            results.append({
                "country": country,
                "city": city_name,
                "area": parsed.get("area", ""),
                "population": parsed.get("population", "")
            })

        except Exception as e:
            print(f"Error with {country}: {e}")

    with open(args.output, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["country", "city", "area", "population"]
        )
        writer.writeheader()
        writer.writerows(results)

    print(f"\nSaved to {args.output}")


if __name__ == "__main__":
    main()
