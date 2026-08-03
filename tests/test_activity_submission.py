import importlib.util
from pathlib import Path


spec = importlib.util.spec_from_file_location("appmod", Path(__file__).resolve().parents[1] / "src" / "app.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_submit_activity_adds_new_entry():
    original_count = len(module.activities)
    payload = {
        "name": "Robotics Club",
        "description": "Build and compete with robots.",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "age_range": "Middle School",
        "venue_name": "Innovation Lab",
        "venue_address": "77 Maker Street, Mergington",
    }

    result = module.submit_activity(payload)

    assert result["name"] == "Robotics Club"
    assert "Robotics Club" in module.activities
    assert len(module.activities) == original_count + 1
    assert module.activities["Robotics Club"]["venue"]["name"] == "Innovation Lab"
    assert module.activities["Robotics Club"]["age_range"] == "Middle School"


def test_submit_activity_requires_name_and_venue():
    try:
        module.submit_activity({"description": "Missing required fields"})
        assert False, "Expected validation error"
    except ValueError:
        pass
