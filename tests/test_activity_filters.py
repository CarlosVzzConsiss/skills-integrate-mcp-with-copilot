import importlib.util
from pathlib import Path


spec = importlib.util.spec_from_file_location("appmod", Path(__file__).resolve().parents[1] / "src" / "app.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_activities_include_filter_metadata():
    assert module.activities
    for activity in module.activities.values():
        assert "category" in activity
        assert "age_group" in activity


def test_get_filtered_activities_filters_by_category_and_age_group():
    results = module.get_filtered_activities(category="Sports", age_group="Middle School")
    assert results
    assert all(item["category"] == "Sports" for item in results.values())
    assert all(item["age_group"] == "Middle School" for item in results.values())
