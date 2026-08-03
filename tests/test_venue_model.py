import importlib.util
from pathlib import Path


spec = importlib.util.spec_from_file_location("appmod", Path(__file__).resolve().parents[1] / "src" / "app.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_venues_group_multiple_activities():
    assert hasattr(module, "venues")
    assert "STEM Center" in module.venues
    assert len(module.venues["STEM Center"]["activities"]) >= 2
    assert {"Programming Class", "Math Club"}.issubset(
        set(module.venues["STEM Center"]["activities"])
    )


def test_activities_include_venue_and_age_range():
    assert module.activities
    for activity in module.activities.values():
        assert "venue" in activity
        assert "age_range" in activity
        assert "name" in activity["venue"]
        assert "address" in activity["venue"]
