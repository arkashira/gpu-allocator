from collections import deque
from typing import Tuple, Dict, Any
import time

class Detector:
    """
    A class to detect anomalies in GPU usage events.
    """

    def __init__(self, alert_service, LOCATION_WINDOW_SEC=3600):
        self.alert_service = alert_service
        self.user_stats = {}
        self.LOCATION_WINDOW_SEC = LOCATION_WINDOW_SEC

    def process_event(self, event: Dict[str, Any]) -> bool:
        """
        Processes an event and detects anomalies. Returns True if an alert is emitted, False otherwise.
        """
        try:
            user_id = event['user_id']
            usage_percent = event.get('usage_percent', 0)
            location = event.get('location', 'unknown')
        except KeyError:
            print("Error: Missing required field 'user_id'.")
            return False

        # Validate required fields
        if not all([user_id, usage_percent, location]):
            print("Error: Missing required fields.")
            return False

        # Initialize user stats if not present
        if user_id not in self.user_stats:
            self.user_stats[user_id] = _UserStats()

        # Update per-user statistics
        self.user_stats[user_id].update(usage_percent)

        # Maintain per-user location deque
        current_time = time.time()
        if user_id not in self.user_stats:
            self.user_stats[user_id] = _LocationHistory()
        self.user_stats[user_id].locations.append((location, current_time))
        self.user_stats[user_id].prune_old_entries(current_time, self.LOCATION_WINDOW_SEC)

        # Detect statistical outliers using the 3σ rule
        if self.user_stats[user_id].is_outlier():
            self.alert_service.send_alert(f"Statistical outlier detected for user {user_id}")
            return True

        # Detect location-hopping using the distinct-location count
        if self.user_stats[user_id].is_location_hopping():
            self.alert_service.send_alert(f"Location hopping detected for user {user_id}")
            return True

        return False


class _UserStats:
    def __init__(self):
        self.usage_history = []
        self.locations = deque()

    def update(self, usage_percent):
        self.usage_history.append(usage_percent)

    def prune_old_entries(self, current_time, window_sec):
        while self.locations and current_time - self.locations[0][1] > window_sec:
            self.locations.popleft()

    def is_outlier(self):
        # Placeholder for actual outlier detection logic
        return len(self.usage_history) > 3

    def is_location_hopping(self):
        # Placeholder for actual location hopping detection logic
        return len(set(loc for loc, _ in self.locations)) > 3


# Minimal test to ensure the module parses correctly
if __name__ == "__main__":
    import py_compile
    py_compile.compile("detector.py")