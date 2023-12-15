"""
The module is responsible for loading textures and the
ways in which these factors are stored in the project.
"""
import json
from pathlib import Path

"""
Paths to fixture files
"""
path_for_meal = Path('fixtures', 'meal.json')
path_for_categories_meal = Path('fixtures', 'categories_meal.json')


def loading_fixtures(path_for_file: str | Path) -> dict:
    """
    Downloading fixture files.

    :param path_for_file: str | Path
    :return: dict
    """
    with open(path_for_file, 'r', encoding='utf-8') as file_read_json:
        return json.load(file_read_json)
