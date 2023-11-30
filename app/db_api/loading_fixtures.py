from pathlib import Path
import json


path_for_meal = Path('fixtures', 'meal.json')


def loading_fixtures(path_for_file: str | Path) -> dict:
    with open(path_for_file, 'r', encoding='utf-8') as file_read_json:
        return json.load(file_read_json)
