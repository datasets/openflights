from pathlib import Path

import requests


BASE_URL = "https://raw.githubusercontent.com/jpatokal/openflights/master/data"
FILES = [
    "airports.dat",
    "airports-extended.dat",
    "airlines.dat",
    "routes.dat",
    "planes.dat",
    "countries.dat",
]


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    data_dir = root / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    for name in FILES:
        url = f"{BASE_URL}/{name}"
        response = requests.get(url, timeout=60)
        response.raise_for_status()
        (data_dir / name).write_text(response.text, encoding="utf-8")
        print(f"updated {name}")


if __name__ == "__main__":
    main()
