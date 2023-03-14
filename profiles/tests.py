from django.test import TestCase, Client
from django.urls import reverse
from factories import UserFactory, ProfileFactory


class TestProfile(TestCase):
    def setUp(self):
        self.client = Client()
        self.users = UserFactory.create_batch(1)
        self.profile = ProfileFactory()

    def test_profile_index(self):
        title_name = "Profiles"
        response = self.client.get(reverse("profiles:index"))
        title = f"<title>{title_name}</title>"
        h1 = f"<h1>{title_name}</h1>"
        response_content = response.content.decode()
        assert response.status_code == 200
        assert title in response_content
        assert h1 in response_content

    def test_profile_page(self):
        response = self.client.get(
            reverse("profiles:profile", kwargs={"username": self.profile})
        )
        response_content = response.content.decode()
        title = f"<title>{self.profile}</title>"
        h1 = f"<h1>{self.profile}</h1>"
        first_name = f"<p>First name: {self.profile.user.first_name}</p>"
        last_name = f"<p>Last name: {self.profile.user.last_name}</p>"
        email = f"<p>Email: {self.profile.user.email}</p>"
        favorite_city = f"<p>Favorite city: {self.profile.favorite_city}</p>"
        assert response.status_code == 200
        assert title in response_content
        assert h1 in response_content
        assert first_name in response_content
        assert last_name in response_content
        assert email in response_content
        assert favorite_city in response_content
