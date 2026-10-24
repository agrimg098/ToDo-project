from django.test import TestCase
from django.urls import reverse
from .models import Todo


class TodoAppTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse("todo:list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Taskflow")

    def test_add_task(self):
        response = self.client.post(reverse("todo:list"), {"action": "add", "title": "Test task"})
        self.assertRedirects(response, reverse("todo:list"))
        self.assertTrue(Todo.objects.filter(title="Test task").exists())

    def test_toggle_task(self):
        task = Todo.objects.create(title="Toggle me")
        self.client.post(reverse("todo:toggle", args=[task.pk]))
        task.refresh_from_db()
        self.assertTrue(task.is_completed)

    def test_delete_task(self):
        task = Todo.objects.create(title="Delete me")
        self.client.post(reverse("todo:delete", args=[task.pk]))
        self.assertFalse(Todo.objects.filter(pk=task.pk).exists())
