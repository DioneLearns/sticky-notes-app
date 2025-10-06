from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Note
from django.urls import reverse

class NoteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.note = Note.objects.create(
            title='Test Note',
            content='Test Content',
            author=self.user
        )

    def test_note_creation(self):
        self.assertEqual(self.note.title, 'Test Note')
        self.assertEqual(self.note.content, 'Test Content')
        self.assertEqual(self.note.author, self.user)

    def test_note_list_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_note_create_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('create_note'), {
            'title': 'New Test Note',
            'content': 'New Test Content'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertTrue(Note.objects.filter(title='New Test Note').exists())

    def test_note_edit_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('edit_note', args=[self.note.id]), {
            'title': 'Updated Note',
            'content': 'Updated Content'
        })
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Note')

    def test_note_delete_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('delete_note', args=[self.note.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(id=self.note.id).exists())

    def test_login_view(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after login

    def test_register_view(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password': 'newpass123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after registration
        self.assertTrue(User.objects.filter(username='newuser').exists())
