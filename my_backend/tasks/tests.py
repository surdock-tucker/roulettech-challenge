from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task

class TaskTests(APITestCase):
    def setUp(self):
        self.task = Task.objects.create(name="Test Task", description="Test Description", completed=False)
    
    def test_get_tasks(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        response = self.client.post('/api/tasks/create/', {'name': 'New Task', 'description': 'New Description', 'completed': False})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)
    
    def test_update_task(self):
        response = self.client.put(f'/api/tasks/update/{self.task.id}/', {'name': 'Updated Task', 'description': 'Updated Description', 'completed': True})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.name, 'Updated Task')
    
    def test_delete_task(self):
        response = self.client.delete(f'/api/tasks/delete/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
