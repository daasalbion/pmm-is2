
#./manage test adm en consola
from django.test import TestCase, Client
from django.contrib.auth.models import User
class TestLogin(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'adriana'
        self.email = 'test@test.com'
        self.password = 'adrisila'
        self.test_user = User.objects.create_user(self.username, self.email, self.password)

    def test_login_exitoso(self):
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)

