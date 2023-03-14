from django.test import TestCase, Client
from django.urls import reverse


def test_dummy():
    assert 1


class TestOCLettingsSite(TestCase):
    def test_index_oc_lettings_site(self):
        title_name = "Holiday Homes"
        client = Client()
        response = client.get(reverse("index"))
        title = f"<title>{title_name}</title>"
        h1 = f"<h1>Welcome to {title_name}</h1>"
        respons_content = response.content.decode()
        assert response.status_code == 200
        assert title in respons_content
        assert h1 in respons_content
