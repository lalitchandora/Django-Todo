import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Task

class TaskTests(TestCase):
    def test_was_added_today(self):
        date = timezone.now().date()

        task = Task(title = 'sample title',text = 'sample text',date = date)
        self.assertIs(task.was_added_today(),True)

    