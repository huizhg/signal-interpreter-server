from pytest import fixture
import json
import os


@fixture
def test_basic_json():
    current_dir = os.path.abspath(__file__)
    json_file_path = os.path.join(current_dir, "fixtures/test_basic.json")
    with open(json_file_path, "r") as json_file:
        content = json.load(json_file)
        return content
