import unittest
from unittest.mock import patch
from gpu_allocator.src.notifications.alerts import send_alert, PolicyViolationAlert

class TestAlerts(unittest.TestCase):
    def test_send_alert(self):
        with patch('gpu_allocator.src.notifications.alerts.notify') as mock_notify:
            send_alert(PolicyViolationAlert('Policy 1', 'Violation reason'))
            mock_notify.assert_called_once_with('Policy 1: Violation reason')

    def test_send_multiple_alerts(self):
        with patch('gpu_allocator.src.notifications.alerts.notify') as mock_notify:
            send_alert(PolicyViolationAlert('Policy 1', 'Violation reason 1'))
            send_alert(PolicyViolationAlert('Policy 2', 'Violation reason 2'))
            mock_notify.assert_has_calls([call('Policy 1: Violation reason 1'), call('Policy 2: Violation reason 2')])

    def test_no_alert_when_policy_not_violated(self):
        with patch('gpu_allocator.src.notifications.alerts.notify') as mock_notify:
            send_alert(PolicyViolationAlert('Policy 1', 'Not violated'))
            mock_notify.assert_not_called()